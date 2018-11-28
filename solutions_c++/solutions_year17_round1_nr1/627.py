#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <iomanip>
#define MOD 1000000007
#define INF 999999999999999
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pl;
typedef vector<ll> vl;
typedef vector<pl > vpl;
typedef vector<vl > vvl;

void solve() {
	ll R, C; cin >> R >> C;
	char input[R][C];
	for(int i = 0; i < R; i++) {
		string to_put; cin >> to_put;
		for(int j = 0; j < C; j++) {
			input[i][j] = to_put[j];
		}
	}

	for(int j = 0; j < C; j++) {
		for(int i = 1; i < R; i++) {
			if(input[i][j] == '?' && input[i-1][j] != '?') {
				input[i][j] = input[i-1][j];
			}
		}
		for(int i = R-2; i >= 0; i--) {
			if(input[i][j] == '?' && input[i+1][j] != '?') {
				input[i][j] = input[i+1][j];
			}
		}
	}

	for(int i = 0; i < R; i++) {
		for(int j = 1; j <= C-1; j++) {
			if(input[i][j] == '?' && input[i][j-1] != '?') {
				input[i][j] = input[i][j-1];
			}
		}
		for(int j = C-2; j >= 0; j--) {
			if(input[i][j] == '?' && input[i][j+1] != '?') {
				input[i][j] = input[i][j+1];
			}
		}
	}
	cout << endl;
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			cout << input[i][j];
		}
		cout << endl;
	}
}

int main() {
	ios::sync_with_stdio(false);
	ll T; cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve(); 
	}
}
	