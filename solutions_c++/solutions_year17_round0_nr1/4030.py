#include <algorithm>
#include <cassert>
#include <vector>
#include <string>
#include <iostream>

class Tree {
    size_t size;
    std::vector<bool> tree;

public:
    Tree(size_t size) {
        this->size = 1;
        while (this->size < size)
            this->size *= 2;

        tree = std::vector<bool>(2 * this->size);
        for (size_t i = 0; i < tree.size(); ++i)
            tree[i] = false;
    }

    void set(size_t a, size_t b) {
        assert(0 <= a && a <= b && b < size);

        a += size;
        b += size;

        tree[a] = (tree[a] xor true);
        if (a != b)
            tree[b] = (tree[b] xor true);

        while (a / 2 != b / 2) {
            if (a % 2 == 0)
                tree[a + 1] = (tree[a + 1] xor true);

            if (b % 2 == 1)
                tree[b - 1] = (tree[b - 1] xor true);

            a /= 2;
            b /= 2;
        }
    }

    bool get(size_t a) {
        assert(0 <= a && a < size);

        bool result = false;

        a += size;
        while (a > 0) {
            if (tree[a])
                result = result xor true;
            a /= 2;
        }

        return result;
    }
};

int solve(std::string s, int k) {
    Tree tree(s.length());
    int result = 0;

    for (int i = 0; i <= s.length() - k; ++i) {
        if ((s[i] == '+' && !tree.get(i)) || (s[i] == '-' && tree.get(i)))
            continue;

        ++result;

        // std::cout << "set: " << i << ", " << i + k - 1 << std::endl;
        tree.set(i, i + k - 1);
        // for (int j = 0; j < s.length(); ++j)
        //     std::cout << "    " << tree.get(j) << "\n";
    }

    for (int i = 0; i < s.length(); ++i) {
        // std::cout << s[i] << " " << tree.get(i) << std::endl;

        if ((s[i] == '+' && tree.get(i)) || (s[i] == '-' && !tree.get(i)))
            result = -1;
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cout.tie(0);
    std::cin.tie(0);

    int tests_count;
    std::cin >> tests_count;

    for (int i = 0; i < tests_count; ++i) {
        std::string state;
        int k;

        std::cin >> state >> k;

        int s = solve(state, k);

        std::cout << "Case #" << i + 1 << ": ";
        if (s != -1)
            std::cout << s;
        else
            std::cout << "IMPOSSIBLE";
        std::cout << "\n";
    }
}
