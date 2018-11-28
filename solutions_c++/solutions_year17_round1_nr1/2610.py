#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <utility>
#include <string.h>
#define _USE_MATH_DEFINES
#include <cmath>
#include <cctype>
#include <fstream>

using namespace std;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define MP make_pair
#define PB push_back
#define EPS 0.0000001
#define ALL(a) a.begin(), a.end()
#define Abs(a) ((a) > 0 ? (a) : -(a))

const int INF = 1000 * 1000 * 1000;
const int MOD = 1000 * 1000 * 1000 + 7;
const lint INF_L = 1000 * 1000 * 1000;
const ll INF_LL = 1LL * INF_L * INF_L;
const ll MOD_LL = 1000000000007LL;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

ll pow(ll n, ll a, ll mod) {
    ll res = 1;
    while (a) {
        if (a & 1) res = (res * n) % mod;
        n = (n * n) % mod;
        a >>= 1;
    }
    return res;
}

ll gcd(ll a, ll b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

ll lcm(ll a, ll b) {
    return (a / gcd(a, b)) * b;
}

const int N = 200*1000 + 10;
const int M = 4000;

vector<char> vectToLower(vector<char> v) {
	for (int i = 0; i < v.size(); ++i) {
		v[i] = (char) tolower(v[i]);
	}
	return v;
}

void expand(vector<char> &v) {
	for (int i = 0; i < v.size(); ++i) {
		if (v[i] != '?' && islower(v[i])) {
			v[i] = (char) toupper(v[i]);
			for (int i1 = i - 1; i1 >= 0 && v[i1] == '?'; --i1) {
				v[i1] = v[i];
			}
			for (int i1 = i + 1; i1 < v.size() && v[i1] == '?'; ++i1) {
				v[i1] = v[i];
			}
		}
	}
}

void rebuild(vector<char> &line, const vector<char> v) {
	for (int i = 0; i < v.size(); ++i) {
		if (v[i] != '?') {
			char ch = line[i];
			for (int i1 = 0; i1 < line.size(); ++i1) {
				if (line[i1] == ch) {
					line[i1] = '?';
				}
			}
			line[i] = (char) tolower(v[i]);
		}
	}
	
	expand(line);
}

//#define ONLINE_JUDGE
int main() {
	//ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
    freopen("../A-large.in", "r", stdin);
    freopen("../out.txt", "w", stdout);
#endif
	
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int rows, cols;
		cin >> rows >> cols;
		vector<vector<char>> matr(rows, vector<char>(cols));
		int startRow = -1;
		for (int i = 0; i < rows; ++i) {
			for (int j = 0; j < cols; ++j) {
				cin >> matr[i][j];
				if (matr[i][j] != '?') {
					startRow = i;
				}
			}
		}
		
		vector<char> line = vectToLower(matr[startRow]);
		expand(line);
		matr[startRow] = line;
		for (int r = startRow + 1; r < rows; ++r) {
			rebuild(line, matr[r]);
			matr[r] = line;
		}
		
		line = matr[startRow];
		for (int r = startRow - 1; r >= 0; --r) {
			rebuild(line, matr[r]);
			matr[r] = line;
		}
		
		cout << "Case #" << t+1 << ":\n";
		for (int i = 0; i < rows; ++i) {
			for (int j = 0; j < cols; ++j) {
				cout << matr[i][j];
			}
			cout << endl;
		}
	}
	
    return 0;
}