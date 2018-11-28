#include<stdio.h>
using namespace std;

char mat[30][30];
int f,c,t;
char letra,letraaux;
bool habia; 

int main(){
	freopen("A-large (1).in","r",stdin);
	freopen("salida.out","w",stdout);
	scanf("%d",&t);
	for(int h=1;h<=t;h++){
	scanf("%d%d",&f,&c);
	for(int i=0;i<f;i++){
		scanf("%s",mat[i]);
	}
	for(int i=0;i<f;i++){
		habia=false;
		for(int j=0;j<c;j++){
			if(mat[i][j]!='?'){
				habia=true;
				letra=mat[i][j];
				for(int k=j-1;k>=0&&mat[i][k]=='?';k--) mat[i][k]=letra;
			}
		}
		if(mat[i][c-1]=='?'&&habia) for(int j=c-1;j>=0&&mat[i][j]=='?';j--) mat[i][j]=letra;
	}
	for(int i=0;i<f;i++){
		for(int j=0;j<c;j++) if(mat[i][j]=='?'){
			for(int k=1;;k++){
				if(i+k<f&&mat[i+k][j]!='?'){
					mat[i][j]=mat[i+k][j];
					break;
				}else if(i-k>=0&&mat[i-k][j]!='?'){
					mat[i][j]=mat[i-k][j];
					break;
				}
			}
		}
	}
	printf("Case #%d: \n",h);
	for(int i=0;i<f;i++){
		for(int j=0;j<c;j++) printf("%c",mat[i][j]);
		printf("\n");
	}
	}
	fclose(stdout);
}