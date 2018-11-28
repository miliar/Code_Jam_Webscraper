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

bool tidy(int x){
	int last=x%10;
	int tmp=x/10;
	while(tmp){
		if(tmp%10 > last)return 0;
		last=tmp%10;
		tmp/=10;
	}
	return 1;
}
int t,n;
int main(){
	scanf("%i",&t);
	int tc=1;
	while(t--){
		scanf("%i",&n);
		int ans=0;
		for(int i=1;i<=n;i++)
			if(tidy(i))ans=i;
		printf("Case #%i: %i\n",tc++,ans);
	}
	return 0;
}

