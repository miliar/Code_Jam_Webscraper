#include <iostream>
#include <set>

int main() {
    int T;
    std::cin >> T;
    for (int t = 0; t < T; t++) {
        std::cerr << t << std::endl;
        int n, k;
        std::cin >> n >> k;
        std::multiset<int, std::greater<int>> s;
        s.insert(n);
        for (int i = 0; i < k; i++) {
            int z = *(s.begin());
            s.erase(s.begin());
            z--;
            int a = z/2;
            int b = z - a;
            s.insert(a);
            s.insert(b);
            //std::cout << "Select " << z+1 << "->" << a << " " << b << std::endl;
            if (i == k-1)
                std::cout << "Case #" << t+1 << ": " << b << " " << a << std::endl;
        }
    }
    return 0;
}
