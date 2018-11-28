#include<iostream>
#include<cstdio>
#include<map>
using namespace std;

typedef long long LL;
typedef map<LL, LL> mii;

int main() {
  int cases;
  cin >> cases;
  for (int cas = 1; cas <= cases; cas++) {
    printf("Case #%d: ", cas);
    
    LL n, k;
    cin >> n >> k;;
    mii m;
    m[n] = 1;
    while (k > 0) {
      mii::reverse_iterator it = m.rbegin();
      LL n = it->first;
      LL count = it->second;
      m.erase(n);

      n--;
      LL n2 = n / 2;
      LL n1 = n - n2;

      m[n1] += count;
      m[n2] += count;
      k -= count;
      if (k <= 0) {
	cout << n1 << ' ' << n2 << endl;
	break;
      }
    }
  }
  return 0;
}
