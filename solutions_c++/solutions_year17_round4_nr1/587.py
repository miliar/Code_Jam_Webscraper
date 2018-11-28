#include <bits/stdc++.h>
using namespace std;

map<vector<int>, int> mem;
int P;

int ret(vector<int> state) {
    if(mem.find(state) != mem.end())
        return mem[state];

    int &ans = mem[state];
    ans = 0;
    
    int total = 0;

    for(int i = 0; i < P; ++i)
        total += state[i];

    if(total == 0) {
        return ans = 0;
    }
    
    int cost = 0;
    if(state[P] == 0)
        cost = 1;

    for(int i = 0; i < P; ++i) {
        if(state[i] == 0)
            continue;
        vector<int> temp = state;
        temp[i]--;
        temp[P] = (temp[P] + i) % P;
        ans = max(ans, cost + ret(temp));
    }

    return ans;
}

int main() {
    ifstream cin("A.in");
    ofstream cout("A.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        cerr << t_case << "\n";

        int n, p; cin >> n >> p;
        P = p;

        vector<int> state(p + 1, 0);
        mem.clear();

        for(int i = 0; i < n; ++i) {
            int x; cin >> x;
            state[x % p]++;
        }

        cout << ret(state) << "\n";
    }
}
