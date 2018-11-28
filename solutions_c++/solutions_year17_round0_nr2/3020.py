#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <unordered_map>
#include <set>
#include <stack>
#include <bitset>
#include <queue>
#include <numeric>
#include <map>
#include <list>
#include <errno.h>
#include <algorithm>
#include <memory>

#include <iterator>
#include <assert.h>
#include <unordered_set>
#include <sstream>

#define pb push_back
#define mp make_pair

//#define x first
//#define y second

using big = long long;

using namespace std;

string solve() {
	string a;
	cin >> a;
	int i;
	for (i = 1; i < a.size(); ++i) {
		if (a[i - 1] > a[i]) {
			break;
		}
	}
	if (i == a.size()) {
		return a;
	}
	--i;
	for (; i - 1 >= 0 && a[i - 1] == a[i]; --i);
	--a[i];
	for (++i; i < a.size(); ++i) {
		a[i] = '9';
	}
	if (a[0] == '0' && a.size() > 1) {
		a.erase(a.begin());
	}
	return a;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		cout << solve() << endl;
	}
	fclose(stdin);
	fclose(stdout);
}

