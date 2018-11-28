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

int main()
{
	int t;
	freopen("1.txt","r",stdin);
	freopen("a.out","w",stdout);
	cin >>t;
	rep(x,1,t+1)
	{
		double d,n;
		cin >>d>>n;
		vector<pair<double,double> > a(n);
		double max=0,mini=0;
		rep(i,0,n)
		{
			cin >>a[i].F>>a[i].S;
			if(a[i].F<d)
			{
				if(((d-a[i].F)/a[i].S)>max)
				{
					max=(d-a[i].F)/a[i].S;
					mini=i;
				}
			}
		}
		
	cout<<"Case #"<<x<<": "<<fixed<<setprecision(7)<<d/max<<endl;
	}
}
