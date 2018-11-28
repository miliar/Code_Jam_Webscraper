#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define ll long long
#define N 

int mark[102][102][102][102];
queue<pair<pair<int,int>,pair<int,int> > > q;
inline void func(int a,int b,int c,int d,int val)
{
	if(a<=0)	return;
	if(mark[a][b][c][d])	return;
	mark[a][b][c][d]=val;
	q.push(MP(MP(a,b),MP(c,d)));
}
int main()
{
	// freopen("C.in","r",stdin);
	// freopen("C.out","w",stdout);
	int t,i,j,k;
	sd(t);
	for(int tt=1;tt<=t;++tt)
	{
		while(!q.empty())	q.pop();
		cerr<<tt<<'\n';
		clr(mark);
		int hd,ad,hk,ak,B,D;
		sd(hd);sd(ad);sd(hk);sd(ak);sd(B);sd(D);
		
		mark[hd][ad][hk][ak]=1;

		q.push(MP(MP(hd,ad),MP(hk,ak)));
		int ans = -1;

		while(!q.empty())
		{
			pair<pair<int,int>,pair<int,int> > cur = q.front();
			int val = mark[cur.F.F][cur.F.S][cur.S.F][cur.S.S];
			q.pop();
			//attack
			if(cur.S.F-cur.F.S<=0)
			{
				ans=val;
				break;
			}
			int a=cur.F.F,b=cur.F.S;
			int c=cur.S.F,d=cur.S.S;
			func(a-d,b,c-b,d,val+1);	//attack
			func(a-d,b+B,c,d,val+1);	//buff
			func(hd-d,b,c,d,val+1);	//cure
			func(a-max(0,d-D),b,c,max(0,d-D),val+1);	//debuff
		}
		printf("Case #%d: ",tt);
		if(ans==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
}