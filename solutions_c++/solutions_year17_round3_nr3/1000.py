#include <bits/stdc++.h>

using namespace std;

int n1, n2, t, w = 1, ans, sum;

pair<pair<int, int> , int> g[200];

int sum[2];

int ff[1445];

bool comp(pair<pair<int, int> , int> a, pair<pair<int, int> , int> b){
    if(a.first.first < b.first.first) return 1;
    else return  0;
}

vector<vector<int> > tim(3);

int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    cin >> t;
    while(w <= t){
        for(int i = 0; i <= 1440; ++i){
            ff[i] = 1e+9;
        }
        ans = 0;
        cout << "Case #" << w << ": ";
        ++w;
        cin >> n1 >> n2;
        for(int i = 0; i < n1 + n2; ++i){
            scanf("%d %d", &g[i].first.first, &g[i].first.second);
            if(i >= n1) g[i].second = 1;
        }
        for(int i = 0; i < n1 + n2; ++i){
            for(int j = i + 1; j < n1 + n2; ++j){
                if(!comp(g[i], g[j])) swap(g[i], g[j]);
            }
        }
        tim[1].push_back(g[0].first.first);
        for(int i = 1; i < n1 + n2; ++i){
            if(g[i - 1].second == g[i].second) tim[2].push_back(g[i].first.first - g[i - 1].first.second);
            else tim[2].push_back(g[i].first.first - g[i - 1].first.second);
        }
        tim[1].push_back(1440 - g[n1 + n2 - 1].first.second);
        ff[sum] = 0;
        for()
    }
    return 0;
}