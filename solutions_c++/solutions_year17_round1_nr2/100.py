#include <bits/stdc++.h>

const int N = 55;
std::map<int, std::vector<int>> in, out;
std::set<int> all;
std::priority_queue<std::pair<int, int>> candidate[N];
bool deled[N * N];
int l[N * N], r[N * N];
int n, p, x0[N];

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int T;
    std::cin >> T;
    for (int ca = 1; ca <= T; ++ ca) {
        in.clear(); out.clear(); all.clear();

        std::cin >> n >> p;
        for (int i = 0; i < n; ++ i) {
            std::cin >> x0[i];
            while (!candidate[i].empty())
                candidate[i].pop();
        }

        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < p; ++ j) {
                int number = i * p + j;
                int x; std::cin >> x;
                l[number] = ceil(x / 1.1 / x0[i]) + 0.5;
                r[number] = floor(x / 0.9 / x0[i]) + 0.5;
                deled[number] = false;
                in[l[number]].push_back(number);
                out[r[number]].push_back(number);
                if (!all.count(l[number])) all.insert(l[number]);
                if (!all.count(r[number])) all.insert(r[number]);
            }
        }

        int ans = 0;
        for (const auto& x : all) {
            for (const auto& t : in[x]) {
                int i = t / p;
                candidate[i].push(std::make_pair(- r[t], t));
            }

            //std::cout << "in" << std::endl;
            while (true) {
                bool found = true;
                for (int i = 0; i < n; ++ i) {
                    while (!candidate[i].empty() && deled[candidate[i].top().second]) candidate[i].pop();
                    if (candidate[i].empty()) {
                        found = false; break;
                    }
                }
                //std::cout << "middle" << std::endl;
                if (found) {
                    ++ ans;
                    for (int i = 0; i < n; ++ i) {
                        int t = candidate[i].top().second; candidate[i].pop();
                        deled[t] = true;
                    }
                }
                else {
                    break;
                }
            }
            //std::cout << "out" << std::endl;

            for (const auto& t : out[x]) {
                deled[t] = true;
            }
        }

        std::cout << "Case #" << ca << ": " << ans << std::endl;
    }
}
