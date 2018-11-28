#include <bits/stdc++.h>
#define ll long long
#define ull unsigned ll

using namespace std;
#define MAXN 150001
#define files(x) freopen((x+string(".dat")).c_str(), "r", stdin); //freopen((x+string(".sol")).c_str(), "w", stdout);
#define int ll


#define MAXN 1000001
#define input_file(x) freopen((x+string(".txt")).c_str(), "r", stdin);
#define output_file(x) freopen((x+string(".txt")).c_str(), "w", stdout);




/*int next(int from, int cur, int base){
    return ((cur+2) * inv(from, base))%base;
}*/

bool shit[201000];
main () {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    input_file("input");
    output_file("output");
    int t;
    cin>>t;
    for (int test_id = 1;test_id<=t;test_id++){
            int n;
    double d;
        cin>>d>>n;
        pair<double, double> vals[n];
        double p[n+2], v[n+2];
        for (int i=0;i<n;i++){
            double x,y;
            cin>>x>>y;
            vals[i] = {x,y};
            //cin>>p[i]>>v[i];
        }
        sort(vals, vals + n);
        for (int i=0;i<n;i++){
                p[i] = vals[i].first;
                v[i] = vals[i].second;
        }
        double ps[n];



        for (int i=n-1;i>=0;i--){
            ps[i] = (d - p[i])/(v[i]);
            if (i<n-1)
                ps[i] = max(ps[i], ps[i+1]);
        }


        double res = d/ps[0];
        cout<<"Case #"<<test_id<<": ";
        cout<<fixed<<setprecision(9)<<res<<endl;


    }



}
