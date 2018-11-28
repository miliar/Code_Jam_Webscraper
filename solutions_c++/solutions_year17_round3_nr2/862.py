#include<bits/stdc++.h>

using namespace std;

#define int long long
#define f first
#define s second

int32_t main(){
    ios_base::sync_with_stdio(0);
    ios_base::sync_with_stdio(0);
    ifstream fin("b.in");
    ofstream fout("ansb.txt");
    #define cin fin
    #define cout fout
    int t;
    cin >> t;
    for(int z = 0; z < t; ++z){
        int n, m;
        cin >> n >> m;
        vector<pair<pair<int, int>, int>> v(n + m);
        int p = 0, sum1 = 0, sum2 = 0;
        for(int i = 0; i < n; ++i){
            cin >> v[i].f.f >> v[i].f.s;
            sum1 += v[i].f.s - v[i].f.f;
            v[i].s = 1;
        }
        for(int i = 0; i < m; ++i){
            cin >> v[i].f.f >> v[i].f.s;
            sum2 += v[i].f.s - v[i].f.f;
            v[i].s = 2;
        }
        sort(v.begin(), v.end());
        vector<int> v1;
        vector<int> v2;
        for(int i = 0; i < n + m - 1; ++i){
            if(v[i].s != v[i+1].s){
                ++p;
            }
            else if(v[i].s == 1){
                v1.push_back(v[i+1].f.f - v[i].f.s);
            }
            else if(v[i].s == 2){
                v2.push_back(v[i+1].f.f - v[i].f.s);
            }
        }
        if(v[0].s != v.back().s){
            ++p;
        }
        else{
            if(v[0].s == 1){
                v1.push_back(1440 - v.back().f.s + v[0].f.f);
            }
            if(v[0].s == 2){
                v2.push_back(1440 - v.back().f.s + v[0].f.f);
            }
        }
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        int i = 0;
        while(i < v1.size() && sum1 + v1[i] <= 720){
            sum1 += v1[i];
            ++i;
        }
        int j = 0;
        while(j < v2.size() && sum2 + v2[j] <= 720){
            sum2 += v2[j];
            ++j;
        }
        cout << "Case #" << z+1 << ": ";
        cout << p + 2 * max(v1.size() - i, v2.size() - j) << endl;
    }
}
