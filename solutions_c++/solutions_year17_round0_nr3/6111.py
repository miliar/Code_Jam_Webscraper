#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>

typedef unsigned long long int ull;
typedef long long int ll;

int main() {
    int cc;
    std::cin >> cc;

    for (int c = 0; c < cc; c++) {
        ull n;
        std::cin >> n;
        ull k;
        std::cin >> k;

        std::cout << "Case #" << (c + 1) << ": ";

        ull sq = 1;
        while(sq*2 <= k)
            sq *= 2;
        n -= k;
        ull total = n / sq;

        ull a = 0, b = 0;
        b = total / 2;
        a = b;
        double sa = total / 2.f;
        if(sa != (int)sa)
            a++;

        std::cout << std::max(a, b) << " " << std::min(a, b);
        std::cout << std::endl;

    }
    return 0;
}