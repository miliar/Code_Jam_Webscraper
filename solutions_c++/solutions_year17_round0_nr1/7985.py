#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <functional>
#include <iterator>
#include <map>
#include <numeric>
#include <cstring>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <cctype>
#include <math.h>
#include <cstdlib>

using namespace std;

#define I64 long long int
#define INF 0x7f7f7f7f

#define PII pair <int, int>
#define PLL pair <I64, I64>
#define PDD pair <double, double>
#define PSI pair <string, int>
#define PIS pair <int, string>
#define PSS pair <string, string>

#define MII map <int, int>
#define MLL map <I64, I64>
#define MDD map <double, double>
#define MSI map <string, int>
#define MIS map <int, string>
#define MSS map <string, string>

#define VI vector <int>
#define VS vector <string>
#define QI queue <int>
#define QS queue <string>
#define SI stack <int>
#define SS stack <string>

#define pb push_back
#define pob pop_back
#define mp make_pair

#define IT iterator
#define ff first
#define ss second

#define SET(a, b) memset( a, b, sizeof (a) )
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define IAMHERE cout << "YES\n";
#define DEBUG(a, b) cout << a << ": " << b << "\n";

#define SIZE 1000
#define MAX 2000
#define EPS 1e-9
#define PI (2*acos(0.0))

int minStep(string &s, int k)
{
	int cnt = 0;

	for (int i = 0; i <= s.size() - k; i++) {
		if (s[i] == '-') {
			for (int j = i, counter = 1; counter <= k; counter++, j++) {
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
			}
			cnt++;
		}
	}

	return cnt;
}

bool isAllHappy(const string &s)
{
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') return false;
	}
	return true;
}

int main()
{
    READ("A-large.in");
    WRITE("out.txt");
    int Case=1;
    int n, m, k;
    string s, rs;
    char dump[2];

    int tc; scanf("%d", &tc);

    while (tc--) {
    	cin >> s >> k;

    	rs = s;
    	reverse(rs.begin(), rs.end());

    	int cntlr = minStep(s, k);
    	int cntrl = minStep(rs, k);
    	int ans;

    	if (!isAllHappy(s)) {
    		cntlr = INF;
    	}
    	if (!isAllHappy(rs)) {
    		cntrl = INF;
		}

    	ans = min(cntlr, cntrl);

    	if (ans == INF) {
    		printf("Case #%d: IMPOSSIBLE\n", Case++);
    	}
    	else {
    		printf("Case #%d: %d\n", Case++, ans);
    	}
    }
    return 0;
}
