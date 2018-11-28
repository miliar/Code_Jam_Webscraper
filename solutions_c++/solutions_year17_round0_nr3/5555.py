
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
int L[N],R[N];
bool a[N];


void print(bool a[],int n)
{
	int i;
	loop(i,n)
		cout<<a[i]<<' ';
	cout<<'\n';
}

#undef int
int main()
{
#define int long long
	ios_base::sync_with_stdio(false);
	int n,t,m,T,l,k,ans,i,j,res=0,fl;
	t=1;
	int maxi,maxi2,maxi3;
	int idx;
	cin>>(T);
	Loop(t,T)
	{
		cout<<"Case #"<<t<<": ";
		cin>>n>>k;
		loop(i,n+2)
			a[i]=0;
		a[0]=1;
		a[n+1]=1;
		while(k--)
		{
			int Lt=0,Rt=n+1;
			for(int i=1;i<=n;++i)
			{
				if(!a[i])
					L[i]=i-Lt-1;
				else
				{
					L[i]=0;
					Lt=i;
				}
			}

			for(int i=n;i>=0;--i)
			{
				if(!a[i])
					R[i]=Rt-i-1;
				else
				{
					R[i]=0;
					Rt=i;
				}
			}

			maxi=0,maxi2=0;
			maxi3=0;
			Loop(i,n)
			{
				maxi=max(maxi,min(L[i],R[i]));
				maxi2=max(maxi2,max(L[i],R[i]));
			}

			idx=-1;
			int ct=0;
			Loop(i,n)
			{
				if(min(L[i],R[i]) == maxi)
				{
					ct++;
					idx=i;
					maxi3=max(maxi3,max(L[i],R[i]));
				}
			}

		//	DB3(ct,maxi2,maxi);

			if(ct == 1)
				a[idx]=1;
			else
			{
				ct=0;
				Loop(i,n)
				{
					if(max(L[i],R[i]) == maxi3 and min(L[i],R[i]) == maxi)
					{
						idx=i;
						break;
					}
				}
		//		DB(idx);

				a[idx]=1;
			}
		//print(a,n+2);
		}


		cout<<max(L[idx],R[idx])<<' '<<min(L[idx],R[idx])<<'\n';

	}

	return 0;
}

