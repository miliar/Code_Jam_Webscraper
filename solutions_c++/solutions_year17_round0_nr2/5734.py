#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <ctime>


typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
using namespace std;

int main() {
	FILE *stream;
	//freopen_s(&stream, "B-small.in", "r", stdin);
	//freopen_s(&stream, "B-small.out", "w", stdout);
	freopen_s(&stream, "B-large.in", "r", stdin);
	freopen_s(&stream, "B-large.out", "w", stdout);
	int T;
	string str;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> str;
		cout << "Case #" << (i + 1) << ": ";
		string res = "";
		int l = str.size();
		if (l == 1) res = str;
		for (int j = l - 1; j > 0; j--) {
			if (str[j] >= str[j - 1]) {
				res = str[j] + res;
			}
			else {
				for (int k = 0; k < res.size(); k++) res[k] = '9';
				res = res + '9';
				str[j - 1]--;
			}
		}

		if (l != 1) if (str[0] != '0') res = str[0] + res;
		cout << res << endl;
	}

	return 0;
}