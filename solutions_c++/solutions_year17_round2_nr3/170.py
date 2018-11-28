#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream cin("C.in");
    ofstream cout("C.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        
        int n, q; cin >> n >> q;
        
        vector<int> e(n, 0), s(n, 0);

        for(int i = 0; i < n; ++i)
            cin >> e[i] >> s[i];
            
        vector<vector<long long>> d(n, vector<long long> (n, 0));

        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j) {
                cin >> d[i][j];
                if(d[i][j] == -1)
                    d[i][j] = 1e15;
                if(i == j)
                    d[i][j] = 0;
            }
        
        for(int k = 0; k < n; ++k)
            for(int i = 0; i < n; ++i)
                for(int j = 0; j < n; ++j)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

        vector<vector<double>> time(n, vector<double> (n, 1e16));
        
        for(int i = 0; i < n; ++i)
            time[i][i] = 0;
        
        vector<int> p(n, 0);

        for(int i = 0; i < n; ++i)
            p[i] = i;
        
        
        for(int it = 0; it < 3 * n; ++it)
            for(int k = 0; k < n; ++k)
                for(int i = 0; i < n; ++i)
                    for(int j = 0; j < n; ++j)
                        if(d[p[k]][j] <= e[p[k]])
                            time[i][j] = min(time[i][j], time[i][p[k]] + (d[p[k]][j] + 0.0) / s[p[k]]);
        

        cout.precision(10);
        
        for(int i = 0; i < q; ++i) {
            int u, v; cin >> u >> v;
            u--, v--;
            /*
            vector<double> ans(n, 1e16);
            ans[u] = 0;
            vector<int> del(n, 0);

            for(int it = 0; it < n; ++it) {
                int who = -1;
                double dist = 1e16;
                for(int j = 0; j < n; ++j)
                    if(not del[j] and ans[j] < dist) {
                        dist = ans[j];
                        who = j;
                    }
                
                assert(who != -1);

                for(int j = 0; j < n; ++j)
                    if(not del[j] and d[who][j] <= e[who])
                        ans[j] = min(ans[j], ans[who] + (d[who][j] + 0.0) / s[who]);

                del[who] = 1;
            } */  
            
            //cout << ans[v] << " ";
            cout << time[u][v] << " ";
        }
        
        cout << "\n";

        cerr << "\n";
        cerr << t_case << "\n";
    }
}
