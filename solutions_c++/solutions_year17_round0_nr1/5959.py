#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

#define maxN 1010
int T;
int RN = 0;
string S;
char dir[maxN];
int f[maxN];
int K;
int N;

int cal()
{
	memset(f, 0 ,sizeof(f));
	int res = 0;
	int sum = 0;
	for(int i=0; i+K <= N; i++) {
		if((dir[i] + sum) % 2 != 0) {
			res++;
			f[i] = 1;
		}
		sum += f[i];
		if(i - K + 1 >= 0) {
			sum -= f[i - K + 1];
		}
	}
	for(int i= N - K + 1; i < N; i++) {
		if((dir[i] + sum) % 2 != 0) {
			return -1;
		}
		if(i - K + 1 >= 0) {
			sum -= f[i - K + 1];
		}
	}
	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
#ifdef _DEBUG
	freopen("test.in", "r", stdin);
#else
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	cin >> T;
	while(T--) {
		cin >> S;
		cin >> K;
		N = S.length();
		for(int i=0; i<N; i++) {
			if(S[i] == '-')
				dir[i] = 1;
			else
				dir[i] = 0;
		}

		int Final = cal();
		if(Final == -1) {
			cout << "Case #" << ++RN << ": IMPOSSIBLE" << '\n';
		}
		else {
			cout << "Case #" << ++RN << ": " << Final << '\n';
		}

	}
	return 0;
}