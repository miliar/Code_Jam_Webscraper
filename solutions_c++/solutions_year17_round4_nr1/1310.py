#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <math.h>
#include <cmath>
#include <queue>
#include <iomanip>
#include <bitset>
#include <memory.h>
#include <stack>
#pragma comment (linker, "/STACK:167177216")
#define ll long long
#define ull unsigned long long
#define INF 1000000007;
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define vI vector<int>
#define vvI vector<vector<int>>
#define vLL vector<LL>
#define vS vector<string>
#define fori(i, n) for(int (i)=0; (i)<n; (i)++)
#define forn(it,from,to) for(int (it)=from; (it)<to; (it)++)
#define forI(tmp) for(auto(it)=(tmp).begin();(it)!=(tmp).end();(it)++)
#define PI 3.14159265356
#define LD long double
#define sc(a) scanf("%d", &(a))
#define scLL(a) scanf("%I64d", &(a))
typedef long long LL;
using namespace std;
const LL MOD = 1000000000 + 7;
vector<int> counter;

int D[101][4][500000];

int get_key(vector<int> &c) {
	int result = 0;
	int sum = 1;
	for (int i = 0; i < counter.size(); ++i) {
		result += c[i] * sum;
		sum *= (counter[i] + 1);
	}

	return result;
}
vector<int> g;
int n;
int p;
int rec(int pos, int q, vector<int> &c) {
	int key = get_key(c);
	if (D[pos][q][key] != -1) return D[pos][q][key];

	if (pos == n) return 0;

	int result = 0;

	for (int i = 0; i < c.size(); ++i) {
		if (c[i] == 0) continue;

		int new_q = q + i;
		c[i]--;
		result = max(result, rec(pos + 1, new_q % p, c) + (int)((new_q % p) == 0 || (pos + 1)== n));
		c[i]++;
	}

	return D[pos][q][key] = result;
}

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif	
	ios::sync_with_stdio(false);
	cin.tie();

	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt) {
		memset(D, -1, sizeof(D));
		
		cin >> n >> p;
		g.clear();
		g.resize(n);

		forn(i, 0, n)cin >> g[i];

		counter.clear();
		counter.resize(p);
		forn(i, 0, n)counter[g[i] % p]++;

		auto tmp = counter;

		cout << "Case #" << tt + 1 << ": " << rec(0, 0, tmp)<<endl;
	}

	return 0;
}