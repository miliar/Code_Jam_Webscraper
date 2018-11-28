#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>

using namespace std;

#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define fup(i, a, b) for (__typeof(a) i = (a); i != (b); ++i)
#define fdown(i, a, b) for (__typeof(a) i = (a); i != (b); --i)
#define all(x) (x).begin(),(x).end()
#define forall(i, x) fup(i, (x).begin(),(x).end())
#define debug(x) cout << #x << " = " << x << "\n"

typedef long long ll;


int main() {
  int t, c = 0;

  for (scanf("%d", &t); t--;) {
    string num;
    cin >> num;
    int sz = (int)num.size();
    num += '0';

    for (;;) {
      int i = 1;
      while (i < sz && num[i] >= num[i-1])
        ++i;
      if (i == sz) break;
      for (int j = i; j < sz; ++j) num[j] = '9';
      num[i-1]--;
    }

    int i = 0;
    while (num[i]=='0' && i < sz-1) ++i;

    printf("Case #%d: ", ++c);
    cout << num.substr(i,sz-i) << endl;
  }

  return 0;
}
