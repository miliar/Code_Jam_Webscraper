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

int tt;
ll n;
vector<int> q;

bool can(int val, int x) {
	for (int i = x; i < q.size(); i++) {
		if (q[i] < val) return 0;
		if (q[i] > val) return 1;
	}
	return 1;
}

const bool is_testing = 0;
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
		q.clear();
		cin >> n;
		while (n) {
			q.pub(n % 10);
			n /= 10;
		}
		reverse(all(q));
		cout << "Case #" << v << ": ";
		if (!can(1, 0)) {
			for (int i = 0; i < (int)q.size() - 1; i++) cout << 9;
		} else {
			for (int i = 0; i < q.size(); i++) {
				if (can(q[i], i)) {
					cout << q[i];
				} else {
					cout << q[i] - 1;
					for (int j = i + 1; j < q.size(); j++) cout << 9;
					break;
				}
			}
		}
		cout << "\n";
	}
}