#include<bits/stdc++.h>

using namespace std;

#define int long long
#define f first
#define s second
#define double long double
double pi = 3.14159265;

int32_t main(){
    ios_base::sync_with_stdio(0);
    ifstream fin("a2.in");
    ofstream fout("ansa2.txt");
    #define cin fin
    #define cout fout
    int t;
    cin >> t;
    for(int z = 0; z < t; ++z){
        int n, k;
        cin >> n >> k;
        vector<pair<int, int>> vp(n);
        for(int i = 0; i < n; ++i){
            cin >> vp[i].f >> vp[i].s;
        }
        sort(vp.begin(), vp.end());
        multiset<double> s;
        double ans = 0;
        double sum = 0;
        for(double i = 0; i < n; ++i){
            if(s.size() == k - 1){
                ans = max(ans, sum + pi*vp[i].f*vp[i].f + 2*pi*vp[i].f*vp[i].s);
            }
            s.insert(2*pi*vp[i].f*vp[i].s);
            sum += 2*pi*vp[i].f*vp[i].s;
            while(s.size() > k-1){
                sum -= *s.begin();
                s.erase(s.begin());
            }
        }
        cout << "Case #" << z+1 << ": ";
        #undef double
        cout << fixed << setprecision(7) << (double)ans << endl;
    }
}
