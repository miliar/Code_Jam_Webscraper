//Author:- IITian_Sujal
//let's keep it simple and easy....
#include<bits/stdc++.h>
#define ll          long long int
#define mp          make_pair
#define pii         pair<int,int>
#define pb          push_back
#define vi          vector<int>
#define Max(a,b)    ((a)>(b)?(a):(b))
#define Min(a,b)    ((a)<(b)?(a):(b))
#define rep(i,a,b)  for (__typeof((b)) i=(a);i<(b);i+=1)
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define mod	        1000000007
#define endl        '\n'
using namespace std;
string s;
int a[1005];
int main()
{
	int t,k;
	freopen("1.txt","r",stdin);
	freopen("a.out","w",stdout);
	cin >>t;
	rep(r,1,t+1)
	{
		cin >>s;
		cin >>k;
		rep(i,0,1000)
		{
			a[i]=0;
		}
		int x=0;
		int z=0;
		int l=s.size();
		rep(i,0,l)
		{
			x+=a[i];
			if(x%2==1)
			{
				if(s[i]=='+')
				{
					s[i]='-';
				}
				else
				{
					s[i]='+';
				}
			}
			if(s[i]=='-')
			{
				if(i+k>l)
				{
					z=-1;
					break;
				}
				s[i]='+';
				x+=1;
				z+=1;
				a[i+k]=-1;
			}
		}
		if(z==-1)
		{
			cout<<"Case #"<<r<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<r<<": "<<z<<endl;	
		}
	}
}
