#include <bits/stdc++.h>
#define ll long long
#define ss second
#define ff first
using namespace std;


int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for(int z = 1; z <= t; ++z)
    {
        double d;
        int n;
        cin >> d >> n;
        vector<pair<double, double> > h;
        for(int i = 0; i < n; ++i){
            double k, s;
            cin >> k >> s;
            h.push_back({k, s});
        }
        sort(h.begin(), h.end());
        vector<double> ti(n);
        vector<double> wi(n);
        for(int i = h.size()-1; i >= 0; --i){

            int f = false;
            for(int j = i+1; !f && j < h.size(); ++j)
            {
                if(h[i].ss > h[j].ss){
                    double difS = h[i].ss - h[j].ss;
                    double difD = h[j].ff - h[i].ff;
                    double time = difD / difS;
                    double where = time * h[i].ss + h[i].ff;
                    if(where <= ti[j]){
                        ti[i] = where;
                        f = true;
                        wi[i] = j;
                    }
                }
            }

            if(!f){
                ti[i] = d;
                wi[i] = -1;
            }

        }

        int st = 0;
        double wh = h[0].ff;
        double time = 0;
        while(st != -1){
            time += (ti[st] - wh) / h[st].ss;
            wh = ti[st];
            st = wi[st];
        }

        double ans = d / time;
        printf("Case #%d: %.6lf\n", z , ans);
    }
}
