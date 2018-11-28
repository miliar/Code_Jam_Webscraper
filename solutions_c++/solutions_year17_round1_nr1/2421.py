#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<string>
using namespace std;
int T;
int dx[4] = {1,-1,0,0};
int dy[4]= {0,0,-1,1};
void Gao(){
	scanf("%d",&T);
	char a[30][30];
	char b[30][30];
	 
	for(int tt=1;tt<=T;tt++){
		int r,c;
		
		scanf("%d %d",&r,&c);
		string ss;
		for(int i=0;i<r;i++){
			scanf("%s",a[i]);
				//	printf("%s\n",a[i]);
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<r;j++){
				b[i][j]='*';
			}
		}
		/*
		for(int i=0;i<c;i++){
			if(a[0][i]!='?'){
				b[0][i]=a[0][i];
			}else{
				for(int j=1;j<r;j++){
					if(a[j][i]!='?'){
						b[0][i]=a[j][i];
						break;
					}
				}
			}
		}
		for(int i=0;i<c;i++){
			for(int j=1;i+j<c;j++){
				if(b[0][i+j]!='*'){
					break;
				}else{
					b[0][i+j]=b[0][i];
				}
			}
			for(int j=-1;i+j>=0;j--){
				if(b[0][i+j]!='*'){
					break;
				}else{
					b[0][i+j]=b[0][i];
				}
			}
		}
		for(int i=1;i<r;i++){
			for(int j=0;j<c;j++){
				if(a[i][j]=='?'){
					b[i][j]=b[i-1][j];
				}else{
					b[i][j]=a[i][j];
				}
			}
		}
		*/

		/*
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(a[i][j]!='?'){
					b[i][j]=a[i][j];
					for(int k=0;k<r;k++){
						if(b[k][j]=='*')
						{
							b[k][j]=a[i][j];
						}
					}
				}else{
					if(!(b[i][j]>='A'&&b[i][j]<='Z')){
						b[i][j]='*';
					}
				}
			}
		}
		*/
		/*
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(a[i][j]=='?'){
					continue;
				}else{
					int maxl;
					int max
					for(int k=0;i+k<r;k++){
						for(int)
					}
				}
			}
		}
		*/
		for(int k=0;k<4;k++){
			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					if(a[i][j]=='?'){
						for(int tx= i,ty=j;
								tx>=0&&tx<r&&ty>=0&&ty<c;
									tx+=dx[k],ty+=dy[k]){
								if(a[tx][ty]!='?'){
									a[i][j]=a[tx][ty];
									break;
								}
							}
					}else{
						a[i][j]=a[i][j];
					}
				}
			}
		}
		printf("Case #%d:\n",tt);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				printf("%c",a[i][j]);
			}
			printf("\n");
		}
	}
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	Gao();
		return 0;
}
