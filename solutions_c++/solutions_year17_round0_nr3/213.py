#include <bits/stdc++.h>
using namespace std;

map<int64_t, map<int64_t, int64_t>> mem;

map<int64_t, int64_t> getLengths(int64_t n) {
    if(mem.find(n) != mem.end())
        return mem[n];
    
    map<int64_t, int64_t> ans;
    if(n == 0)
        return mem[n] = ans;

    ans[n] = 1;

    int64_t lf = (n - 1) / 2;
    int64_t rt = (n - 1) - lf;

    auto a = getLengths(lf);
    auto b = getLengths(rt);

    for(const auto& elem : a) {
        ans[elem.first] += elem.second;
    }

    for(const auto& elem : b) {
        ans[elem.first] += elem.second;
    }

    return mem[n] = ans;
}

int main() {
    ifstream cin("C.in");
    ofstream cout("C.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";

        int64_t n, k; cin >> n >> k;

        map<int64_t, int64_t> M = getLengths(n);
        int64_t len = -1;

        for(auto it = M.rbegin(); it != M.rend(); ++it) {
            if((*it).second < k) {
                k -= (*it).second;
            } else {
                len = (*it).first;
                break;
            }
        }
        
        assert(len >= 0);

        int64_t lf = (len - 1) / 2;
        int64_t rt = (len - 1) - lf;

        if(rt > lf)
            swap(rt, lf);

        cout << lf << " " << rt << "\n";
    }
}
