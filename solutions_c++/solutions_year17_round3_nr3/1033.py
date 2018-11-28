#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>      // std::setprecision
#include < queue>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define endl '\n'

using dvojice = pair<long long int, long long int>;

int a, b, c, d, m, n, x, y;

vector< vector< int >>graf;
vector<int> navstiven;


int dijskra(int start, int cil, vector< vector<int> >& delkahrany) {
	int n = delkahrany.size();
	vector<int> delkacesty(n,-1);
	vector<bool> def(n,false);

	for (int i = 0; i < n; ++i) {
		delkacesty[i] = INT32_MAX;
	}
	delkacesty[start] = 0;

	for (int i = 0; i < n; ++i) {
		int aktualni = -1;
		for (int j = 0; j < n; ++j) {
			if (def[j]) continue;
			if (aktualni == -1 || delkacesty[j] < delkacesty[aktualni]) {
				aktualni = j;
			}
		}

		def[aktualni] = true;
		for (int j = 0; j < n; ++j) {
			if (delkahrany[aktualni][j] == -1) continue;
			int vzdalenost = delkacesty[aktualni] + delkahrany[aktualni][j];
			if (vzdalenost < delkacesty[j]) {
				delkacesty[j] = vzdalenost;
			}
		}
	}

	return delkacesty[cil];
}


int main() {
	std::ios::sync_with_stdio(false);

	int t, n, m;
	cin >> t >> n;
	for (int i = 1; i <= t; ++i) {
		vector<vector<int>> dylkahrany(n, vector<int>(n));
		vector<bool>def(n);
		vector<int>delkacesty(n, LONG_MAX);

		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
			{
				cin >> dylkahrany[j][k];
			}
		}

		cout << dijskra(0, n - 1, dylkahrany) << endl;
		


	}
	return 0;
}