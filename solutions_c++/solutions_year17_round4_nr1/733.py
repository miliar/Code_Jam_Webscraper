#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int n, P;

int mod[4];

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, x;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		memset(mod, 0, sizeof(mod));
		scanf("%d %d", &n, &P);
		for(int i = 1; i <= n; ++i){
			scanf("%d", &x);
			mod[x % P] += 1;
		}
		int res = 0;
		if(P == 1){
			res = n;
		}
		else if(P == 2){
			res = mod[0] + (mod[1] + 1) / 2;
		}
		else if(P == 3){
			res = mod[0];
			if(mod[1] > mod[2]){
				res += mod[2];
				res += (mod[1] - mod[2]) % 3 == 0 ? (mod[1] - mod[2]) / 3 : (mod[1] - mod[2]) / 3 + 1;
			} 
			else{
				res += mod[1];
				res += (mod[2] - mod[1]) % 3 == 0 ? (mod[2] - mod[1]) / 3 : (mod[2] - mod[1]) / 3 + 1;
			} 
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
