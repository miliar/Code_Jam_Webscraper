#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<time.h>
#include<assert.h>
#include<iostream>
using namespace std;
typedef long long LL;
typedef pair<int,int>pi;
char s[33];
int main(){
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out.txt","w",stdout);
	int _;scanf("%d",&_);
	int cas=1;
	while(_--){
		scanf("%s",s);
		int n=strlen(s);
		for(int i=1;i<n;i++){
			if(s[i]<s[i-1]){
				s[i-1]--;
				for(int j=i;j<n;j++)s[j]='9';
				int j=i-1;
				while(j&&s[j]<s[j-1])s[j]='9',s[j-1]--,j--;
			}
		}
		LL x=0;
		for(int i=0;i<n;i++)x=x*10+s[i]-'0';
		printf("Case #%d: ",cas++);
		printf("%lld\n",x);
	}
	return 0;
}
