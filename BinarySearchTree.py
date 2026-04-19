class Node:
  left: 'Node | None'
  right: 'Node | None'
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

class BinarySearchTree:

  def __init__(self, root):
    self.root = root

  def insert(self, value):
    new_node = Node(value)

    # if root node is None
    if self.root is None:
      self.root = new_node
      return 
    
    curr_node = self.root

    while curr_node:
      # right side
      if value >= curr_node.value:
        if curr_node.right is None:
          curr_node.right = new_node
          return
        curr_node = curr_node.right
      else:
        if curr_node.left is None:
          curr_node.left = new_node
          return
        curr_node = curr_node.left
    return
  
  def lookup(self, value):
    if self.root is None: 
      return False
    curr_node = self.root
    while curr_node:
      if value == curr_node.value:
        return True
      if value > curr_node.value:
        curr_node = curr_node.right
      else:
        curr_node = curr_node.left
    return False


  def remove(self, value):
    if self.root is None:
        return False

    curr_node = self.root
    parent_node = None

    while curr_node:
        if value > curr_node.value:
            parent_node = curr_node
            curr_node = curr_node.right
        elif value < curr_node.value:
            parent_node = curr_node
            curr_node = curr_node.left
        elif value == curr_node.value:

            # Option 1: no right child
            if curr_node.right is None:
                if parent_node is None:
                    self.root = curr_node.left
                else:
                    if curr_node.value < parent_node.value:
                        parent_node.left = curr_node.left
                    else:
                        parent_node.right = curr_node.left

            # Option 2: no left child
            elif curr_node.left is None:
                if parent_node is None:
                    self.root = curr_node.right
                else:
                    if curr_node.value < parent_node.value:  # fix: was swapped
                        parent_node.left = curr_node.right
                    else:
                        parent_node.right = curr_node.right

            # Option 3: both children exist
            # Find in-order successor (leftmost node in right subtree)
            else:
                successor_parent = curr_node
                successor = curr_node.right
                while successor.left:
                    successor_parent = successor
                    successor = successor.left

                curr_node.value = successor.value  # replace value

                # Delete the successor (it has no left child by definition)
                if successor_parent == curr_node:
                    successor_parent.right = successor.right
                else:
                    successor_parent.left = successor.right

            return True

    return False  # value not found
  
  
  def print_tree(self):
      if not self.root:
          print("Empty tree")
          return

      from collections import deque

      # Collect levels with depth and position
      levels = []
      queue = deque([(self.root, 0, 0)])  # node, depth, pos

      while queue:
          node, depth, pos = queue.popleft()
          while len(levels) <= depth:
              levels.append([])
          levels[depth].append((pos, node.value if node else None))
          if node and (node.left or node.right):
              queue.append((node.left, depth + 1, 2 * pos))
              queue.append((node.right, depth + 1, 2 * pos + 1))

      max_depth = len(levels)
      width = 2 ** max_depth * 2

      # Track where each node was printed (pos -> character index)
      prev_char_positions = {}

      for depth, level in enumerate(levels):
          spacing = width // (2 ** depth)
          line = ""
          char_positions = {}

          for i, (pos, val) in enumerate(level):
              target = spacing // 2 + i * spacing
              # Pad to reach target position
              pad = max(0, target - len(line))
              line += " " * pad
              val_str = str(val) if val is not None else " "
              char_positions[pos] = len(line) + len(val_str) // 2  # center of number
              line += val_str

          print(line)

          # Draw branches aligned to actual character positions
          if depth < max_depth - 1:
              branch_line = ""
              for pos, val in level:
                  if val is None:
                      continue
                  center = char_positions[pos]
                  left_slash  = center - 1
                  right_slash = center + 1

                  # Extend branch_line if needed
                  if len(branch_line) < left_slash:
                      branch_line += " " * (left_slash - len(branch_line))
                  branch_line = branch_line[:left_slash] + "/" + " " + "\\"

              print(branch_line)

          prev_char_positions = char_positions


node_9 = Node(9)

tree = BinarySearchTree(node_9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.print_tree()
print(tree.lookup(171))
