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
int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	#ifndef ONLINE_JUDGE
		freopen("B-large.in","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		string a;
		cin>>a;
		for(int i=a.length()-2;i>=0;i--)
		{
			if(a[i]>a[i+1])
			{
				a[i]--;
				for(int j=i+1;j<a.length();j++) a[j]='9';
			}
		}
		for(int i=0;i<a.length();i++)
		if(a[0]=='0') a.erase(0,1);
		cout<<"Case #"<<cas<<": "<<a<<endl;
	}
    return 0;
}

