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
		freopen("C-small-2-attempt0.in","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		int n,k,ans2=INF,a,b;
		cin>>n>>k;
		priority_queue<int> q;
		q.push(n);
		for(int i=0;i<k;i++)
		{
			int tmp=q.top();q.pop();
			if(tmp&1)
			{
				a=tmp/2;
				b=tmp/2;
			}
			else
			{
				a=tmp/2;
				b=tmp/2-1;
			}
			q.push(a);
			q.push(b);
			ans2=min(ans2,b);
		}
		
		cout<<"Case #"<<cas<<": "<<a<<" "<<b<<endl;
	}
    return 0;
}

