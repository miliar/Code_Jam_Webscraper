#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define FO(i, a, b) for (int i=(a); i<(b); i++)
#define FOR(i, n) FO(i, 0, n)

int N, R, aB, Y, aR, B, aY;
const int r = 0, y = 1, b = 2;

bool seen[3];
char trans[7] = "RYBGVO";
int acnt[3];

vector <int> walk(vector <int> what)
{
	vector <int> res;
	for (int z: what){
		if (!seen[z]){
			FOR(i, acnt[z])
				res.push_back(z), res.push_back(3 + z);

			seen[z] = true;
		}

		res.push_back(z);
	}
	return res;
}

string solve(void)
{
	cin >> N >> R >> aB >> Y >> aR >> B >> aY;
	R -= aR;
	Y -= aY;
	B -= aB;
	int cnt[3] = {R, Y, B};
	acnt[0] = aR, acnt[1] = aY, acnt[2] = aB;
	vector <int> s = {};
	for (int i=2; i>=0; i--){
		if (cnt[i] > 0){
			s.push_back(i);
			cnt[i]--;
			break;
		}
	}

	while (cnt[0] > 0 || cnt[1] > 0 || cnt[2] > 0){
		int prev = s.back();
		pair <int, int> m = {-1, -1};
		FOR(i, 3)
			if (i != prev)
				m = max(m, {cnt[i], i});

		if (m.first <= 0)
			return "IMPOSSIBLE";

		int i = m.second;
		cnt[i]--;
		s.push_back(i);
	}

	if (cnt[0] < 0 || cnt[1] < 0 || cnt[2] < 0)
		return "IMPOSSIBLE";

	seen[0] = seen[1] = seen[2] = false;
	vector <int> res = walk(s);
	FOR(i, 3){
		vector <int> a = walk({i});
		a.pop_back();
		for (auto b: a)
			res.push_back(b);
	}

	if (res.size() != N)
		return "IMPOSSIBLE";

	string t;
	FOR(i, N){
		int a = res[i], b = res[(i + 1) % N];
		if (a == b || (a > 2 && b != a - 3) || (b > 2 && a != b - 3))
			return "IMPOSSIBLE";
		t.push_back(trans[a]);
	}

	return t;
}

int main(void)
{
	int t;
	ios::sync_with_stdio(false);
	cin >> t;
	FOR(i, t){
		cout << "Case #" << i + 1 << ": " << solve() << '\n';
	}
}
