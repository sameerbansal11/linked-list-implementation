#!/usr/bin/env python3
"""
linked-list-implementation
Singly and Doubly Linked List with all operations,
visual representation, and interactive menu.

Author: Sameer Bansal
Reg No: RA2311032010061
College: SRM Institute of Science and Technology
Branch: B.Tech CSE (IoT) | Batch: 2023-2027
"""

from __future__ import annotations
import os
from typing import Optional

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"


# ═══════════════════════════════════════════════════════════
# SINGLY LINKED LIST
# ═══════════════════════════════════════════════════════════


class SNode:
    """Node for Singly Linked List"""

    def __init__(self, data: int) -> None:
        self.data: int = data
        self.nxt: Optional[SNode] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[SNode] = None
        self.size: int = 0

    # ── Insert ────────────────────────────────────────────
    def insert_at_beginning(self, data: int) -> str:
        node = SNode(data)
        node.nxt = self.head
        self.head = node
        self.size += 1
        return f"{GREEN}✅ Inserted {data} at beginning{RESET}"

    def insert_at_end(self, data: int) -> str:
        node = SNode(data)
        if not self.head:
            self.head = node
        else:
            curr: SNode = self.head
            while curr.nxt:
                curr = curr.nxt
            curr.nxt = node
        self.size += 1
        return f"{GREEN}✅ Inserted {data} at end{RESET}"

    def insert_at_position(self, data: int, pos: int) -> str:
        if pos < 0 or pos > self.size:
            return f"{RED}❌ Invalid position: {pos} (size={self.size}){RESET}"
        if pos == 0:
            return self.insert_at_beginning(data)
        node = SNode(data)
        curr: SNode = self.head  # type: ignore[assignment]
        for _ in range(pos - 1):
            curr = curr.nxt  # type: ignore[assignment]
        node.nxt = curr.nxt
        curr.nxt = node
        self.size += 1
        return f"{GREEN}✅ Inserted {data} at position {pos}{RESET}"

    def insert_after_value(self, target: int, data: int) -> str:
        curr = self.head
        while curr:
            if curr.data == target:
                node = SNode(data)
                node.nxt = curr.nxt
                curr.nxt = node
                self.size += 1
                return f"{GREEN}✅ Inserted {data} after {target}{RESET}"
            curr = curr.nxt
        return f"{RED}❌ Value {target} not found{RESET}"

    # ── Delete ────────────────────────────────────────────
    def delete_at_beginning(self) -> str:
        if not self.head:
            return f"{RED}❌ List is empty{RESET}"
        val = self.head.data
        self.head = self.head.nxt
        self.size -= 1
        return f"{GREEN}✅ Deleted {val} from beginning{RESET}"

    def delete_at_end(self) -> str:
        if not self.head:
            return f"{RED}❌ List is empty{RESET}"
        if not self.head.nxt:
            val = self.head.data
            self.head = None
            self.size -= 1
            return f"{GREEN}✅ Deleted {val} from end{RESET}"
        curr: SNode = self.head
        while curr.nxt and curr.nxt.nxt:
            curr = curr.nxt  # type: ignore[assignment]
        val = curr.nxt.data  # type: ignore[union-attr]
        curr.nxt = None
        self.size -= 1
        return f"{GREEN}✅ Deleted {val} from end{RESET}"

    def delete_by_value(self, data: int) -> str:
        if not self.head:
            return f"{RED}❌ List is empty{RESET}"
        if self.head.data == data:
            self.head = self.head.nxt
            self.size -= 1
            return f"{GREEN}✅ Deleted {data}{RESET}"
        curr: SNode = self.head
        while curr.nxt:
            if curr.nxt.data == data:
                curr.nxt = curr.nxt.nxt
                self.size -= 1
                return f"{GREEN}✅ Deleted {data}{RESET}"
            curr = curr.nxt  # type: ignore[assignment]
        return f"{RED}❌ Value {data} not found{RESET}"

    def delete_at_position(self, pos: int) -> str:
        if not self.head:
            return f"{RED}❌ List is empty{RESET}"
        if pos < 0 or pos >= self.size:
            return f"{RED}❌ Invalid position: {pos}{RESET}"
        if pos == 0:
            return self.delete_at_beginning()
        curr: SNode = self.head
        for _ in range(pos - 1):
            curr = curr.nxt  # type: ignore[assignment]
        val = curr.nxt.data  # type: ignore[union-attr]
        curr.nxt = curr.nxt.nxt  # type: ignore[union-attr]
        self.size -= 1
        return f"{GREEN}✅ Deleted {val} at position {pos}{RESET}"

    # ── Search & Access ───────────────────────────────────
    def search(self, data: int) -> tuple[int, str]:
        curr = self.head
        index = 0
        while curr:
            if curr.data == data:
                return index, f"{GREEN}✅ Found {data} at index {index}{RESET}"
            curr = curr.nxt
            index += 1
        return -1, f"{RED}❌ {data} not found{RESET}"

    def get_at(self, pos: int) -> tuple[Optional[int], str]:
        if pos < 0 or pos >= self.size:
            return None, f"{RED}❌ Invalid position{RESET}"
        curr: SNode = self.head  # type: ignore[assignment]
        for _ in range(pos):
            curr = curr.nxt  # type: ignore[assignment]
        return curr.data, f"{GREEN}✅ Value at {pos}: {curr.data}{RESET}"

    # ── Utility ───────────────────────────────────────────
    def reverse(self) -> str:
        prev: Optional[SNode] = None
        curr = self.head
        while curr:
            nxt = curr.nxt
            curr.nxt = prev
            prev = curr
            curr = nxt
        self.head = prev
        return f"{GREEN}✅ List reversed{RESET}"

    def sort(self) -> str:
        if not self.head or not self.head.nxt:
            return f"{YELLOW}ℹ️  Nothing to sort{RESET}"
        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            while curr and curr.nxt:
                if curr.data > curr.nxt.data:
                    curr.data, curr.nxt.data = curr.nxt.data, curr.data
                    swapped = True
                curr = curr.nxt
        return f"{GREEN}✅ List sorted in ascending order{RESET}"

    def find_middle(self) -> tuple[Optional[int], str]:
        if not self.head:
            return None, f"{RED}❌ List is empty{RESET}"
        slow = self.head
        fast = self.head
        while fast and fast.nxt:
            slow = slow.nxt  # type: ignore[assignment]
            fast = fast.nxt.nxt
        return slow.data, f"{GREEN}✅ Middle element: {slow.data}{RESET}"  # type: ignore[union-attr]

    def detect_cycle(self) -> tuple[bool, str]:
        slow = self.head
        fast = self.head
        while fast and fast.nxt:
            slow = slow.nxt  # type: ignore[assignment]
            fast = fast.nxt.nxt
            if slow is fast:
                return True, f"{RED}⚠️  Cycle detected!{RESET}"
        return False, f"{GREEN}✅ No cycle detected{RESET}"

    def to_list(self) -> list:
        result: list = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.nxt
        return result

    def display(self, title: str = "Singly Linked List") -> None:
        if not self.head:
            print(f"  {YELLOW}  (empty list){RESET}")
            return
        nodes = self.to_list()
        chain = (
            " → ".join(f"{CYAN}[{n}]{RESET}" for n in nodes) + f" → {RED}NULL{RESET}"
        )
        print(f"\n  {BOLD}{title}{RESET} (size={self.size})")
        print(f"  HEAD → {chain}")
        print(f"  Indexes: ", end="")
        for i, n in enumerate(nodes):
            print(f"{BLUE}[{i:^{len(str(n))+2}}]{RESET}", end=" ")
        print()


# ═══════════════════════════════════════════════════════════
# DOUBLY LINKED LIST
# ═══════════════════════════════════════════════════════════


class DNode:
    """Node for Doubly Linked List"""

    def __init__(self, data: int) -> None:
        self.data: int = data
        self.prv: Optional[DNode] = None
        self.nxt: Optional[DNode] = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[DNode] = None
        self.tail: Optional[DNode] = None
        self.size: int = 0

    # ── Insert ────────────────────────────────────────────
    def insert_at_beginning(self, data: int) -> str:
        node = DNode(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.nxt = self.head
            self.head.prv = node
            self.head = node
        self.size += 1
        return f"{GREEN}✅ Inserted {data} at beginning{RESET}"

    def insert_at_end(self, data: int) -> str:
        node = DNode(data)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prv = self.tail
            self.tail.nxt = node
            self.tail = node
        self.size += 1
        return f"{GREEN}✅ Inserted {data} at end{RESET}"

    def insert_at_position(self, data: int, pos: int) -> str:
        if pos < 0 or pos > self.size:
            return f"{RED}❌ Invalid position: {pos}{RESET}"
        if pos == 0:
            return self.insert_at_beginning(data)
        if pos == self.size:
            return self.insert_at_end(data)
        node = DNode(data)
        curr: DNode = self.head  # type: ignore[assignment]
        for _ in range(pos - 1):
            curr = curr.nxt  # type: ignore[assignment]
        node.nxt = curr.nxt
        node.prv = curr
        if curr.nxt:
            curr.nxt.prv = node
        curr.nxt = node
        self.size += 1
        return f"{GREEN}✅ Inserted {data} at position {pos}{RESET}"

    # ── Delete ────────────────────────────────────────────
    def delete_by_value(self, data: int) -> str:
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prv:
                    curr.prv.nxt = curr.nxt
                else:
                    self.head = curr.nxt
                if curr.nxt:
                    curr.nxt.prv = curr.prv
                else:
                    self.tail = curr.prv
                self.size -= 1
                return f"{GREEN}✅ Deleted {data}{RESET}"
            curr = curr.nxt
        return f"{RED}❌ Value {data} not found{RESET}"

    def delete_at_beginning(self) -> str:
        if not self.head:
            return f"{RED}❌ List is empty{RESET}"
        val = self.head.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.nxt
            if self.head:
                self.head.prv = None
        self.size -= 1
        return f"{GREEN}✅ Deleted {val} from beginning{RESET}"

    def delete_at_end(self) -> str:
        if not self.tail:
            return f"{RED}❌ List is empty{RESET}"
        val = self.tail.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prv
            if self.tail:
                self.tail.nxt = None
        self.size -= 1
        return f"{GREEN}✅ Deleted {val} from end{RESET}"

    # ── Traversal ─────────────────────────────────────────
    def traverse_forward(self) -> list:
        result: list = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.nxt
        return result

    def traverse_backward(self) -> list:
        result: list = []
        curr = self.tail
        while curr:
            result.append(curr.data)
            curr = curr.prv
        return result

    def display(self) -> None:
        if not self.head:
            print(f"  {YELLOW}  (empty list){RESET}")
            return
        nodes = self.traverse_forward()
        forward = " ⇌ ".join(f"{CYAN}[{n}]{RESET}" for n in nodes)
        print(f"\n  {BOLD}Doubly Linked List{RESET} (size={self.size})")
        print(f"  {RED}NULL{RESET} ⇌ {forward} ⇌ {RED}NULL{RESET}")
        print(f"  Forward  : {' → '.join(str(n) for n in nodes)}")
        print(f"  Backward : {' → '.join(str(n) for n in reversed(nodes))}")
        print(
            f"  HEAD: {self.head.data}  |  TAIL: {self.tail.data if self.tail else 'None'}"
        )


# ═══════════════════════════════════════════════════════════
# CIRCULAR LINKED LIST
# ═══════════════════════════════════════════════════════════


class CircularLinkedList:
    def __init__(self) -> None:
        self.head: Optional[SNode] = None
        self.size: int = 0

    def insert(self, data: int) -> str:
        node = SNode(data)
        if not self.head:
            self.head = node
            node.nxt = self.head
        else:
            curr: SNode = self.head
            while curr.nxt is not self.head:
                curr = curr.nxt  # type: ignore[assignment]
            curr.nxt = node
            node.nxt = self.head
        self.size += 1
        return f"{GREEN}✅ Inserted {data} in circular list{RESET}"

    def delete(self, data: int) -> str:
        if not self.head:
            return f"{RED}❌ List is empty{RESET}"
        if self.head.data == data and self.size == 1:
            self.head = None
            self.size -= 1
            return f"{GREEN}✅ Deleted {data}{RESET}"
        curr: SNode = self.head
        while curr.nxt is not self.head:
            if curr.nxt and curr.nxt.data == data:
                curr.nxt = curr.nxt.nxt
                self.size -= 1
                return f"{GREEN}✅ Deleted {data}{RESET}"
            curr = curr.nxt  # type: ignore[assignment]
        return f"{RED}❌ Value {data} not found{RESET}"

    def display(self) -> None:
        if not self.head:
            print(f"  {YELLOW}  (empty circular list){RESET}")
            return
        nodes: list = []
        curr: SNode = self.head
        for _ in range(self.size):
            nodes.append(curr.data)
            curr = curr.nxt  # type: ignore[assignment]
        chain = " → ".join(f"{CYAN}[{n}]{RESET}" for n in nodes)
        print(f"\n  {BOLD}Circular Linked List{RESET} (size={self.size})")
        print(f"  {chain} → {GREEN}(back to HEAD: {self.head.data}){RESET}")


# ── Display & Menu ────────────────────────────────────────
def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def display_banner() -> None:
    print("=" * 58)
    print("       🔗 LINKED LIST IMPLEMENTATION")
    print("       Author : Sameer Bansal | RA2311032010061")
    print("       College: SRMIST Kattankulathur")
    print("=" * 58)


def display_menu() -> None:
    print(f"""
  {BOLD}SINGLY LINKED LIST{RESET}
  [1]  Insert at beginning    [2]  Insert at end
  [3]  Insert at position     [4]  Insert after value
  [5]  Delete at beginning    [6]  Delete at end
  [7]  Delete by value        [8]  Delete at position
  [9]  Search                 [10] Reverse
  [11] Sort                   [12] Find middle
  [13] Detect cycle           [14] Display

  {BOLD}DOUBLY LINKED LIST{RESET}
  [15] Insert at beginning    [16] Insert at end
  [17] Insert at position     [18] Delete by value
  [19] Delete at beginning    [20] Delete at end
  [21] Display (fwd + bwd)

  {BOLD}CIRCULAR LINKED LIST{RESET}
  [22] Insert                 [23] Delete
  [24] Display

  {BOLD}DEMO{RESET}
  [25] Run full demo (all operations)

  [q]  Quit
""")


def run_demo(
    sll: SinglyLinkedList, dll: DoublyLinkedList, cll: CircularLinkedList
) -> None:
    print(f"\n  {BOLD}{CYAN}═══ FULL DEMO — ALL LINKED LIST OPERATIONS ═══{RESET}\n")

    print(f"  {BOLD}── SINGLY LINKED LIST ──{RESET}")
    for v in [10, 20, 30, 40, 50]:
        print(f"  {sll.insert_at_end(v)}")
    print(f"  {sll.insert_at_beginning(5)}")
    print(f"  {sll.insert_at_position(25, 3)}")
    print(f"  {sll.insert_after_value(40, 45)}")
    sll.display()
    print(f"\n  {sll.search(25)[1]}")
    _, msg = sll.get_at(3)
    print(f"  {msg}")
    print(f"  {sll.find_middle()[1]}")
    _, msg2 = sll.detect_cycle()
    print(f"  {msg2}")
    print(f"  {sll.reverse()}")
    sll.display("After Reverse")
    print(f"  {sll.sort()}")
    sll.display("After Sort")
    print(f"  {sll.delete_by_value(25)}")
    print(f"  {sll.delete_at_beginning()}")
    print(f"  {sll.delete_at_end()}")
    sll.display("After Deletions")

    print(f"\n  {BOLD}── DOUBLY LINKED LIST ──{RESET}")
    for v in [100, 200, 300, 400]:
        print(f"  {dll.insert_at_end(v)}")
    print(f"  {dll.insert_at_beginning(50)}")
    print(f"  {dll.insert_at_position(250, 3)}")
    dll.display()
    print(f"  {dll.delete_by_value(250)}")
    print(f"  {dll.delete_at_beginning()}")
    print(f"  {dll.delete_at_end()}")
    dll.display()

    print(f"\n  {BOLD}── CIRCULAR LINKED LIST ──{RESET}")
    for v in [1, 2, 3, 4, 5]:
        print(f"  {cll.insert(v)}")
    cll.display()
    print(f"  {cll.delete(3)}")
    cll.display()


def get_val(prompt: str) -> int:
    val = input(f"  {prompt}: ").strip()
    try:
        return int(val)
    except ValueError:
        return 0


# ── Main ──────────────────────────────────────────────────
def main() -> None:
    clear()
    display_banner()

    sll = SinglyLinkedList()
    dll = DoublyLinkedList()
    cll = CircularLinkedList()

    for v in [10, 20, 30, 40, 50]:
        sll.insert_at_end(v)
    for v in [100, 200, 300]:
        dll.insert_at_end(v)
    for v in [1, 2, 3]:
        cll.insert(v)

    print(f"\n  {GREEN}✅ Pre-loaded with sample data{RESET}")
    sll.display()
    dll.display()
    cll.display()
    display_menu()

    while True:
        try:
            choice = input("\n  Enter option: ").strip().lower()

            if choice == "q":
                print("\n  👋 Goodbye!")
                break
            elif choice == "1":
                print(sll.insert_at_beginning(get_val("Value")))
            elif choice == "2":
                print(sll.insert_at_end(get_val("Value")))
            elif choice == "3":
                v = get_val("Value")
                p = int(input("  Position: ").strip())
                print(sll.insert_at_position(v, p))
            elif choice == "4":
                t = get_val("Target value")
                v = get_val("New value")
                print(sll.insert_after_value(t, v))
            elif choice == "5":
                print(sll.delete_at_beginning())
            elif choice == "6":
                print(sll.delete_at_end())
            elif choice == "7":
                print(sll.delete_by_value(get_val("Value to delete")))
            elif choice == "8":
                print(sll.delete_at_position(int(input("  Position: ").strip())))
            elif choice == "9":
                _, msg = sll.search(get_val("Search value"))
                print(msg)
            elif choice == "10":
                print(sll.reverse())
                sll.display()
            elif choice == "11":
                print(sll.sort())
                sll.display()
            elif choice == "12":
                _, msg = sll.find_middle()
                print(msg)
            elif choice == "13":
                _, msg = sll.detect_cycle()
                print(msg)
            elif choice == "14":
                sll.display()
            elif choice == "15":
                print(dll.insert_at_beginning(get_val("Value")))
            elif choice == "16":
                print(dll.insert_at_end(get_val("Value")))
            elif choice == "17":
                v = get_val("Value")
                p = int(input("  Position: ").strip())
                print(dll.insert_at_position(v, p))
            elif choice == "18":
                print(dll.delete_by_value(get_val("Value to delete")))
            elif choice == "19":
                print(dll.delete_at_beginning())
            elif choice == "20":
                print(dll.delete_at_end())
            elif choice == "21":
                dll.display()
            elif choice == "22":
                print(cll.insert(get_val("Value")))
            elif choice == "23":
                print(cll.delete(get_val("Value to delete")))
            elif choice == "24":
                cll.display()
            elif choice == "25":
                run_demo(SinglyLinkedList(), DoublyLinkedList(), CircularLinkedList())
            elif choice == "menu":
                display_menu()
            else:
                print("  ⚠️  Invalid option. Type 'menu' to see all options.")

        except KeyboardInterrupt:
            print("\n\n  👋 Goodbye!")
            break
        except ValueError as e:
            print(f"  {RED}⚠️  Invalid input: {e}{RESET}")


if __name__ == "__main__":
    main()
