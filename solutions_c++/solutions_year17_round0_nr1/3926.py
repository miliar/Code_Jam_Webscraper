/*---------------------------------------------
				Author:TanYz
---------------------------------------------*/
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <cstdlib>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define mpii(a,b) make_pair(a,b)
const int INF=1<<30;
const int maxn=2333333;
const int mod=1000000007;

int T,k,kase=0;
string str;
int ans;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("tan_out.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		cin>>str>>k;
		int ans=0;
		for(int i=0;i<=str.size()-k;i++){
			if(str[i]=='+')continue;
			for(int j=i;j<i+k;j++){
				if(str[j]=='+')str[j]='-';
				else str[j]='+';
			}
			ans++;
		}
		bool ok=true;
		for(int i=str.size()-k;i<str.size();i++)if(str[i]=='-'){
			ok=false;break;
		}
		printf("Case #%d: ",++kase);
		if(ok)printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}
	return 0;
}



