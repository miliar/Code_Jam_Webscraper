#include <bits/stdc++.h>
#define FOR(x,n) for(int x = 0; x < n; x++)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int)(a).size())
using namespace std;
typedef long long ll;

string num;
const int MXDIGITS = 30;
int m[MXDIGITS][10][2] = {};

int solve(int p, int mnDigit, bool smaller)
{
  if(p == SZ(num))
    return 0;

  if(m[p][mnDigit][smaller] != -1)
    return m[p][mnDigit][smaller];

  m[p][mnDigit][smaller] = -2;
  for(int i = mnDigit; i <= (smaller ? 9 : num[p]-'0'); i++)
    if(solve(p+1, i, smaller || (num[p]-'0' > i)) >= 0)
        m[p][mnDigit][smaller] = i;

  return m[p][mnDigit][smaller]; 
}

int main()
{
  int T; cin >> T;
  for(int cases = 1; cases <= T; cases++){
    memset(m,-1,sizeof(m));
    cin >> num;
    solve(0, 0, 0);
    cout << "Case #" << cases << ": ";
    int mnDigit = 0, started = 0, smaller = 0;
    for(int i = 0; i < SZ(num); i++){
      int d = m[i][mnDigit][smaller];
      smaller |= num[i] - '0' > d;
      mnDigit = d;
      if(!started && !d) continue;
      started = 1;
      cout << d;
    }
    cout << "\n";
  }
}
