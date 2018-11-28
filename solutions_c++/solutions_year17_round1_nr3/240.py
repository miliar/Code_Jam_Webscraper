#include <bits/stdc++.h>

int hd, ad, hk, ak, buff, debuff;

void init() {
    std::cin >> hd >> ad >> hk >> ak >> buff >> debuff;
}

void work() {
    std::vector<int> ini;

    ini.push_back(hd);
    ini.push_back(ad);
    ini.push_back(hk);
    ini.push_back(ak);

    std::map<std::vector<int>, int> answer;

    std::vector<std::vector<int> > queue;
    answer[ini] = 0;
    queue.push_back(ini);
    for (int l = 0; l < (int)queue.size(); l++) {
        std::vector<int> u = queue[l];
        if (u[2] - u[1] <= 0) {
            std::cout << answer[u] + 1 << std::endl;
            return ;
        }
        std::vector<int> v;
        // attack
        v = u;
        v[2] -= v[1];
        v[0] -= v[3];
        if (v[0] > 0 && answer.count(v) == 0) {
            answer[v] = answer[u] + 1;
            queue.push_back(v);
        }
        // buff
        v = u;
        v[1] += buff;
        v[0] -= v[3];
        if (v[0] > 0 && answer.count(v) == 0) {
            answer[v] = answer[u] + 1;
            queue.push_back(v);
        }
        // cure
        v = u;
        v[0] = hd;
        v[0] -= v[3];
        if (v[0] > 0 && answer.count(v) == 0) {
            answer[v] = answer[u] + 1;
            queue.push_back(v);
        }
        // debuff
        v = u;
        v[3] = std::max(0, v[3] - debuff);
        v[0] -= v[3];
        if (v[0] > 0 && answer.count(v) == 0) {
            answer[v] = answer[u] + 1;
            queue.push_back(v);
        }
    }
    std::cout << "IMPOSSIBLE" << std::endl;
}

int main() {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int testCount;
    std::cin >> testCount;
    for (int i = 1; i <= testCount; i++) {
        printf("Case #%d: ", i);
        init();
        work();
    }

    return 0;
}
