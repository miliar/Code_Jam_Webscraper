#include <bits/stdc++.h>

using namespace std;



int main() {
  freopen("inp.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int T;
  cout << fixed << setprecision(20);
  cin >> T;
  for(int t = 1 ; t <= T ; t ++){
    cout << "Case #"<<t<<": ";

    double ans = 1e15;
    int n;
    double d;
    cin >> d >> n;
    for(int i = 0 ; i < n ; i ++){
        double x,y;
        cin >> x >> y;
        ans = min(ans, d*y/(d-x));
    }
    cout << ans;
    cout << endl;
  }
  return 0;
}
