#include<bits/stdc++.h>

using namespace std;

#define int long long
#define f first
#define s second
#define double long double

int32_t main(){
    ios_base::sync_with_stdio(0);
    ifstream fin("c.in");
    ofstream fout("ansc.txt");
    #define cin fin
    #define cout fout
    int t;
    cin >> t;
    for(int z = 0; z < t; ++z){
        int n, k;
        double p;
        cin >> n >> k >> p;
        vector<double> v(n);
        for(int i = 0; i < n; ++i){
            cin >> v[i];
        }
        sort(v.begin(), v.end());
        double sum = v[0];
        for(int i = 1; i < n; ++i){
            if((sum + p) / i <= v[i]){
                for(int  j = 0; j < i; ++j){
                    v[j] = ((sum + p) / i);
                }
                p = 0;
                break;
            }
            sum += v[i];
        }
        if(p != 0){
            for(int i = 0; i < n; ++i){
                v[i] = ((sum + p)/n);
            }
        }
        double pr = 1;
        for(int i = 0; i < n; ++i){
            pr *= v[i];
        }
        cout << "Case #" << z+1 << ": ";
        #undef double
        cout << fixed << setprecision(7) << (double)(pr) << endl;
    }
}
