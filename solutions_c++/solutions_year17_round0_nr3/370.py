#include <bits/stdc++.h>

int main() {
    //std::cout << (-1) / 2 << std::endl;
    int T; std::cin >> T;
    for (int t = 1; t <= T; ++ t) {
        long long n, k;
        std::cin >> n >> k;
        long long l = n, r = n;
        //if (l + r < n - 1) ++ r;
        long long sum = 0, cnt = 1;
        while (sum + cnt < k) {
            sum += cnt; cnt *= 2;
            l = (l - 1) / 2; r = r / 2;
        }
        std::cout << "Case #" << t << ": ";
        if (l == r) {
            std::cout << r / 2 << " " << (l - 1) / 2 << std::endl;
        }
        else {
            assert(r == l + 1);
            k -= sum;
            sum += cnt; cnt *= 2;
            -- r; -- l;
            //std::cout << l << " " << r << std::endl;
            //std::cout << sum << " " << cnt << std::endl;
            if (sum > n) {
                std::cout << 0 << " " << 0 << std::endl;
            }
            else {
                int cntr = (n - sum) % (sum + 1), cntl = cnt - cntr;
                if (r % 2 == 0)
                    if (k <= (cnt - cntl * 2) / 2)
                        std::cout << r / 2 << " " << r / 2 << std::endl;
                    else
                        std::cout << r / 2 << " " << r / 2 - 1 << std::endl;
                else
                    if (k <= cntr)
                        std::cout << r / 2 + 1 << " " << r / 2 << std::endl;
                    else 
                        std::cout << r / 2 << " " << r / 2 << std::endl;
            }
        }
    }
}
