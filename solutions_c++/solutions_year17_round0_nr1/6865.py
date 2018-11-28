#include<cstdio>
#include<iostream>
#include<cstring>

int main(){
				int T, K, minVal;
				char str[1001], possible;
				scanf("%d",&T);
				for(int i=0;i<T;i++){
								minVal=0;
								possible=1;
								scanf("%s %d", str, &K);
								for(int j=0;j<strlen(str);j++){
												if(str[j]=='+')continue;
												if(j+K>strlen(str)){possible=0;break;}
												minVal++;
												for(int l=j;l<j+K;l++)str[l]=str[l]=='+'?'-':'+';
								}
								if(!possible)printf("Case #%d: IMPOSSIBLE\n", i+1);
								else printf("Case #%d: %d\n", i+1, minVal);
				}
				return(0);
}

