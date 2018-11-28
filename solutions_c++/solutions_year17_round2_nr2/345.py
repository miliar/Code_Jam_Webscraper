#include <cinttypes>
#include <inttypes.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <set>
#include <stack>
#include <string.h>
#include <list>
#include <bitset>
#include <functional>

#define vi vector<int>
#define vvi vector<vi>
#define pii pair<int,int>
#define vpii vector<pii>
#define ll long long

#define all(s) s.begin(), s.end()

using namespace std;

int nxi() { int a; cin >> a; return a; }

vector<ll> a;
void inc(int i, ll v) {
	for (; i < a.size(); i |= i + 1) {
		a[i] = max(a[i], v);
	}
}

long long get(int r) {
	long long ans = 0;
	for (; r >= 0; r = (r & (r + 1)) - 1) {
		ans = max(ans, a[r]);
	}
	return ans;
}

long long get(int l, int r) {
	return get(r) - get(l - 1);
}


int gcd(int a, int b) { return a == 0 ? b : gcd(b % a, a); }

bool cmp(pii a, pii b) {
	return a > b;
}

int main() {

	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

int TCount = nxi();
for (int T = 1; T <= TCount; ++T) {

	int n, R, O, Y, G, B, V;
	cin >> n >> R >> O >> Y >> G >> B >> V;

	int l = max(max(R, Y), B);

	vpii ar;
	ar.push_back(pii(R, 'R'));
	ar.push_back(pii(Y, 'Y'));
	ar.push_back(pii(B, 'B'));

	printf("Case #%d: ", T);

	char prev = 0;
	if (l <= n / 2) {
		string res;

		for (int i = 0; i < n; ++i) {
			stable_sort(all(ar), cmp);
			

			for (int j = 0; j < 3; ++j) {
				if (prev == ar[j].second) continue;

				prev = ar[j].second;
				res += (char)ar[j].second;
				ar[j].first--;
				break;
			}
		}
		
		if (res[0] == res.back()) {
			int j = res.length() - 1;
			swap(res[j], res[j - 1]);
			j--;
			while (res[j] == res[j - 1])
			{
				j--;
				swap(res[j], res[j - 1]);
				j--;
			}
		}
		cout << res << endl;
	}
	else {
		cout << "IMPOSSIBLE\n";
	}
}

	return 0;
}

