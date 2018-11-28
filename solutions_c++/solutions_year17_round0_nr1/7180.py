#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <map>
#include <valarray>
#include <sstream>
#include <set>
#include <fstream>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

void trimp(string &res) {
	int from = 0;
	int to = res.length() - 1;
	for (; from < res.length() && res[from] == '+'; from++);
	for (; to > from && res[to] == '+'; to--);
	res = res.substr(from, to - from + 1);
}

bool flip(string &in, int n) {
	if (in.length() < n)
		return false;
	for (int i = 0; i < n; i++) {
		if (in[i] == '+')
			in[i] = '-';
		else
			in[i] = '+';
	}
	return true;
}

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif	

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		string x;
		int s;
		cin >> x >> s;
		int cnt = 0;
		trimp(x);
		while (flip(x, s)) {
			trimp(x);
			cnt++;
		}
		cout << "Case #" << i + 1 << ": ";
		if (x.length() == 0)
			cout << cnt << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}