#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long LL;
const int sz=1e5+7;
double a[56];
int dcmp(double x){ if(x>1e-8) return 1; if(x<-1e-8) return -1; return 0; }
priority_queue<double,vector<double>,greater<double> > Q;
int main()
{
	//freopen("C-small-1-attempt0.in","r",stdin);
	//freopen("C-small-1-attempt0.out","w",stdout);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{
		while(!Q.empty()) Q.pop();
		int N,K,i; double P; cin>>N>>K; cin>>P;
		for(i=1;i<=N;i++){cin>>a[i]; Q.push(a[i]);}
		a[++N]=1; Q.push(a[N]);
		while(dcmp(P)>0)
		{
			//printf("P_%f\n",P);
			double u=Q.top(); Q.pop();
			int cnt=1;
			double v=Q.top();
			while(dcmp(u-v)==0)
			{
				Q.pop(); cnt++;
				v=Q.top();
			}
			double t=min(P,(v-u)*cnt);
			//printf("u_%f,v_%f,t_%f,P_%f,cnt_%d\n",u,v,t,P,cnt);
			P-=t; u+=t/cnt;
			for(int ii=1;ii<=cnt;ii++) Q.push(u);
		}
		double ans=1;
		while(!Q.empty())
		{
			double u=Q.top(); ans*=u; Q.pop();
			//printf("A_%f\n",u);
		}
		printf("Case #%d: %.8f\n",casi,ans);
	} 
	return 0;
}

