#include <cstdio>
#include <cstring>
#include <cmath>
#include <cfloat>
#include <climits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <tuple>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long> vl;

#define ten(n) (1e##n)
#define COUT cout <<
#define SPACE_COUT << " "  <<
#define COMMA_COUT << ", " <<
#define ENDL << endl;

int
main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
      int k;
      string s;
      cin >> s >> k;

      int max_flip_num = s.size() - k + 1;
      int flip[1001];
      for (int j = 0; j < s.size(); ++j) {
	flip[j] = 0;
      }

      int total = 0;
      int consecutive_flip_num = 0;
      for (int j = 0; j < max_flip_num; j++) {
	if (j - k >= 0) {
	  consecutive_flip_num -= flip[j-k];
	}
	int dir = (s[j] == '-' ? 1 : 0) + consecutive_flip_num;
	if (dir % 2 == 0) continue;
	total++;
	flip[j] = 1;
	consecutive_flip_num++;
      }

      for (int j = max_flip_num; j < s.size(); j++) {
	if (j - k >= 0) {
	  consecutive_flip_num -= flip[j-k];
	}
	int dir = (s[j] == '-' ? 1 : 0) + consecutive_flip_num;
	if (dir % 2 == 0) continue;

	total = -1;
	break;
      }
      if (total == -1) {
	printf("Case #%d: IMPOSSIBLE\n", i);
      } else {
	printf("Case #%d: %d\n", i, total);
      }
    }
    return 0;
}
