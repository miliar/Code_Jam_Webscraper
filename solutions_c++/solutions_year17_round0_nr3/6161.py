#include<stdio.h>
#include<algorithm>
#include<vector>
#include<functional>
#include<stdlib.h>
using namespace std;

#define all(A) (A).begin(), (A).end()
#define II(A) int (A); scanf("%d",&(A));
#define DBG if(1)
#define NDBG if(0)

typedef long long ll;
typedef pair<int,int> pii;

int cnt[1000000+10];

int main(){
	II(TC);
	for(int tc = 1; tc <= TC; tc++){
		II(N)II(K);
		N++;
		for(int i = 0; i <= N; i++){
			cnt[i] = 0;
		}
		cnt[N] = 1;
		int it = N;
		while(K > 0){
			if(cnt[it] == 0){
				it--;
				continue;
			}
			cnt[it]--;
			cnt[(it+1)/2]++;
			cnt[it/2]++;
			K--;
		}
		printf("Case #%d: %d %d\n", tc, (it+1)/2 - 1, it/2 - 1);
	}
	return 0;
} 
