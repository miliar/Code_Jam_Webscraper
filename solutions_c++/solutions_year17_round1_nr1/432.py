#include <cstdio>
#include <vector>
using namespace std;

char arr[25][26];
int R, C;
vector<int> list[25];

int main(){
	int cases;
	scanf("%d", &cases);
	
	for(int z=1; z<=cases; z++){
		scanf("%d %d", &R, &C);
		
		for(int i=0; i<R; i++) list[i].clear();
		
		for(int i=0; i<R; i++){
			scanf("%s", arr[i]);
			for(int j=0; j<C; j++){
				if(arr[i][j] != '?'){
					list[i].push_back(j);
				}
			}
		}
		
		int sr = 0;
		for(int i=0; i<R; i++){
			if(list[i].size() == 0) continue;
			int sc = 0;
			for(int j=0; j<list[i].size(); j++){
				for(int r=sr; r<=i; r++){
					for(int c=sc; c<=list[i][j]; c++){
						arr[r][c] = arr[i][list[i][j]];
					}
				}
				sc = list[i][j]+1;
				if(j == list[i].size()-1){
					for(int r=sr; r<=i; r++){
						for(int c=sc; c<C; c++){
							arr[r][c] = arr[i][list[i][j]];
						}
					}
				}
			}
			sr = i+1;
		}
		if(sr != R){
			int sc = 0;
			for(int j=0; j<list[sr-1].size(); j++){
				for(int r=sr; r<R; r++){
					for(int c=sc; c<=list[sr-1][j]; c++){
						arr[r][c] = arr[sr-1][list[sr-1][j]];
					}
				}
				sc = list[sr-1][j]+1;
				if(j == list[sr-1].size()-1){
					for(int r=sr; r<R; r++){
						for(int c=sc; c<C; c++){
							arr[r][c] = arr[sr-1][list[sr-1][j]];
						}
					}
				}
			}
		}
		printf("Case #%d:\n", z);
		for(int i=0; i<R; i++){
			printf("%s\n", arr[i]);
		}
	}
	
	return 0;
}