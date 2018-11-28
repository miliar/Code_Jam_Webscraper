#include <stdio.h>

char ori[110][110],tor[110][110],bis[110][110];
int n,q,resp;

void add_tor(int x,int y){
	resp++;
	for(int i=1;i<=n;i++){
		tor[x][i]=tor[i][y]='*';
	}
	tor[x][y]='x';
}

void add_bis(int x,int y){
	resp++;
	for(int i=1;i<x+y;i++){
		if(i<=n && x+y-i<=n) bis[i][x+y-i]='*';
	}
	for(int i=1;i<=n;i++){
		if(1<=y-x+i && y-x+i<=n) bis[i][y-x+i]='*';
	}
	bis[x][y]='+';
}

int main(){
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		scanf("%d %d",&n,&q);
		
		resp=0;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				ori[i][j]=tor[i][j]=bis[i][j]='.';
			}
		}
		
		for(int i=0;i<q;i++){
			int x,y;
			char c;
			scanf(" %c %d %d",&c,&x,&y);
			ori[x][y]=c;
			if(c=='x' || c=='o'){
				add_tor(x,y);
			}
			if(c=='+' || c=='o'){
				add_bis(x,y);
			}
		}
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(tor[i][j]=='.'){
					add_tor(i,j);
				}
				if(tor[i][n+1-j]=='.'){
					add_tor(i,n+1-j);
				}
				if(tor[j][i]=='.'){
					add_tor(j,i);
				}
				if(tor[n+1-j][i]=='.'){
					add_tor(n+1-j,i);
				}
				
				
				if(bis[i][j]=='.'){
					add_bis(i,j);
				}
				if(bis[i][n+1-j]=='.'){
					add_bis(i,n+1-j);
				}
				if(bis[j][i]=='.'){
					add_bis(j,i);
				}
				if(bis[n+1-j][i]=='.'){
					add_bis(n+1-j,i);
				}
			}
		}
		
		/*
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				printf("%c",tor[i][j]);
			}
			printf("\n");
		}
		printf("\n");
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				printf("%c",bis[i][j]);
			}
			printf("\n");
		}
		*/
		int resp2=0;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(ori[i][j]=='+' && tor[i][j]=='x') resp2++;
				if(ori[i][j]=='x' && bis[i][j]=='+') resp2++;
				if(ori[i][j]=='.' && bis[i][j]=='+' && tor[i][j]=='x') resp2++;
				else if(ori[i][j]=='.' && bis[i][j]=='+') resp2++;
				else if(ori[i][j]=='.' && tor[i][j]=='x') resp2++;
			}
		}
		printf("Case #%d: %d %d\n",tt,resp,resp2);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(ori[i][j]=='+' && tor[i][j]=='x'){
					printf("o %d %d\n",i,j);
				}
				if(ori[i][j]=='x' && bis[i][j]=='+'){
					printf("o %d %d\n",i,j);
				}
				if(ori[i][j]=='.' && tor[i][j]=='x' && bis[i][j]=='+'){
					printf("o %d %d\n",i,j);
				}
				else if(ori[i][j]=='.' && tor[i][j]=='x'){
					printf("x %d %d\n",i,j);
				}
				else if(ori[i][j]=='.' && bis[i][j]=='+'){
					printf("+ %d %d\n",i,j);
				}
			}
		}
	}
	return 0;
}
		
		
		
		
		
		
