#include<bits/stdc++.h>
using namespace std;
char mat[30][30];
int R,C;
bool isempty(int c){

	bool flag= true;
	int j;
	for(int i=0 ;i<R ;i++){
		if(mat[i][c] != '?'){

			for(j=i-1 ; j>=0 && mat[j][c] == '?';j--)
				mat[j][c] = mat[i][c];
			for(j=i+1 ; j<R && mat[j][c] == '?' ;j++)
				mat[j][c] = mat[i][c];

			flag = false;
		}
	}
	return flag;
}
int main(){

	int t,n,i,j,p,k;
	freopen("A-large (1).in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(p=1 ;p<=t ;p++){

		scanf("%d %d",&R,&C);
		for(i=0 ; i<R ;i++){
			scanf("%s",mat[i]);
		}
		for(i=0 ; i<C ;i++){
			if(!isempty(i)){
				for(j=i-1 ;j>=0 ;j--){
					if(isempty(j)){
						for(k=0 ;k<R ;k++)
							mat[k][j] = mat[k][j+1];
					}
				}

				for(j=i+1 ;j<C ;j++){
					if(isempty(j)){
						for(k=0 ;k<R ;k++)
							mat[k][j] = mat[k][j-1];
					}
				}
				break;
			}
		}
		printf("Case #%d:\n",p);

		for(i=0 ; i<R ;i++){
			printf("%s\n",mat[i]);
		}
	}

	return 0;
}

