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

int T,kase=0;
string n;

int main()
{
	freopen("B-small-attempt6.in","r",stdin);
	freopen("tan_out.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		cin>>n;
		string ans;
		bool ok=true;
		int pos;
		for(int i=0;i<n.size()-1;i++)
			if(n[i]>n[i+1]){
				pos=i+1;ok=false;break;
			}
		if(ok)ans=n;
		else for(int i=n.size()-1;i>=0;i--){
			if(i==0 && n[i]=='0')break;
			if(i>pos)ans=ans+'9';
			else if(i<pos)ans=ans+n[i];
			else {
				n[i-1]--;
				ans=ans+'9';
				if(n[i-1]=='0')pos--;
				if(i<2)continue;
				if(n[i-1]<n[i-2])pos--;
			}
		}
		if(!ok)reverse(ans.begin(),ans.end());
		printf("Case #%d: ",++kase);
		cout<<ans<<endl;
	}
	return 0;
}



