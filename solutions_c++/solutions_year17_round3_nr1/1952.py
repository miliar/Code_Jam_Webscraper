#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mod 1000000007
#define inf 1e19  
vector<pair<double,double> > arr;
#define pi 3.1415926535
vector< int > vec;
int main() 
{
		// your code goes here
		freopen("input.in", "r", stdin);
       freopen("output.in" , "w" , stdout);
		double t,n,k,x,y;char s[10001];string str;
		cin>>t;
	for(int zz=1;zz<=t;zz++)
		{
				cout<<"Case #"<<zz<<": ";
		//	scanf(" %[^\n]s",s);
		arr.clear();	
		cin>>n>>k;
		for(int i=0;i<n;i++)
		{
			cin>>x>>y;
			arr.pb(make_pair(x,(2*pi*x*y)));
		}
		sort(arr.begin(),arr.end());
		reverse(arr.begin(),arr.end());
		if(k==1)
		{
			double ans=0,val=0;
			for(int i=0;i<n;i++)
			{
				ans=pow(arr[i].first,2)*pi+arr[i].second;
				val=max(val,ans);
				ans=0;
				//cout<<val<<" ";
			}
			cout<<fixed<<setprecision(10)<<val<<"\n";
			continue;
		}
		for(int i=0;i<k;i++)
		{
         	vec.pb(i);
		}
		

		for(int i=k;i<arr.size();i++)
		{
		     	double ans=0,val=inf;int p;
		
		   for(int j=0;j<k;j++)
		   {
		   
			if(j==0)ans+=((pow(arr[vec[j]].first,2)-pow(arr[vec[j+1]].first,2))*pi);
			ans+=arr[vec[j]].second;
			if(ans<val)
			{
				p=j;
				val=ans;ans=0;
			}
			ans=0;
		     }
		     ans=0;
		     ans+=arr[i].second;
		     if(val<ans)
		     {
		     	  vec.erase(vec.begin()+p);
		     	  vec.pb(i);
		     	  
		     }
		 
		}
		double ans=0;
		ans+=pow(arr[vec[0]].first,2)*pi;
		ans+=arr[vec[0]].second;
		for(int i=1;i<vec.size();i++)
		{
			ans+=arr[vec[i]].second;
		}
		
		cout<<fixed<<setprecision(10)<<ans<<"\n";vec.clear();
		  
	    }
	  return 0;
}

