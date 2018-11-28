#include<bits/stdc++.h>

using namespace std;

#define f first
#define s second
#define int long long

int32_t main(){
    ios_base::sync_with_stdio(0);
    ifstream fin("c.in");
    ofstream fout("outputC.txt");
    #define cin fin
    #define cout fout
    int t;
    cin >> t;
    for(int z = 0; z < t; ++z){
        int n, q;
        cin >> n >> q;
        vector<pair<int, double>> vp(n);
        vector<vector<int>> v(n, vector<int>(n));
        vector<int> l(n);
        for(int i = 0; i < n; ++i){
            cin >> vp[i].f >> vp[i].s;
        }
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                cin >> v[i][j];
                if(i + 1 == j){
                    l[i] = v[i][j];
                }
            }
        }
        int u, vv;
        cin >> u >> vv;
        vector<double> ans(n, 1e18);
        ans[n-1] = 0;
        for(int i = n-2; i >= 0; --i){
            int sum = 0;
            for(int p = i; p < n-1; ++p){
                sum += l[p];
                if(vp[i].f >= sum){
                    ans[i] = min(ans[i], sum/vp[i].s + ans[p+1]);
                }
            }
        }
        cout << "Case #" << z+1 << ": ";
        cout << fixed << setprecision(7) << ans[0] << endl;
//        for(int i = 0; i < ans.size(); ++i){
//            cout << ans[i] << ' ';
//        }
//        cout << endl << endl;
    }
}
