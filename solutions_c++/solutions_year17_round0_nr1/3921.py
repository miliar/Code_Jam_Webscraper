 #pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <string>
#include <string.h>
#include <sstream>
#include <cctype>
#include <climits>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <vector>
#include <iterator>
#include <algorithm>
#include <stack>
#define _clr(x,y) memset(x,y,sizeof(x))
#define _inf(x) memset(x,0x3f,sizeof(x))
#define pb push_back
#define mp make_pair
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;
typedef long long LL;
int k;
string s;
int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	#ifndef ONLINE_JUDGE
		freopen("A-large.in","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		cin>>s>>k;
		int ans=0,p=1;
		
		for(int i=0;i<s.length()-k+1;i++)
		{
			if(s[i]=='+') continue;
			ans++;
			for(int j=i;j<i+k;j++)
			{
				if(s[j]=='+') s[j]='-';
				else if(s[j]=='-') s[j]='+';
			}
		}
		//cout<<s<<endl;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				p=0;
				break;
			}
		}
		cout<<"Case #"<<cas<<": ";
		if(!p)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		else cout<<ans<<endl;
	}
    return 0;
}

