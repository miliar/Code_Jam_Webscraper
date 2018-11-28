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
#define forl1(N)         for(int l = 1; l<=(N); l++)
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
int amounts[5];
int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
#endif
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios::sync_with_stdio(false); cin.tie(0);
	
	int casesNum; cin >> casesNum;
	for (int currentCase = 1; currentCase <= casesNum; currentCase++) {
		printf("Case #%d: ", currentCase);
		int n, p; cin >> n >> p;
		fori(p)amounts[i] = 0;
		fori(n) {
			int a; cin >> a;
			amounts[a%p]++;
		}
		if (p == 2) {
			int answer = amounts[0] + amounts[1] / 2;
			amounts[1] %= 2;
			if (amounts[1] == 0)answer--;
			cout << answer + 1 << endl;
		}
		else if (p == 3) {
			int answer = amounts[0];
			int x = min(amounts[1], amounts[2]);
			answer += x;
			amounts[1] -= x;
			amounts[2] -= x;
			answer += (amounts[2] + amounts[1]) / 3;
			if ((amounts[1] + amounts[2])%3 == 0)answer--;
			cout << answer +1<< endl;
		}
		else {
			int answer = amounts[0];
			int x = min(amounts[1], amounts[3]);
			answer += x;
			amounts[1] -= x;
			amounts[3] -= x;
			amounts[2] += amounts[1] / 2;
			amounts[1] %= 2;
			amounts[2] += amounts[3] / 2;
			amounts[3] %= 2;
			answer += amounts[2] / 2;
			amounts[2] %= 2;
			if (amounts[1] + amounts[2] + amounts[3] == 0)answer--;
			cout << answer+1 << endl;

		}

	}
	return 0;
}