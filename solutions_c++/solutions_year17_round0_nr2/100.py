#include <iostream>
using namespace std;

typedef long long ll;

#define FOR(i,a,b) for(typeof(a) i=(a);i<(b);++i)
#define sz size()

void do_case(int te) {
  string a;
  cin >> a;
  FOR(i,1,a.sz) if(a[i] < a[i-1]) {
    int c = i-1;
    while(c > 0 && a[c] == a[c-1]) --c;
    a[c] = a[c]-1;
    FOR(j,c+1,a.sz) a[j] = '9';
    break;
  }
  if(a[0] == '0') a = a.substr(1);
  cout << "Case #" << te << ": " << a << endl;
}

int main() {
  int te, T=1;
  cin >> te;
  while(te--) {
    do_case(T);
    ++T;
  }
}