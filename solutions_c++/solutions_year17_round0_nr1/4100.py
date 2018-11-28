/* ***********************************************
Author        :axp
Created Time  :2017/4/8 23:29:25
TASK		  :A.cpp
LANG          :C++
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef long long ll;
const int inf = 1<<30;
const int md = 1e9+7;
int n,m;
int T;
string s;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
	for(int kase=1;kase<=T;kase++)
	{
		cin>>s>>m;
		n=s.size();
		int ans=0;
		for(int i=0;i<=n-m;i++)
			if(s[i]=='-')
			{
				for(int j=0;j<m;j++)
					s[i+j]='+'+'-'-s[i+j];
				ans++;
			}

		for(int i=0;i<n;i++)
			if(s[i]=='-')
				ans=-1;
		printf("Case #%d: ",kase);
		if(ans<0)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}
    return 0;
}
