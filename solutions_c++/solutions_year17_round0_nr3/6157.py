#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <queue>

void bstall (int n, int k);

int main() {


    int t;
    int n, k;
    std::cin >> t;

    for (int i = 1; i <= t; ++i) {
        std::cin >> n >> k;
        std::cout << "Case #" << i << ": ";
        bstall(n, k);
        std::cout << std::endl;
    }

    return 0;
}


void bstall (int n, int k) {
    std::multiset<int> q;
    q.insert(n);
    while (k > 1) {
        int prev = *q.rbegin();
        auto tmp = q.end();
        q.erase(--tmp);
        if (prev / 2 > 0) {
            q.insert(prev / 2);
        }
        if (prev - 1 - prev/2 > 0) {
            q.insert(prev - 1 - prev/2);
        }
        k--;
    }
    int emptyStall = *q.rbegin();
    std::cout << emptyStall / 2 << " " << emptyStall - 1 - emptyStall/2;

//    double lg = std::log(k) / std::log(2);
//    int prev = n / std::pow(2, std::floor(lg));
//    std::cout << prev / 2 << " " << prev - 1 - prev/2;

}