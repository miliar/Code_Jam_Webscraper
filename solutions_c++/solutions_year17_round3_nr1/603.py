#include<bits/stdc++.h>
#define int long long
#define sqr(x) (x) * (x)
#define ld long double
 using namespace std;

 const int N = 1e5 + 121;
 pair<int,int> a[N];
 int i, n, k, t,kol;
 long double S,pi = 3.1415926535897932384626433832795,mx;
 ld b[N];
 int R,H;
 int tt;
 int j;
 bool cmp1(pair<int,int> a,pair<int,int> b){
    return(a.first > b.first || (a.first == b.first && a.second > b.second));
 }

 bool cmp2(pair<int,int> a,pair<int,int> b){
    return(a.second > b.second ||
           (a.second == b.second && a.first > b.first));
 }

 ld f(int r,int h){
    return (ld)(pi * 2 * r * h);
 }

 //int
  main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("output.txt","w",stdout);

    cin >> t;
    for(tt=1;tt<=t;++tt){
        cout << "Case #"<<tt<<": ";
        cin >> n >> k;
        for(i = 1; i <= n; ++i) cin >> a[i].first >> a[i].second;
        mx = 0;
        for(i = 1; i <= n; ++i){
        S = sqr(a[i].first) * pi + f(a[i].first,a[i].second);
        kol = 0;
        for(j = 1; j <= n; ++j)
            if(i!=j && a[j].first <= a[i].first)
                b[++kol] = f(a[j].first,a[j].second);
            sort(b+1,b+kol+1);
            reverse(b+1,b+kol+1);
            for(j = 1; j < min(kol+1,k); ++j)
                S += b[j];
            if(S > mx) mx = S;
        }

        cout << setprecision(5) << fixed << mx << '\n';
    }

 }
