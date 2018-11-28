#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int n, k, B[1010];
char A[1010];

void solve(){
	int res = 0;
	for(int i = 1; i <= n - k + 1; ++i){
		if(B[i] == 0){
			++res;
			for(int j = 0; j < k; ++j){
				B[i + j] ^= 1;
			}
		}
	}
	for(int i = 1; i <= n; ++i){
		if(B[i] == 0){
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", res);
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, tt = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%s", A + 1);
		scanf("%d", &k);
		n = strlen(A + 1);
		for(int i = 1; i <= n; ++i){
			B[i] = (A[i] == '-') ? 0 : 1;
		}
		printf("Case #%d: ", ++tt);
		solve();
	} 
	return 0;
}


