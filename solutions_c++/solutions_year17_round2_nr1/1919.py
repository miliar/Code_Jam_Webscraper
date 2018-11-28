#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
typedef long long ll;

void solve(){
  double d;
  int n;
  double M = 0;
  cin >> d >> n;
  for(int i = 0;i < n;++i){
    double k, s;
    cin >> k >> s;
    M = max(M, (d - k)/s);
  }
  cout << setprecision(15) << d/M << endl;
}


int main(void){
  int t;
  cin >> t;
  for(int i = 0;i < t;++i){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
