#include <bits/stdc++.h>

using namespace std;

const int N=1000070; //10e6

#define ll long long int
#define inf 0x3f3f3f3f
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define ii tuple<int, int>
#define all(x) (x).begin(), (x).end()

char mat[30][30];
int x, y;

void fill(int i, int j, int op){
	char curr=mat[i][j];
	if(op==1){
		for(int w=j+1; w<y; w++){
			if(mat[i][w]=='?'){
				mat[i][w]=curr;
			}else break;
		}
		for(int w=j-1; w>=0; w--){
			if(mat[i][w]=='?'){
				mat[i][w]=curr;
			}else break;	
		}
	}else{
		for(int w=i+1; w<x; w++){
			if(mat[w][j]!='?'){
				curr=mat[w][j];
				for(int k=j; k<y; k++){
					if(mat[w][k]==curr){
						mat[i][k]=curr;
					}
				}
				return;
			}
		}
		for(int w=i-1; w>=0; w--){
			if(mat[w][j]!='?'){
				curr=mat[w][j];
				for(int k=j; k<y; k++){
					if(mat[w][k]==curr){
						mat[i][k]=curr;
					}
				}
				return;
			}
		}
	}
}
int main(int argc, char const *argv[]){
	int t, counter=1;
	scanf("%d", &t);

	while(t--){
		scanf("%d %d ", &x, &y);
		for(int i=0; i<x; i++){
			for(int j=0; j<y; j++){
				scanf("%c", &mat[i][j]);
			}
			scanf("%*c");
		}

		for(int i=0; i<x; i++){
			for(int j=0; j<y; j++){
				if(mat[i][j]!='?')fill(i, j, 1);
			}
		}
		for(int i=0; i<x; i++){
			for(int j=0; j<y; j++){
				if(mat[i][j]=='?'){
					fill(i, j, 2);
				}
			}
			
		}
		printf("Case #%d:\n", counter++);
		for(int i=0; i<x; i++){
			for(int j=0; j<y; j++){
				printf("%c", mat[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}