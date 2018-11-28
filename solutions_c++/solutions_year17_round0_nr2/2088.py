#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm> 

using namespace std;

int len;
char A[100];
int B[100];

void solve(){
	if(len == 1){
		printf("%d\n", B[1]);
		return;
	}
	for(int i = len - 1; i >= 1; --i){
		if(B[i] > B[i + 1]){
			B[i]--;
			for(int j = i + 1; j <= len; ++j)
				B[j] = 9;
		}
	}
	int k = 1;
	while(B[k] == 0 && k <= len){
		++k;
	}
	if(k > len){
		printf("What the fuck?\n");
		throw(-1);
	}
	for(int j = k; j <= len; ++j)
		printf("%d", B[j]);
	printf("\n");
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		scanf("%s", A + 1);
		len = strlen(A + 1);
		for(int i = 1; i <= len; ++i)
			B[i] = A[i] - '0';
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
