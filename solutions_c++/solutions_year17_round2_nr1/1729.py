#include<bits/stdc++.h>
#define MX 100005
using namespace std;
typedef long long ll;

int main(){
     freopen("input1.txt", "r", stdin);
     freopen("output1.txt", "w", stdout);
     int i, j, k;
     int t, T, n;
     double s, v, d, mx;
     scanf("%d", &T);
     for(t=1; t<=T; ++t){
          cin >> d >> n;
          mx=0.0000000001;
          for(i=0; i<n; ++i){
               cin >> s >> v;
               mx=max(mx, (d-s)/v);
          }
          cout << "Case #" << t << ": ";
          cout << setprecision(8) << fixed << d/mx << endl;
     }
     return 0;
}
