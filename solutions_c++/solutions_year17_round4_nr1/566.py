#include <bits/stdc++.h>

std::map<std::pair<int, std::vector<int>>, int> f;
std::vector<int> rem;
int n, p;

int solve(std::pair<int, std::vector<int>> S) {
    auto iter = f.find(S);
    if (iter != f.end()) {
        return iter->second;
    }
    else {
        iter = f.insert(std::make_pair(S, 0)).first;
        if (*std::max_element(S.second.begin(), S.second.end()) == 0) return 0;
        else {
            int base = 0;
            if (S.first == 0) ++ base;
            for (int i = 1; i < p; ++ i) if (S.second[i]) {
                auto nS = std::make_pair((S.first + i) % p, S.second);
                -- nS.second[i];
                int tmp = solve(nS);
                if (tmp + base > iter->second) {
                    iter->second = tmp + base;
                }
            }
            return iter->second;
        }
    }
}

int main() {
    int T; std::cin >> T;
    int ca = 0;
    while (ca < T) {
        f.clear();
        std::cin >> n >> p;
        rem.resize(p);
        for (int i = 0; i < p; ++ i) rem[i] = 0;
        for (int i = 0; i < n; ++ i) {
            int x; std::cin >> x;
            ++ rem[x % p];
        }
        int ans = rem[0];
        rem[0] = 0;

        std::cout << "Case #" << ++ ca << ": " << ans + solve(std::make_pair(0, rem)) << std::endl;
    }
}
