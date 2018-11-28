// Fresh Chocolate

#include <bits/stdc++.h>

int main() {
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N;
        int P;
        int sum = 0;
        std::vector<int> G;
        std::vector<int> Groups(4, 0);

        std::cin >> N >> P;
        for (int i = 0; i < N; ++i) {
            int tmp;
            std::cin >> tmp;
            ++Groups.at(tmp % P);
            sum += tmp;
        }
        int ans = Groups.at(0);
        int two;
        int three;
        switch (P) {
            case 2: ans += Groups.at(1) >> 1; break;
            case 3: two = std::min(Groups.at(1), Groups.at(2));
                    Groups.at(1) -= two;
                    Groups.at(2) -= two;
                    ans += two + Groups.at(1)/3 + Groups.at(2)/3;
                    break;
            case 4: three = std::min(Groups.at(1), Groups.at(3));
                    Groups.at(1) -= three;
                    Groups.at(3) -= three;
                    ans += three + (Groups.at(2) >> 1);
                    Groups.at(2) >>= 1;
                    ans += Groups.at(1) / 4 + Groups.at(3) / 3;
                    break;
        }
        if (sum % P) {
            ++ans;
        }
        std::cout << "Case #" << t << ": " << ans << std::endl;
    }
    return 0;
}
