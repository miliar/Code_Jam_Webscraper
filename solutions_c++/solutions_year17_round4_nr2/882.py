#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>


using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<LL, LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))

const int MaxN = 1000;
pii tickets[MaxN + 10];
vi pass[MaxN+5]; // pass[place] - list of passengers for the seat "place"
vi seats[MaxN + 5]; // seats[p] - list of seat for passenger "p'
vi g[MaxN + 5];

vector<int> mt;
vector<char> used;

bool try_kuhn(int v) {
	if (used[v])  return false;
	used[v] = true;
	for (size_t i = 0; i<g[v].size(); ++i) {
		int to = g[v][i];
		if (mt[to] == -1 || try_kuhn(mt[to])) {
			mt[to] = v;
			return true;
		}
	}
	return false;
}

void solve()
{
	int n, c, m;
	cin >> n >> c >> m;
	for (int i = 0; i <= MaxN; i++)
	{
		pass[i].clear();
		seats[i].clear();
		g[i].clear();
	}

	for (int i = 0; i < m; i++)
	{
		int p, buyer;
		cin >> p >> buyer;
		tickets[i] = { p, buyer };
		pass[p].push_back(buyer);
		seats[buyer].push_back(p);
	}
	if (n == 1)
	{
		cout << m << " 0" << endl;
		return;
	}

	int numRides = max(pass[1].size(), max(seats[1].size(), seats[2].size()));
	cout << numRides << " ";
	for (int i = seats[1].size()-1; i >=0; i--)
	{
		int s1 = seats[1][i];
		for (int j = seats[2].size() - 1; j >= 0; j--)
			if (s1 != seats[2][j])
				g[i].push_back(j);
	}

	mt.assign(seats[2].size(), -1);
	int sum = 0;
	for (int v = 0; v<seats[1].size(); ++v) {
		used.assign(seats[1].size(), false);
		if (try_kuhn(v))
			sum++;
	}
	
	//numRides = sum;
	int s1 = seats[1].size() - sum;
	int s2 = seats[2].size() - sum;
	numRides -= sum;
	int swaps = s1 + s2 - numRides;
	cout << swaps << endl;

}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	//freopen("input.in", "r", stdin);
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output_B_small_1.txt","w",stdout);
	//cout<<fixed;
	//cout<<setprecision(9);

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}