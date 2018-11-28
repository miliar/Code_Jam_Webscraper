#include <iostream>
#include <iomanip>

using namespace std;

struct Case {
  int t, i;
  Case() : i(0) { cin >> t; }
  bool next() { return i++ < t; }
} T;
ostream& operator<<(ostream& o, const Case &i) { o<<"Case #"<<i.i<<": "; return o; }

int main() {
  cout<<fixed<<setprecision(10);
while (T.next()) {
  int n, d;
  cin>>d>>n;
  long double maxt = 0;
  for (int i = 0; i < n; i++) {
    int k, s;
    cin>>k>>s;
    long double t = d-k;
    t/=s;
    // cerr<<t<<" ";
    if (t > maxt) {
      maxt = t;
    }
  }
  // cerr<<endl;
  cout<<T<<d/maxt<<endl;
}
}
