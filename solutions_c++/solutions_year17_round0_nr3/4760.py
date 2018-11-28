#include <iostream>
#include <algorithm>
#include <tuple>
#include <utility>

class Node {
public:

    Node(int s)
    : size(s)
    {}


    std::pair<int, int> Split() {
        cached = false;
        if (left != nullptr) {
            if (right->Best() > left->Best())
                return right->Split();
            else
                return left->Split();
        } else {
            if (size % 2 == 1) {
                left = new Node(size / 2);
                right = new Node(size / 2);
                return std::pair<int, int>(size / 2, size / 2);
            } else {
                left = new Node(size / 2 - 1);
                right = new Node(size / 2);
                return std::pair<int, int>(size / 2 - 1, size / 2);
            }
        }
    }


    std::pair<int, int> Best() {
        if (cached)
            return best;
        cached = true;
        if (left != nullptr) {
            best = std::max(left->Best(), right->Best());
            return best;
        }
        if (size % 2 == 1) {
            best = std::pair<int, int>(size / 2, size / 2);
        } else {
            best = std::pair<int, int>(size / 2 - 1, size / 2);
        }
        return best;
    }

private:
    int size;
    Node* left = nullptr;
    Node* right = nullptr;
    bool cached = false;
    std::pair<int, int> best;
};

int main() {
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N;
        int K;
        std::cin >> N >> K;
        Node root(N);
        for (int i = 1; i < K; ++i)
            root.Split();
        auto last = root.Split();
        std::cout << "Case #" << t << ": " << last.second << " " << last.first << std::endl;
    }
}
