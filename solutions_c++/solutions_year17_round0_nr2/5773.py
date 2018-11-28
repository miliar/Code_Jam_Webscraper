#include <stdio.h>
#include <math.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {
#ifndef WIN32
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif // !WIN32
	int tc;
	scanf("%d", &tc);
	int tc_o = tc;
	while (tc--) {
		char num[20];
		scanf("%s", &num);

		int i = 0, l = strlen(num);
		while (i < l && num[i] <= num[i + 1]) i++;
		while (i < l - 1 && i > 0 && num[i - 1] == num[i]) i--;
		if (i < l - 1) {
			num[i]--;
			for (int j = i + 1; j < l; j++) {
				num[j] = '9';
			}
		}
		int c = 0;
		while (num[c] == '0') c++;
		printf("Case #%d: %s\n", tc_o - tc, num + c);
	}
	return 0;
}