#include <bits/stdc++.h>
using namespace std;
char arr[50][50];
int main(){

	int i,j,k,l,n,m,t,r,c;
	cin>>t;
	for(int test = 1; test <= t; test++){
		scanf("%d %d",&r,&c);
		for(i=0;i<r;i++){
			scanf("%s",arr[i]);
		}

		int ques[r+2];

		i = 0;
		for(i=0;i<r;i++){
			char fill = '\0';
			for(j=0;j<c;j++){
				if(arr[i][j] == '?' && fill != '\0'){
					arr[i][j] = fill;
				}
				else if(arr[i][j] != '?'){
					fill = arr[i][j];
				}
				else if(j > 0 && arr[i][j-1] != '?'){
					arr[i][j] = arr[i][j-1];
				}
				else{
					int jj = j;
					while(jj < c && arr[i][jj] == '?'){
						jj++;
					}
					if(jj == c){
						//lite hai, leave this grid
						j = jj;
						break;
					}
					else{
						//copy all the elements
						for(;j<jj;j++){
							arr[i][j] = arr[i][jj];
						}
					}
				}
			}
		}

		for(int y = 0; y <= r; y++){

			for(i=0;i<r;i++){
				ques[i] = 0;
			}
			for(i=0;i<r;i++){
				for(j=0;j<c;j++){
					if(arr[i][j] == '?'){
						ques[i]++;
					}
				}
			}

			for(i=0;i<r;i++){
				if(ques[i] == c){
					//need to copy some row here
					int ii = i;

					if(i > 0 && ques[i-1] == 0){
						for(j=0;j<c;j++){
							arr[i][j] = arr[i-1][j];
						}
						continue;
					}
				}
			}

			for(i=0;i<r;i++){
				ques[i] = 0;
			}
			for(i=0;i<r;i++){
				for(j=0;j<c;j++){
					if(arr[i][j] == '?'){
						ques[i]++;
					}
				}
			}


			for(i=r-1;i>=0;i--){
				if(ques[i] == c){
					//need to copy some row here

					if(i != r-1 && ques[i+1] == 0){
						for(j=0;j<c;j++){
							arr[i][j] = arr[i+1][j];
						}
						continue;
					}
				}
			}
		}

		printf("Case #%d:\n",test);
		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				printf("%c",arr[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}