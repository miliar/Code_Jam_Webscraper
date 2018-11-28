#include<bits/stdc++.h>
#define int long long
#define ld long double
 using namespace std;

 const int N = 2000;
 int t,tt,i,n,k;
 ld l,r,mid,eps=1e-8,ans,a[N],u;

 bool f(ld x){
     ld sum = 0;
     for(int i = 1; i <= n; ++i){
        sum += max((ld)0.0,x - a[i]);
        if(sum > u + eps) return 0;
     }
     return 1;
 }

 void up(ld x){
        for(int i = 1; i <= n; ++i){
        a[i] = max(a[i],x);
     }

 }
  main(){

    cin >> t;
    for(tt = 1;tt <= t; ++tt){
        cout << "Case #"<<tt<<": ";
        cin >> n >> k;
        cin >> u;
        for(i = 1; i <= n; ++i) cin >> a[i];

        l = 0;
        r = 1.0;
        while(l+eps<r){
            mid=(l+r)/2;
            if(f(mid))l=mid;else r=mid;
        }
        up(mid);
        ans = 1;
        for(i = 1;i <= n; ++i) ans = ans * a[i];
        cout << setprecision(9) << fixed << min((ld)1.0,ans) << '\n';
    }

 }
