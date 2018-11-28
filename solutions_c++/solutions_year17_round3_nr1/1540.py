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
const long double eps = 1e-8;
const long double PI=acos(-1.0);
typedef long long LL;
struct node
{
	long double r,h;
}cake[1005];
bool cmp1(node a,node b){if(fabs(a.r-b.r)>eps)return a.r>b.r;return a.h>b.h;}
bool cmp2(node a,node b){return a.r*a.h>b.r*b.h;}
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
		int n,k;
		long double ans=0.0,tmp=0.0;
		cin>>n>>k;
		for(int i=0;i<n;i++)cin>>cake[i].r>>cake[i].h;
		//sort(cake,cake+n,cmp1);
		for(int i=n-k;i>=0;i--)
		{
			sort(cake,cake+n,cmp1);
			tmp=PI*cake[i].r*cake[i].r+2.0*PI*cake[i].r*cake[i].h;
			sort(cake+i+1,cake+n,cmp2);
			for(int j=i+1;j<i+k;j++)
			{
				tmp+=2.0*PI*cake[j].r*cake[j].h;
			}//cout<<tmp<<endl;
			ans=max(ans,tmp);
		}
		
		cout<<"Case #"<<cas<<": "<<fixed<<setprecision(7)<<ans<<endl;
	}
    return 0;
}

