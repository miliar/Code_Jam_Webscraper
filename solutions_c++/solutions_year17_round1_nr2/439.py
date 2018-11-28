#include <cstdio>
#include <algorithm>
using namespace std;

int mem[50][50];
int arr[50][50];
int need[50], ind[50];
int N, P;

int main(){
	int cases;
	scanf("%d", &cases);
	
	for(int z=1; z<=cases; z++){
		scanf("%d %d", &N, &P);
		for(int i=0; i<N; i++){
			scanf("%d", &need[i]);
			ind[i] = 0;
		}
		
		for(int i=0; i<N; i++){
			for(int j=0; j<P; j++){
				scanf("%d", &arr[i][j]);
			}
			sort(arr[i], arr[i]+P);
		}
		
		int tot = 0;
		for(int sv=1; ; ){
			for(int i=0; i<N; i++){
				while(ind[i] < P && arr[i][ind[i]] < (sv*need[i])*0.9-1e-7){
					ind[i]++;
				}
				if(ind[i] == P) goto end;
			}
			bool ok = true;
			for(int i=0; i<N; i++){
				if(arr[i][ind[i]] > (sv*need[i])*1.1+1e-7){
					ok = false;
					sv++;
					break;
				}
			}
			if(ok){
				tot++;
				for(int i=0; i<N; i++){
					ind[i]++;
				}
			}
		}
		end:;
		printf("Case #%d: %d\n", z, tot);
	}
	
	return 0;
}