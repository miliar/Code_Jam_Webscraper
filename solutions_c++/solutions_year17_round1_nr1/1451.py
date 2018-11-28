#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <cassert>
#include <cmath>

#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>
#include <string>
#include <iterator>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <array>
#include <map>
#include <set>
#include <deque>
#include <set>
#include <unordered_set>
#include <unordered_map>

//#include<bits/stdtr1c++.h>

#define fi first
#define se second
#define inf 2147483647
#define mod 1000000009

#define mset(a, s) memset(a, s, sizeof(a))
#define forall(i,a,b) for(int i=a;i<b;++i)
#define max(a, b) (a < b ? b : a)
#define min(a, b) (a > b ? b : a)
#define all(a) a.begin(), a.end()
#define len(a) sizeof a/sizeof a[0]

/*/ --remove first * or add / before to enable scan--
#define scan(x) do{while((x=getchar())<0); for(x-='0';(_=getchar())>='0';x=(x<<3)+(x<<1)+_-'0');}while(0);
char _;//*/

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int T, R, C;
char grid[26][26];


int main(int argc, const char * argv[])
{
	scanf("%d", &T);

	for (int tc = 0; tc < T; ++tc) {
		scanf("%d%d", &R, &C);

		for (int i = 0; i < R; ++i) {
			scanf("%s", &grid[i]);
		}

		int numBad = 0;
		for (int i = 0; i < R; ++i) {
			char last = NULL;
			for (int j = 0; j < C; ++j) {
				char c = grid[i][j];
				if (c == '?') {
					if (last) grid[i][j] = last;
				}
				else last = c;
			}

			if (last == NULL) {
				if (i == numBad) ++numBad;
				else {
					for (int j = 0; j < C; ++j) {
						grid[i][j] = grid[i - 1][j];
					}
				}
			}

			for (int j = C-1; j >= 0; --j) {
				char c = grid[i][j];
				if (c == '?') {
					if (last) grid[i][j] = last;
				}
				else last = c;
			}
		}

		if (numBad >= R)  continue;

		for (int i = numBad-1; i >= 0; --i) {
			for (int j = 0; j < C; ++j) {
				grid[i][j] = grid[i + 1][j];
			}
		}

		printf("Case #%d:\n", tc + 1);
		for (int i = 0; i < R; ++i) {
			printf("%s\n", grid[i]);
		}
	}

	return 0;
}