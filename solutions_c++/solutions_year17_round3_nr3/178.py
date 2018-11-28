/* ***********************************************
Author        :axp
Created Time  :2017/4/30 17:54:51
TASK		  :C.cpp
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
const double eps=1e-9;
int n,m;
int T;
double u;
const int N = 55;
double p[N];
double sum;

double work()
{
	if(n==1)return sum+u;
	priority_queue<pair<int,double> > q;
	for(int i=0;i<n;i++)
		q.push(make_pair(1,1-p[i]));
	while(u>eps && q.size()>1)
	{
		double a=q.top().second;
		int v=q.top().first;
		q.pop();
		double b=q.top().second;
		q.pop();
		double t=a-b;
		if(t<eps)
		{
			q.push(make_pair(v+1,a));
			continue;
		}
		a-=min(t,u/v);
		u-=min(t,u/v)*v;
		q.push(make_pair(v,a));
		q.push(make_pair(1,b));
	}
	if(q.size()==1)
		return pow(1-q.top().second+u/n,n);
	double re=1;
	while(q.size())
	{
		re*=1-q.top().second;
		q.pop();
	}
	return re;
}

double work2()
{
	sort(p+1,p+n+1);
	p[n+1]=1;
	double re=0;
	double s=0;
	for(int i=1;i<=n;i++)
	{
		s+=p[i];
		double avg=(s+u)/i;
		if(avg+eps<p[i])break;
		double now=pow(min(avg,1.0),i);
		for(int j=i+1;j<=n;j++)now*=p[j];
		re=max(re,now);
	}
	return re;
}

int main()
{
    //freopen("in.txt","r",stdin);
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%d%d%lf",&n,&m,&u);
		sum=0;
		for(int i=1;i<=n;i++)scanf("%lf",&p[i]),sum+=p[i];
		double ans=work2();
		printf("Case #%d: %.10lf\n",kase,ans);
	}
    return 0;
}
