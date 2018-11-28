
/*****************************************
Author: lizi
Email: lzy960601@outlook.com
****************************************/
  
#include<bits/stdc++.h>
  
using namespace std;
  
const double eps=1e-10;
const double pi=3.1415926535897932384626433832795;
const double eln=2.718281828459045235360287471352;
  
#define LL long long
#define IN freopen("ba.in", "r", stdin)
#define OUT freopen("ba.out", "w", stdout)
#define scan(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define sqr(x) (x) * (x)
#define pr(x) printf("Case %d: ",x)
#define prn(x) printf("Case %d:\n",x)
#define prr(x) printf("Case #%d: ",x)
#define prrn(x) printf("Case #%d:\n",x)
#define lowbit(x) (x&(-x))
  
string a[30];

int main() {
    IN;OUT;
  int T;
  scanf("%d",&T);
  for (int _ = 1; _ <= T; _++) {
    int n, m;
    scanf("%d%d",&n,&m);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
      for (int j = 0; j < m; j++) {
        if (a[i][j] != '?') {
          for (int k = j - 1; k >= 0;k--) {
            if(a[i][k]!='?')break;
            a[i][k] = a[i][j];
          }
          for (int k = j + 1; k < m; k++) {
              if(a[i][k]!='?')break;
            a[i][k] = a[i][j];
          }
        }
      }
    }
    for (int i = 0; i < n; i++) {
      if (a[i][0] != '?') {
        for (int j = i - 1; j >= 0; j--) {
            if(a[j][0]!='?')break;
          a[j] = a[i];
        }
        for (int j = i + 1; j < n; j++) {
            if(a[j][0]!='?')break;
          a[j] = a[i];
        }
      }
    }
    prrn(_);
    for(int i=0;i<n;i++)cout<<a[i]<<endl;
  }
  return 0;
}
