#include <bits/stdc++.h>
//template to keep things straight
 
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define sc(n) scanf("%d",&n)
#define scL(n) scanf("%lld",&n)
 
#define pr(n) printf("%d\n",n);
#define prL(n) printf("%lld\n",n);
#define newl printf("\n")
 
#define pb push_back
#define pf pop_front
#define in insert
#define ll long long 
#define F first
#define S second
 
#define mp make_pair
using namespace std;
#define tv(container, it)  for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define boost  ios::sync_with_stdio(false)//;cin.tie(0)
#define MOD 1000000007 //10^9+7
 
#define BLOCK 448
#define MAX 100001
#define INF 1000000001 //1000000000000000001 <- 10^18
 

int main()
{
	
int t;
cin>>t;
FOR(T,1,t+1)
{
int r,c;
cin>>r>>c;
string cake[r];
set<int>s;
FOR(i,0,r)
{
	int C=0;
	cin>>cake[i];

	FOR(j,0,c)
	{
		if(cake[i][j]=='?')
			C++;
	}
	if(C==c)
		s.in(i);

}


FOR(i,0,r)
{
	if(s.find(i)!=s.end())continue;
	FORD(j,c-1,0)
	{
		if(cake[i][j]=='?' && j+1<c)
			cake[i][j]=cake[i][j+1];
	}
	FOR(j,0,c)
	{
		if(cake[i][j]=='?' && j-1>=0)
			cake[i][j]=cake[i][j-1];	
	}
}

tv(s,it)
{
	int R=*it;
	//cout<<R<<"\n";
	int flag=0;
	FORD(i,R-1,0)
	{
		if(!(s.find(i)!=s.end()))
		{
		cake[R]=cake[i];
		flag=1;
		break;
		
		}
	}
	if(flag==0)
	{
	FOR(i,R+1,r)
	{   	
		if(!(s.find(i)!=s.end()))
		{
		cake[R]=cake[i];
		break;
		}
	}
	}
	s.erase(R);


}

cout<<"Case #"<<T<<":\n";

FOR(i,0,r)
cout<<cake[i]<<"\n";
}
}