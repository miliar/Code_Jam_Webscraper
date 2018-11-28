#include<bits/stdc++.h>
#define int long long
 using namespace std;

 int t,d,n,i,k,s;
  double mx;

 //int
  main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("output.txt","w",stdout);
    freopen("A-large (1).in","r",stdin);

    int tt;
    cin >> tt;
    for(t=1;t<=tt;++t){
        cin >> d >> n;
        mx = 0;
        for(i =  1; i <= n; ++i){
            cin >> k >> s;
            mx = max(mx, (d - k) /(1.0 * s));
        }

        cout << "Case #"<<t<<": "<<setprecision(10)<<fixed<<d / mx << endl;

    }

  }
