#include <iostream>
#include <iomanip>

using namespace std;

struct Case {
  int t, i;
  Case() : i(0) { cin >> t; }
  bool next() { return i++ < t; }
} T;
ostream& operator<<(ostream& o, const Case &i) { o<<"Case #"<<i.i<<": "; return o; }

const int N=100+5;
int main() {
  cout<<fixed<<setprecision(10);
while (T.next()) {
  cout<<T;
  int n, q;
  cin>>n>>q;
  //q==1
  int e[N], s[N];
  int m[N][N];
  long long d[N][N];
  long double f[N][N];
  for (int i= 0; i<n;i++)
    cin>>e[i]>>s[i];
  for (int i=0;i<n;i++) {
    for (int j=0;j<n;j++) {
      cin>>m[i][j];
      f[i][j]=-1;
    }
    d[i][i]=0;
    f[i][i]=0;
    d[i][i+1] = m[i][i+1];
    f[i][i+1] = (long double)d[i][i+1]/s[i];
  }
  for (int l = 2; l<n; l++) {
    for (int i=0; i+l<n; i++){
      d[i][i+l] = d[i][i+1]+d[i+1][i+l];
      if (e[i] >= d[i][i+l])
        f[i][i+l] = (long double)d[i][i+l]/s[i];
      for (int k=1;k<l;k++) {
        if (f[i][i+l]<0 || f[i][i+l]>f[i][i+k]+f[i+k][i+l])
          f[i][i+l] = f[i][i+k]+f[i+k][i+l];
      }
      // cerr<<f[i][i+l]<<' ';
    }
    // cerr<<endl;
  }
  for (int qq=0; qq<q; qq++) {
    int uk, vk;
    cin>>uk>>vk;
    uk--,vk--;//0, n-1
    // cerr<<uk<<vk<<endl;
    cout<<f[uk][vk];
    if (qq!=q-1) cout<<" ";
  }
  cout<<endl;
}
}
