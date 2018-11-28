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

bool tidy(int N){
	int last = 10;
	while(N > 0){
		if(N % 10 > last){
			return false;
		}
		last = N % 10;
		N /= 10;
	}
	return true;
}

int main(){
	II(TC);
	for(int tc = 1; tc <= TC; tc++){
		II(N);
		while(N > 0){
			if(tidy(N)){
				printf("Case #%d: %d\n", tc, N);
				break;
			}
			N--;
		}
	}
	return 0;
} 
