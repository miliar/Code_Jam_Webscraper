#include<bits/stdc++.h>
using namespace std;

int t, n, k;
char pank[1010];
int v[1010];

int main(){
	scanf("%d", &t); 
	
	for(int c=1; c<=t; c++){
		scanf("%s", &pank);	
		int ind=0;
		while(pank[ind]!='\0'){
			if(pank[ind]=='+'){
				v[ind+1]=1;	
			}
			if(pank[ind]=='-'){
				v[ind+1]=-1;	
			}
			ind++;
		}
		n=ind;
		
		int resp=0;
		scanf("%d", &k);
		for(int i=1; i<=n-k+1; i++){
			if(v[i]==-1){
			 	for(int j=0; j<=k-1; j++){
				 	v[i+j]=-v[i+j];
				}
				resp++;
			}
	//		for(int j=1; j<=n; j++){
	//			printf("%d ", v[j]); 	
	//		}
	//		printf("\n");
		}
		for(int i=n-k+2; i<=n; i++){
			if(v[i]==-1) resp=-1;	
		}
		
		if(resp==-1) printf("Case #%d: IMPOSSIBLE\n", c);
		else printf("Case #%d: %d\n", c, resp);
		
	}
	
	return 0;	
}
