#include<bits/stdc++.h>
#define MX 100005
using namespace std;
typedef long long ll;

double ara[105];

int main(){
     freopen("in3.txt", "r", stdin);
     freopen("out3.txt", "w", stdout);
     int i, j, k;
     int t, T, n;
     double v, ans;
     scanf("%d", &T);
     for(t=1; t<=T; ++t){
          scanf("%d %d", &n, &k);
          cin >> v;
          for(i=0; i<n; ++i) cin >> ara[i];
          while(v>0.00001){
               sort(ara, ara+n);
               ara[0]+=0.0001;
               v-=0.0001;
          }
          ans=1;
          for(i=0; i<n; ++i) ans*=ara[i];
          printf("Case #%d: %0.8lf\n", t, ans);
     }
     return 0;
}
