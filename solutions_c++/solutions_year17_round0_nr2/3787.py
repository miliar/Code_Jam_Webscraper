#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#define inputt int t;cin>>t;
#define pi acos(-1.0)
#define lson o*2,l,m
#define rson o*2+1,m+1,r
#define INF 0x7f7f7f7f
#define lowbit(X) ((X)&(-X))
#define clr(X,Y) memset(X,Y,sizeof(X))
typedef long long ll;
using namespace std;
char s[20];
int main(){
	inputt
	for(int cas=1;cas<=t;cas++){
		scanf("%s",s);
		int i,j;
		int len=strlen(s);
		for(int i=1;i<len;i++){
			if(s[i]<s[i-1]){
				for(j=i-1;j>=0;j--){
					if(s[j]>s[j+1]){
						s[j]--;
					}
					else break;
				}
				for(j+=2;j<len;j++)s[j]='9';
				break;
			}
		}
		i=0;
		while(s[i]=='0')i++;
		printf("Case #%d: ",cas);
		for(;i<len;i++)printf("%c",s[i]);
		printf("\n");
	} 
	return 0;
}

