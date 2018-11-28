
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

void print9(int n)
{
	for(int i=0;i<n;++i)
		cout<<9;
	cout<<'\n';
}

#undef int
int main()
{
#define int long long
	ios_base::sync_with_stdio(false);
	int n,t,m,T,l,k,ans,i,j,res=0,fl;
	t=1;
	string s;
	cin>>(T);
	Loop(t,T)
	{
		cout<<"Case #"<<t<<": ";
		cin>>s;
//		cout<<s<<' ';
		int idx=-1;
		n=s.size();
		for(int i=0;i+1<s.size();++i)
		{
			if(s[i+1]<s[i])
			{
				idx=i;
				break;
			}
		}

		if(idx == -1)
		{
			cout<<s<<'\n';
			continue;
		}
		string out="";

		for(int i=n-1;i>idx;--i)
			out+='9';
//		DB(idx);
//		DB(out);

		s[idx]--;
		out+=s[idx];
		int ii=-1;

		for(int i=idx-1;i>=0;--i)
		{
			assert(s[i]!='0');
			if(s[i]>s[i+1])
			{
				s[i]--;
				ii=i;
			}
			out+=s[i];
		}
		
	//	DB(ii);

		int x=out.size();
		if(out[x-1] == '0')
			print9(s.size()-1);
		else
		{
			reverse(out.begin(),out.end());
			if(ii!=-1)
			{
			string rr="";
			for(int i=0;i<=ii;++i)
				rr+=out[i];
			for(int i=n-1;i>ii;--i)
				rr+='9';
			cout<<rr<<'\n';

			}
			else
			{
			cout<<out<<'\n';
			}
		}


	}
	return 0;
}

