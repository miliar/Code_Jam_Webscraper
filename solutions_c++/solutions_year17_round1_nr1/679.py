#include<iostream>
#include<cstdio>
using namespace std;

char cake[30][30];
int R,C;

void fillCake();

int main(){

	int T;
	scanf("%d", &T);
	
	for(int i=1;i<=T;i++){
		
		scanf("%d %d", &R, &C);
		for(int j=1;j<=R;j++)
			scanf("%s", cake[j-1]);

		fillCake();	
		printf("Case #%d:\n", i);
		for(int i=0;i<R;i++)
			printf("%s\n",cake[i]);
	}
}


void fillCake(){

	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			if(cake[i][j] == '?'){
				
				if(j > 0 && cake[i][j-1] != '?'){
					
					cake[i][j] = cake[i][j-1];
				}
			}
			else if(j > 0 && cake[i][j-1] == '?'){
				for(int k =0;k<j;k++)
					cake[i][k] = cake[i][j];
			} 
		}	
		if(cake[i][0] == '?'){
			if(i > 0 && cake[i-1][0] != '?'){
				for(int k=0;k<C;k++)
					cake[i][k] = cake[i-1][k];
			}
				
		}
	}

	int i;
	for(i = 0;i<R;i++)
		if(cake[i][0] != '?')
			break;

	for(int l=i-1;l>=0;l--){
		for(int k=0;k<C;k++)
			cake[l][k] = cake[l+1][k];
	}


}


