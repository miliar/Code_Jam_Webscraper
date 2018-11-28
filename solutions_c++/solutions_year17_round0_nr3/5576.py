#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <ctime>
#include <list>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <intrin.h>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

#define IMP (1 << 30)
#define NOP (-1)

int T;
ll N, K;
ll y, z;

int main(){
	cin >> T;

	for (int t = 1; t <= T; t++){
		ll Ls, Rs;
		priority_queue <ll> stall;

		cin >> N >> K;
		stall.push(N);

		for (ll i = 0; i < K; i++){
			//ll tmp = stall.front();
			ll tmp = stall.top();
			stall.pop();

			Ls = Rs = tmp / 2;
			if (Rs > 0)	stall.push(Rs);
			if (Ls + Rs == tmp) {

				if (Ls < 1)
					continue;
				Ls--;
			}

			if (Ls > 0) stall.push(Ls);
		}

		if (Ls < Rs)	y = Rs, z = Ls;
		else	y = Ls, z = Rs;

		printf("Case #%d: %lld %lld\n", t, y, z);	
	}



	return 0;
}