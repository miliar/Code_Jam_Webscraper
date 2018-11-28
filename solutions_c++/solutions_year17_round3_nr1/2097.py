#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cmath>
#include <string>
#include <iomanip>
#include <algorithm>


#define MOD 1000000007
#define ll long long
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pll pair<long long,long long>
#define PI 3.14159265358979323846

using namespace std;
ll a[2][1000];
double ans=0;
ll n,k;
void findarea(ll rem,ll pos,double val)
{
	double res=0;
	if(rem==1)
	{
		for(ll r=pos+1;r<n;r++)
		{
			if(k==1)
				res=a[0][r]*PI*a[0][r]+2*PI*a[0][r]*a[1][r];
			else
				res=2*PI*a[0][r]*a[1][r];
			if(val+res>ans)
				ans=val+res;
		}
	}
	for(ll w=pos+1;w<n;w++)
	{
		if(k==rem)
			res=a[0][w]*PI*a[0][w]+2*PI*a[0][w]*a[1][w];
		else
			res=2*PI*a[0][w]*a[1][w];
		findarea(rem-1,w,val+res);
	}
}
int main() {
	// your code goes here
	ll t;
	scanf("%lld",&t);
    for(ll q=1;q<=t;q++)
	{
	    
	    cin>>n>>k;
	    
	    for(ll i=0;i<n;i++){
	        ll r,h;
	        cin>>r>>h;
	        a[0][i]=r;
	        a[1][i]=h;
	    }
	    ll tp1,tp2;
	    for(ll i=0;i<n;i++)
		{
			for(ll j=0;j<n-1;j++)
				if(a[0][j]<a[0][j+1])
				{
					tp1=a[0][j];
					tp2=a[1][j];
					a[0][j]=a[0][j+1];
					a[1][j]=a[1][j+1];
					a[0][j+1]=tp1;
					a[1][j+1]=tp2;
				}
		}
		findarea(k,-1,0);
		cout<<"Case #"<<q<<": "<<setprecision(20)<<ans<<endl;
		ans=0;
	}
	return 0;
}
