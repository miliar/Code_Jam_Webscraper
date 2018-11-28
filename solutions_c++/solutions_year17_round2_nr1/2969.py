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
struct node
{
	int k,s;
}h[10005];
bool cmp(node a,node b){return a.k<b.k;}
int main()
{
	//ios_base::sync_with_stdio(false);cin.tie(0);
	#ifndef ONLINE_JUDGE
		freopen("A-large.in","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		int d,n,k[10005],s[10005];
		double ans;
		cin>>d>>n;
		for(int i=0;i<n;i++)
		{
			cin>>h[i].k>>h[i].s;
			//cin>>k[i]>>s[i];
		}
		sort(h,h+n,cmp);
		double tim[10005]={};
		tim[n-1]=(d-h[n-1].k)*1.0/h[n-1].s;
		for(int i=n-2;i>=0;i--)
		{
			tim[i]=(d-h[i].k)*1.0/h[i].s;
			tim[i]=max(tim[i],tim[i+1]);
		}
		ans=1.0*d/tim[0];
		cout<<"Case #"<<cas<<": "<<fixed<<setprecision(6)<<ans<<endl;
		//cout<<k<<" "<<tmp<<" "<<cnt<<endl;
	}
    return 0;
}

