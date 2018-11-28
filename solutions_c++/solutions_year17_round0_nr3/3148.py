#include <iostream>
#include <set>

void binary(int n, int k) {
    std::multiset <int> sec;
    sec.insert(n);
    int u, l;
    while (k --) {
        std::multiset <int>::iterator it = sec.end();
        it --;
        int s = *it;
        sec.erase(it);
        u = s >> 1;
        l = (s-1) >> 1;
        sec.insert(l);
        sec.insert(u);
    }
    std::cout << u << " " << l << std::endl;
}

int main() {
    int T, n, k;
    std::cin >> T;
    for (int i = 1; i <= T; i ++) {
        std::cin >> n >> k;
        std::cout << "Case #" << i << ": ";
        binary(n, k);
    }
}
