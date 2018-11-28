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

#define FOR(nn) for(int ii = 0; ii < (nn); ii++)
#define FOR2(jj, nn) for(int jj = 0; jj < (nn); (jj)++)
#define FOR3(aa, nn) for(int ii = (aa); ii < (nn); ii++)
#define FORe(ii, nn) for(int ii = 1; ii <= nn; ii++)
#define SIZE(a) ((int)(a).size())

#define IMP (1 << 30)
#define NOP (-1)

int T;
double result;
int N, D;

double hour;

int main(){
	cin >> T;

	for (int t = 1; t <= T; t++){
		result = 0.0;
		hour = 0;

		cin >> D>> N;
		FOR2(i, N){
			int start, speed;
			cin >> start >> speed;
			if (hour < (double)(D - start) / speed) hour = (double)(D - start) / speed;
		}

		result = D / hour;
	
		printf("Case #%d: %llf\n", t, result);
		//cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}

#if 0

#define IMP (1 << 30)
#define NOP (-1)


int T;
int N, P;
int result;
int R[50];
vector <int> Q[50];
int offset[50];

bool visit[50][50];

int binaryLow(int q, int idx){
	int low = 0;
	int high = 1000000;
	int ret = 0;

	while (low <= high){
		int mid = (low + high) / 2;
		if (R[idx] * mid * (double)1.1 <= q){
			ret = mid;
			low = mid + 1;
		}
		else	high = mid - 1;
	}

	return ret;
}

int binaryHigh(int q, int idx){
	int low = 0;
	int high = 1000000;
	int ret = 0;

	while (low <= high){
		int mid = (low + high) / 2;
		if (R[idx] * mid * (double)0.9 <= q){
			ret = mid;
			low = mid + 1;
		}
		else	high = mid - 1;
	}

	return ret;
}

void dfs(int q, int idx){
	int lowKit = binaryLow(q, idx);
	int highKit = binaryHigh(q, idx);






}

int main(){
	cin >> T;

	for (int t = 1; t <= T; t++){
		result = 0;
		cin >> N >> P;
		for (int n = 0; n < N; n++)
			cin >> R[n];

		for (int n = 0; n < N; n++){
			Q[n].resize(P);
			offset[n] = 0;
			for (int p = 0; p < P; p++){
				cin >> Q[n][p];
			}
			::sort(Q[n].begin(), Q[n].end(), ::greater<int>());
		}

		dfs(Q[0][offset[0]], 0);


		printf("Case #%d: %d", t, result);
	}

	return 0;
}



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