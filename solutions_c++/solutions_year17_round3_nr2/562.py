#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cstring>
#define time avabvhisbviw
using namespace std;
const int maxn = 200;
const int day = 1440;
const int oo = 1000000000;
int ac,aj;
int mark[day+1];
int dp[3][3][day+1][day+1];
/*bool cmp(int x,int y)
{
	return s[x]<s[y];
}*/
int caldp(int fir,int pre,int x,int y)
{
	if (dp[fir][pre][x][y]==-1)
	{
		int curtime=1440-x-y;
		if (curtime==1439)
		{
			int p;
			if (x==1) p=1;
			else p=2;
			if (p!=fir) dp[fir][pre][x][y]=oo;
			else dp[fir][pre][x][y]=(p!=pre);
		}
		else
		if (mark[curtime]==1)
		{
			if (x>0) dp[fir][pre][x][y]=caldp(fir,1,x-1,y)+(1!=pre);
			else dp[fir][pre][x][y]=oo;
		}
		else
		if (mark[curtime]==2)
		{
			if (y>0) dp[fir][pre][x][y]=caldp(fir,2,x,y-1)+(2!=pre);
			else dp[fir][pre][x][y]=oo;
		}
		else
		if (mark[curtime]==0)
		{
			dp[fir][pre][x][y]=oo;
			if (x>0) dp[fir][pre][x][y]=min(dp[fir][pre][x][y],caldp(fir,1,x-1,y)+(1!=pre));
			if (y>0) dp[fir][pre][x][y]=min(dp[fir][pre][x][y],caldp(fir,2,x,y-1)+(2!=pre));
		}
	}
	//if (day-x-y==841) cout << fir << ' ' << pre << ' ' << x << ' ' << y << ' ' << dp[fir][pre][x][y] << '\n';
	return dp[fir][pre][x][y];
}
void solve()
{
	cin >> ac >> aj;
	memset(mark,0,sizeof(mark));
	for (int i=1; i<=ac; i++)
	{
		int s,f;
		cin >> s >> f;
		for (int j=s; j<f; j++)
			mark[j]=1;

	}
	for (int i=1; i<=aj; i++)
	{
		int s,f;
		cin >> s >> f;
		for (int j=s; j<f; j++)
			mark[j]=2;
	}
	memset(dp,-1,sizeof(dp));
	cout << min(caldp(1,1,720,720),caldp(2,2,720,720));
	/*sort(id+1,id+1+ac+aj,cmp);
	int res=0;
	// forgot to sort
	// fill the gap
	for (int i=1; i<ac+aj; i++)
	{
		if (rp[id[i]]==rp[id[i+1]])
		{
			if (s[id[i+1]]-f[id[i]]<=time[rp[id[i]]])
				time[rp[id[i]]]-=(s[id[i+1]]-f[id[i]]);
			else
			{
				time[3-rp[id[i]]]-=(s[id[i+1]]-f[id[i]]-time[rp[id[i]]]);
				time[rp[id[i]]]=0;
				res+=2;
			}
		}
	}
	// first and last gap
	s[0]=0,f[0]=0;
	s[ac+aj+1]=1440,f[ac+aj+1]=1440;
	if (time[rp[id[1]]]>s[id[1]]-f[0])
		time[rp[id[1]]]-=(s[id[1]]-f[0]);
	else
	{
		res++;
		time[3-rp[id[1]]]-=(s[id[1]]-f[0]-time[rp[id[1]]]);
		time[rp[id[1]]]=0;
	}
	if (time[rp[id[ac+aj]]]>s[ac+aj+1]-f[id[ac+aj]])
		time[rp[id[ac+aj]]]-=(s[ac+aj+1]-f[id[ac+aj]]);
	else
	{
		res++;
		time[3-rp[id[ac+aj]]]-=(s[ac+aj+1]-f[id[ac+aj]]-time[rp[id[ac+aj]]]);
		time[rp[id[ac+aj]]]=0;
	}
	// middle gap
	for (int i=1; i<ac+aj; i++)
		if (rp[id[i]]!=rp[id[i+1]])
		{
			res++;
			//if (s[id[i+1]]-f[id[i+1]])
		}
	cout << res;*/
}
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i=1; i<=t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}