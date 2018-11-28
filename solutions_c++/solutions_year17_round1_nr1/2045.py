#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

#define IMP (1 << 30)
#define NOP (-1)

int T;
int R, C;

char initial[30][30];

char dfsRow(int r, int c){
	if (c > C)	return '?';

	if (initial[r][c] == '?')	return initial[r][c] = dfsRow(r, c + 1);
	return initial[r][c];
}

char dfsCol(int r, int c){
	if (r > R)	return '?';
	if (initial[r][c] == '?')	return initial[r][c] = dfsCol(r + 1, c);
	return initial[r][c];
}


int main(){
	cin >> T;

	for (int t = 1; t <= T; t++){
		cin >> R >> C;
		//for (int r = 0; r <= R + 1; r++){
		//	for (int c = 0; c <= C + 1; c++){
		//		initial[r][c] = 'A';
		//	}
		//}


		for (int r = 0; r < R; r++)
			cin >> initial[r];


		for (int r = 0; r < R; r++){
			char tmp = '?';

			for (int c = 0; c < C; c++){
				if (initial[r][c] != '?')
					tmp = initial[r][c];

				if (initial[r][c] == '?')
					initial[r][c] = tmp;
			}
			tmp = '?';

			for (int c = C - 1; c >= 0; c--){

				if (initial[r][c] != '?')
					tmp = initial[r][c];


				if (initial[r][c] == '?')
					initial[r][c] = tmp;
			}
		}


		for (int c = 0; c < C; c++){
			char tmp = '?';

			for (int r = 0; r < R; r++){
				if (initial[r][c] != '?')
					tmp = initial[r][c];

				if (initial[r][c] == '?')
					initial[r][c] = tmp;
			}
			tmp = '?';

			for (int r = R-1; r >= 0; r--){

				if (initial[r][c] != '?')
					tmp = initial[r][c];


				if (initial[r][c] == '?')
					initial[r][c] = tmp;
			}
		}



		printf("Case #%d:\n", t);
		for (int r = 0; r < R; r++){
			cout << initial[r] << endl;
		}
	}



	return 0;
}




#if 0
int T;
ll N, K;
ll y, z;

int main(){
	cin >> T;

	for (int t = 1; t <= T; t++){
		ll minLs, minRs;
		ll maxLs, maxRs;

		cin >> N >> K;

		minRs = minLs = maxLs = maxRs = N;
		

		for (ll i = 1; i <= K; ){
			if (maxRs == 0)
				maxLs = maxRs = 0;

			else if (maxRs % 2 != 0) 
				maxLs = maxRs = (maxRs - 1) / 2;

			else if (maxRs % 2 == 0){
				maxRs = maxRs / 2;
				maxLs = maxRs - 1;
			}

			if (minRs == 0)
				minLs = minRs = 0;

			else if (minRs % 2 != 0){
				minLs = minRs = (minRs - 1) / 2;
			}

			else if (minRs % 2 == 0)
				minRs = minLs = minRs / 2 - 1;

			K -= i;
			i *= 2;

			if (i > K){
				i = 1;
				maxLs = minLs;
				maxRs = minRs;
				continue;
			}

		}
		y = maxRs, z = maxLs;
		//if (maxLs < maxRs)	y = maxRs, z = maxLs;
		//else	y = maxLs, z = maxRs;

		printf("Case #%d: %lld %lld\n", t, y, z);	
	}



	return 0;
}

#endif