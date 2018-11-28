#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:167772160000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
//typedef uint64_t ull;
//typedef std::pair<long double,long double> pdd;
#define for8(i) for( i = 1; i<=8; i++)
#define fori(N)          for(int i = 0; i<(N); i++)
#define forj(N)         for(int j = 0; j<(N); j++)
#define fork(N)         for(int k = 0; k<(N); k++)
#define forl(N)         for(int l = 0; l<(N); l++)
#define ford(N)         for(int d = 0; d<(N); d++)
#define fori1(N)          for(int i = 1; i<=(N); i++)
#define forj1(N)         for(int j = 1; j<=(N); j++)
#define fork1(N)         for(int k = 1; k<=(N); k++)
#define ford1(N)         for(int d = 1; d<=(N); d++)
#define PI (2*asin(1))
#define print(n) printf("%d ", (n))
#define printll(n) printf("%I64d ", (n))
#define printline() printf("\n")
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
template <typename T>
using min_heap = std::priority_queue<T, std::vector<T>, std::greater<T> >;
template <typename T>
using max_heap = std::priority_queue<T, std::vector<T>, std::less<T> >;

int n, q;
ll maxDist[200];
ll speed[200];
ll dist[200][200];
void getDist() {
	fori1(n)forj1(n) {
		cin >> dist[i][j];
		if (dist[i][j] == -1)dist[i][j] = 1E15;
	}
	fori1(n)
		forj1(n)
			fork1(n) {
		if (dist[j][k] > dist[j][i] + dist[i][k])
			dist[j][k] = dist[j][i] + dist[i][k];

	}
}

double minTime[200];
priority_queue<pair<double, int> >pq;
int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
#endif
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases; cin >> cases;
	for(int currentCase = 1;currentCase<=cases;currentCase++){
		cin >> n >> q;
		fori1(n)cin >> maxDist[i] >> speed[i];
		getDist();
		cout << "Case #" << currentCase << ": ";
		while (q--) {

			fori1(n)minTime[i] = -1;
			int u, k; cin >> u >> k;
			while (!pq.empty())
				pq.pop();
			pq.push(mp(0, u));
			while (!pq.empty()) {
				double t = -pq.top().first;
				int v = pq.top().second;
				pq.pop();
				if (minTime[v] >= -0.5)continue;
				minTime[v] = t;
				double sp = speed[v];
				double allowedDist = maxDist[v];
				fori1(n) {
					if (dist[v][i] > allowedDist)continue;
					double newTime = t + (double)dist[v][i] / sp;
					pq.push(mp(-newTime, i));
				}
			}
			cout << fixed<<setprecision(10)<<minTime[k] << " ";
		}
		
		cout << endl;

	}
	return 0;

}