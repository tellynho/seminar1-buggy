#include <iostream>
int main() {
    int *p = nullptr;
    std::cout << *p << std::endl; // null pointer dereference
    return 0;
}
