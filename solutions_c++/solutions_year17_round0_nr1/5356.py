
#ifndef ONLINE_JUDGE
#define DEBUG
#endif

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<utility>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define For(i,a,b) for(i=a;i<b;i++)
#define loop(i,b) for(i=0;i<b;i++)
#define Loop(i,b) for(i=1;i<=b;i++)
#define pi(n) cout<<n<<' '
#define si(n) cin>>n
#define int long long 
const int MOD=1e9+7;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef long long LL;
#define F first
#define S second
#define sz(x) (int) x.size()
#define pLL(x) cout<<x<<' '
#define fill(x,c) memset(x,c,sizeof(x))
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#ifdef DEBUG
#define DB(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define DB2(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
#define DB3(x, y, z)       cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<" | "<<#z<<": "<<z<<endl;
#else
#define DB(x)
#define DB2(x,y)
#define DB3(x,y,z)
#endif



const int N=5e5+5;

bool arr[N];

#undef int
int main()
{
#define int long long
	ios_base::sync_with_stdio(false);
	int n,t,m,T,l,k,ans,i,j,res=0,fl;
	t=1;
	string s;
	int flips;
	cin>>(T);
	Loop(t,T)
	{
		fl=0;
		cout<<"Case #"<<t<<": ";
		cin>>s>>k;
		int n=s.size();
		loop(i,n)
			arr[i]=0;
		bool flipped=0;
		int ct=0;
		loop(i,n)
		{
			flipped^=arr[i];
			bool isPositive=flipped^(s[i] == '+');
			if(!isPositive)
			{
				arr[i+k]=1;
				if(i+k-1>=n)
					fl=1;
				ct++;
				flipped^=1;
			}
		}

		if(fl)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<ct<<'\n';
        

	}
	return 0;
}

