#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef pair<int,int> ii;

int p;
map<pair<ii,ii>, int> memo;

int func(vector<int> amt, int base) {
  pair<ii,ii> input = make_pair(ii(amt[1], amt[2]), ii(amt[3], base));
  if (memo.count(input))
    return memo[input];
  int ret=0;
  for (int i=1; i<p; ++i) {
    if (amt[i] != 0) {
      vector<int> newAmt=amt;
      newAmt[i]--;
      int c = func(newAmt, (base+i)%p) + (base==0?1:0);
      if (c>ret) ret=c;
    }
  }
  memo[input] = ret;
  return memo[input];
}

int main() {
  for (int i=0; i<500000000; ++i);
  int numTestCases;
  cin >> numTestCases;
  for (int curTestCase=1; curTestCase <= numTestCases; ++curTestCase) {
    cout << "Case #" << curTestCase << ": ";
    
    memo.clear();
    int n;
    cin >> n >> p;
    vector<int> g(n);
    for (int i=0; i<n; ++i)
      cin >> g[i];

    vector<int> amt(4, 0);
    for (int i=0; i<n; ++i)
      amt[g[i]%p]++;
    cout << func(amt, 0)+amt[0] << endl;
  }
}
