#include <bits/stdc++.h>

using namespace std;

long long p10[20], n;
vector <int> res;
bool vis[50][20][2];

int getDigit(long long a, int pos) {
	return (a / p10[pos] % 10);
}

bool brute(int pos, int base, int ok) {
	//cout << pos << " " << base << " " << ok << endl;
	if (pos == -1)
		return 1;
	if (vis[pos][base][ok])
		return 0;
	vis[pos][base][ok] = 1;
	int roof = 9, d = getDigit(n, pos);
	if (ok == 0)
		roof = d;
	//cout << roof <<  " " << d << endl;
	for(int j = roof; j >= base; j--) {
		bool valid = brute(pos - 1, j, ok | (j < d));
		if (valid) {
			res.push_back(j);
			return 1;
		}
	}
	return 0;
}

int main() {
	int _T;
	cin >> _T;
	p10[0] = 1;
	for(int i=1; i<=18; i++)
		p10[i] = p10[i - 1] * 10;
	for(int _t = 1; _t <= _T; _t++) {
		cout << "Case #" << _t << ": ";
		cin >> n;
		memset(vis, 0, sizeof(vis));
		res.clear();
		brute(18, 0, 0);
		while (res.size() > 1 && res.back() == 0)
			res.pop_back();
		while (res.size() > 0) {
			cout << res.back();
			res.pop_back();
		}
		cout << "\n";
	}
	return 0;
}