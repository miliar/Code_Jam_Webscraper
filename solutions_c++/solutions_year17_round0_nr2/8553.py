#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

// #ifdef ONLINE_JUDGE
// #define freopen if(0)freopen
// #else
// #define cerr if(0)cerr
// #endif

#define fe first
#define se second
#define pb push_back
#define mp make_pair
#define FILENAME ""
#define inf 2000000000
#define mod 1000000007
#define ll long long
using namespace std;

long long solve(long long n) {
  vector<int> v;
  while (n) v.push_back(n % 10), n /= 10;
  for (int i = 0; i < v.size() - 1; i++) {
    if (v[i] < v[i + 1]) {
      v[i + 1]--;
      for (int j = 0; j <= i; j++) v[j] = 9;
    }
  }
  long long result = 0;
  int i = v.size() - 1;
  while (!v[i]) i--;
  while (i >= 0) result = result * 10ll + v[i], i--;
  return result;
}

int main() {
  // freopen(".in","r",stdin);
  // freopen("output.txt","w",stdout);
  int T;
  long long N;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    cin >> N;
    cout << "Case #" << i << ": " << solve(N) << endl;
  }

  return 0;
}













//
