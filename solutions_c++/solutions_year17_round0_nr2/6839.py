#include<cstdio>
#include<iostream>
#include<cstring>

int main(){
				int T;
				char N[19];
				scanf("%d",&T);
				for(int i=0;i<T;i++){
								scanf("%s", N);
								for(int j=strlen(N)-1;j>0;j--){
												if(N[j]<N[j-1]){
																N[j-1]=N[j-1]-1;
																for(int l=j;l<strlen(N);l++)N[l]='9';
												}
								}
								if(N[0]!='0')printf("Case #%d: %s\n", i+1, N);
								else printf("Case #%d: %s\n", i+1, N+1);
				}
				return(0);
}

