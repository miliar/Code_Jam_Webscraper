#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const R PI = acos(-1);
const int MAXN = 1<<20;
const int P = 1e9+7;

char s[100][100];

int main(){
#ifdef LOCAL
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		printf("Case #%d:\n", i0);
		int n, m;
		int i, j;
		scanf("%d%d", &n, &m);
		for(i = 0; i < n; i++)
			scanf("%s", s[i]);
		for(i = 0; i < n; i++){
			for(j = 1; j < m; j++)
				if(s[i][j] == '?')
					s[i][j] = s[i][j-1];
			for(j = m-2; j >= 0; j--)
				if(s[i][j] == '?')
					s[i][j] = s[i][j+1];
		}
		for(i = 1; i < n; i++){
			for(j = 0; j < m; j++)
				if(s[i][j] == '?')
					s[i][j] = s[i-1][j];
		}
		for(i = n-2; i >= 0; i--)
			for(j = 0; j < m; j++)
				if(s[i][j] == '?')
					s[i][j] = s[i+1][j];
		for(i = 0; i < n; i++)
			printf("%s\n", s[i]);
	}
	return 0;
}
