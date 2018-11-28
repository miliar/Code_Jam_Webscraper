#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second

using namespace std;

int main(int argc, char* argv[]){
	int T;
	scanf("%d", &T);
	char line[100][100];
	for(int i = 1; i <= T; i++){
		printf("Case #%d:\n", i);
		int R, C;
		scanf("%d%d", &R, &C);
		for(int j = 0; j < R; j++)
			scanf("%s", line[j]);
		for(int j = 0; j < R; j++){
			for(int k = 0; k < C; k++){
				if(line[j][k] != '?'){
					for(int l = j+1; l < R; l++){
						if(line[l][k] != '?')
							break;
						line[l][k] = line[j][k];
					}
					for(int l = j-1; l >= 0; l--){
						if(line[l][k] != '?')
							break;
						line[l][k] = line[j][k];
					}
				}
			}
		}
		for(int j = 0; j < R; j++){
			for(int k = 0; k < C; k++){
				if(line[j][k] != '?'){
					for(int l = k+1; l < C; l++){
						if(line[j][l] != '?')
							break;
						line[j][l] = line[j][k];
					}
					for(int l = k-1; l >= 0; l--){
						if(line[j][l] != '?')
							break;
						line[j][l] = line[j][k];
					}
				}
			}
		}
		for(int j = 0; j < R; j++)
			printf("%s\n", line[j]);
	} 
    return 0;
}
