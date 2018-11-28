#include <iostream>
#include <bits/stdc++.h>
#define EPS 1e-15
using namespace std;

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        long long d,n;
        cin >>d >> n;
        long long x,s;
        vector<pair<long,long>> v;
        for(int j=0;j<n;j++){
            cin >> x >> s;
            v.push_back(make_pair(x,s));
        }
        std::sort(v.begin(),v.end());
        long double tim = (d - v[n-1].first)/(v[n-1].second*1.);
        for(int j=n-2;j>=0;j--){
            long double limit = ((v[j].first - v[j+1].first)*1.)/((v[j+1].second - v[j].second)*1.);
            if(fabs(limit)<EPS){
                tim = (d-v[j].first)/(1.*min(v[j].second,v[j+1].second));
            }
            if(limit < EPS || limit > tim){
                tim = (d-v[j].first)/(1.*v[j].second);
            }
            else{
                tim = tim;
            }
        }
        cout << "Case #" << i << ": ";
        printf("%.9lf\n",(d*1./tim));
//        if(i==85){
//                cout << d << " " << n << endl;
//                for(int j=0;j<n;j++){
//                    cout << v[j].first << " " << v[j].second << endl;
//
//                }
//                return 0;
//        }
    }
    return 0;
}
