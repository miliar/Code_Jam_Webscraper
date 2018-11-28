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

void dec(char &c) {
	if (c == '0')
		c = '9';
	else
		c--;
}

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif	

	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		string x;
		cin >> x;
		for (int i = x.length() - 1; i > 0; i--) {
			if (x[i] < x[i - 1]) {
				dec(x[i-1]);
				for (int j = i; j < x.length(); j++) {
					x[j] = '9';
				}
			}
		}
		int from = 0;
		for (; from < x.length() && x[from] == '0'; from++);
		x = x.substr(from, x.length() - from + 1);
		cout << "Case #" << i + 1 << ": " << x << endl;
	}

	return 0;
}