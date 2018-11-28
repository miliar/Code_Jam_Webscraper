#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <iostream>

#define MAXN 100005
#define INF 100000000
#define ll long long
#define llu unsigned long long
#define pii pair<int,int>
#define fs first
#define sc second

using namespace std;

int t,n,k;
char inp[1005];
int main(){
	scanf("%i",&t);
	int tc=1;
	while(t--){
		int ans=0;
		scanf("%s",&inp);n=strlen(inp);
		scanf("%i",&k);
		for(int i=0;i<=n-k;i++){
			if(inp[i]=='-'){
				ans++;
				for(int j=i;j<=i+k-1;j++)
					inp[j]=(inp[j]=='-')?'+':'-';
			}
		}
		bool solved=1;
		for(int i=0;i<n;i++)if(inp[i]=='-')solved=0;
		if(solved)
			printf("Case #%i: %i\n",tc++,ans);
		else
			printf("Case #%i: IMPOSSIBLE\n",tc++);
	}
	return 0;
}

