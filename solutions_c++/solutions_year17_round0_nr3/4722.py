#include<iostream>
#include<set>
using namespace std;

#define sz(X) (int)X.size()

int main() {
  int t;
  cin >> t;
  for(int c=1;c<=t;++c) {
    int n, k;
    cin >> n >> k;
    multiset<int, std::greater<int> > s;
    s.insert(n);
    int r1=0, r2=0;
    while(k--) {
      int m = *s.begin() -1;
      s.erase(s.begin());
      r1 = (m+1)/2;
      r2 = m/2;
      s.insert(r1);
      s.insert(r2);
    }
    cout << "Case #" << c << ": " << r1 << " " << r2 << endl;
  }
  return 0;
}
