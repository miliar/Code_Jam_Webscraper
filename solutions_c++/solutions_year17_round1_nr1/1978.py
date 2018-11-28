#include <bits/stdc++.h>
using namespace std;

int strlen(char A[]){
	int i = 0;
	while(A[i]!='\n' && A[i]!='\0' && A[i]!=' '){
		i++;
	}
	return i;
}

int main(){
	int t,r,c;
	scanf("%d",&t);
	for(int cases=1;cases<=t;cases++){
		scanf("%d %d",&r,&c);
		char A[r+1][c+1];
		for(int i=0;i<r;i++){
			scanf("%s",A[i]);
		}
		for(int j=0;j<c;j++){
			for(int i=0;i<r;i++){
				if(A[i][j]=='?'){
					bool a = false;
					for(int k=i-1;k>=0;k--){
						if(A[k][j]!='?' && a==false){
							a = true;
							A[i][j] = A[k][j];
						}
					}
					if(a==false){
						for(int k=i+1;k<r;k++){
							if(A[k][j]!='?' && a==false){
								a = true;
								A[i][j] = A[k][j];
							}
						}
					}
					/*
					if(a==false){
						// means case of all ?'s
						for(int x=j-1;x>=0;x--){
							if(A[0][x]!='?' && a==false){
								cout<<"\n1\n";
								a = true;
								for(int y=0;y<r;y++){
									A[y][j] = A[y][x];
								}
							}
						}
						if(a==false){
							for(int x=j+1;x<c;x++){
								printf("j+1:%d\n",j+1);
								printf("A[0][%d] : %c\n",j+1,A[0][j+1]);
								if(A[0][x]!='?' && a==false){
									printf("x:%d",x+1);
									cout<<"\n2\n";
									a = true;
									for(int y=0;y<r;y++){
										A[y][j] = A[y][x];
									}
								}
							}	
						}
					}
					*/
				}
			}
		}

		for(int j=0;j<c;j++){
			bool d = false;
			for(int i=0;i<r;i++){
				if(A[i][j]=='?' && d==false){
					d = true;
				}
			}
			if(d==true){
				bool b = false;
				for(int k=j-1;k>=0;k--){
					if(A[0][k]!='?' && b==false){
						b = true;
						for(int y=0;y<r;y++){
							A[y][j] = A[y][k];
						}
					}
				}
				if(b==false){
					for(int k=j+1;k<c;k++){
						if(A[0][k]!='?' && b==false){
							b = true;
							for(int y=0;y<r;y++){
								A[y][j] = A[y][k];
							}
						}
					}
				}
			}
		}

		printf("Case #%d:\n",cases);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				printf("%c",A[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}