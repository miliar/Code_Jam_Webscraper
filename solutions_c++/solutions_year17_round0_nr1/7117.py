#include<stdio.h>
#include<algorithm>
#include<vector>
#include<functional>
#include<stdlib.h>
#include<string.h>
using namespace std;

#define all(A) (A).begin(), (A).end()
#define II(A) int (A); scanf("%d",&(A));
#define DBG if(1)
#define NDBG if(0)

typedef long long ll;
typedef pair<int,int> pii;

char pancakes[10000];

int main(){
	int TC;
	scanf("%d", &TC);
	for(int tc = 1; tc <= TC; tc++){
		scanf("%s", pancakes);
		II(K);
		int N = strlen(pancakes);
		int ans = 0;
		for(int i = 0; i < N - K + 1; i++) {
			if(pancakes[i] == '-') {
				ans++;
				for(int j = i; j < i + K; j++) {
					pancakes[j] = '+' + '-' - pancakes[j];
				}
			}
		}
		bool impossible = false;
		for(int i = 0; i < N; i++) {
			if(pancakes[i] == '-') {
				impossible = true;
				break;
			}
		}
		if(impossible) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		else {
			printf("Case #%d: %d\n", tc, ans);
		}
	}
	return 0;
} 
