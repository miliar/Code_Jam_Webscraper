#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back


vector<pair<double,double> > vec;
int main() 
{
		// your code goes here
		freopen("input.in", "r", stdin);
       freopen("output.in" , "w" , stdout);
		ll t,n,k,v,d;char s[10001];string str;double p,q,r;
		cin>>t;
	for(int zz=1;zz<=t;zz++)
		{
				cout<<"Case #"<<zz<<": ";
		//	scanf(" %[^\n]s",s);
		cin>>d>>n;
		for(int i=0;i<n;i++)
		{
			cin>>k>>v;
			vec.push_back(make_pair(k,v));
		}
		sort(vec.begin(),vec.end());
		p=(d-vec[0].first)/vec[0].second;
		q=vec[0].second;r=vec[0].first;
		for(int i=1;i<n;i++)
		{
			while(i<n&&vec[i].second>=q)i++;
			if(i==n)break;
			if((vec[i].first-r)/(q-vec[i].second)>=(d-vec[i].first)/vec[i].second);
			else
			{
				p=(d-vec[i].first)/vec[i].second;q=vec[i].second;r=vec[i].first;
			}
		
			
		}
	 double ans;
	 ans=d/p;
	   cout<<fixed<<setprecision(9)<<ans<<"\n";
	   vec.clear();
		  
	    }
	  return 0;
}

