#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <cassert>
 
using namespace std;

typedef long long ll;
#define mp make_pair
#define pub push_back
#define x first
#define y second
#define all(a) a.begin(), a.end()
#define y1 dsfgsdfgsdfgsdfgsdfgsdfg
#define y0 asdfasdf3rcdt234d5c23xd234dx43
const int INF = (int)1e9 + 7;
const ll LINF = (ll)4e18 + 7;
const double pi = acos(-1.0);
 
const ll p1 = 353251;
const ll p2 = 239017;
const ll mod = 1e9 + 7;
const ll mod1 = 1e9 + 7;
const ll mod2 = 1e9 + 9;
 
/*
const int MAX_MEM = 1e8;
int mpos = 0;
char mem[MAX_MEM];
void * operator new ( size_t n ) {
    char *res = mem + mpos;
    mpos += n;
    return (void *)res;
}
 
void operator delete ( void * ) { }
*/

int tt, k;
string s;

const bool is_testing = 1;
int main() { 
	srand('D' + 'E' + 'N' + 'I' + 'S' + 'S' + 'O' + 'N' + time(NULL));
	//mt19937 rnd(time(NULL));
	ios_base::sync_with_stdio(0); cin.tie(0);
	if (is_testing) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	} else {
		//freopen("beads.in", "r", stdin);
		//freopen("beads.out", "w", stdout);
	}
	cin >> tt;
	for (int v = 1; v <= tt; v++) {
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < (int)s.size() - k + 1; i++) {
			if (s[i] == '-') {
				ans++;
				for (int j = 0; j < k; j++) {
					if (s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
				}
			}
		}
		bool f = 0;
		cout << "Case #" << v << ": ";
		for (int i = 0; i < k; i++) if (s[(int)s.size() - i - 1] == '-') {
			cout << "IMPOSSIBLE" << "\n";
			f = 1;
			break;
		}
		if (!f) cout << ans << "\n";
	}
}