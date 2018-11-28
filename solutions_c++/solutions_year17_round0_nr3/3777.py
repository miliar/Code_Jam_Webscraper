#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
vector< vector< pair<ll,ll> > > arr;
ll power_of_two[100];
void helping()
{
    power_of_two[0]=1;
	for(int i=1;i<=60;i++)
	{
		power_of_two[i]=power_of_two[i-1]+pow(2,i);
		//cout<<i<<" "<<power_of_two[i]<<"\n";
	}	
}
int find_level(ll x)
{
	int i=0,j=60,mid=(i+j)/2;
	while(i<j)
	{
		if(power_of_two[mid]==x)
		{
			return mid;
		}
		else if(power_of_two[mid]<x)
		{
			i=mid+1;
		}
		else 
		{
			j=mid;
		}
		mid=(i+j)/2;
	}
	return mid;
	
}
void fill_arr(ll x)
{
	int j=0;
	vector<pair<ll,ll> > vec;
	vec.push_back(make_pair(x,1));
	arr.push_back(vec);vec.clear();j++;
	while(arr[j-1][0].first>1)
	{
		ll x,y,w=0,n=0,z,m;
		x=arr[j-1][0].first;y=arr[j-1][0].second;
		if(x&1)
		{
		   z=x/2; w=y*2;	
		}
		else
		{
		   w=y;n=y;	z=(x/2);m=(x/2)-1;
		}
		if(arr[j-1].size()>1)
		{
			
			x=arr[j-1][1].first;y=arr[j-1][1].second;
		if(x&1)
		{
			n+=y*2;m=(x/2);
		}
		else
		{
			w+=y;n+=y;m=(x/2)-1;z=(x/2);	
		}
		
		vec.push_back(make_pair(z,w));	vec.push_back(make_pair(m,n));
		arr.push_back(vec);vec.clear();
		
		
		}
		else
		{
			x=arr[j-1][0].first;
		  if(x&1){
		  vec.push_back(make_pair(z,w));arr.push_back(vec);vec.clear();}
		  else
		  {
		  	vec.push_back(make_pair(z,w));	vec.push_back(make_pair(m,n));
		arr.push_back(vec);vec.clear();
		  }
	    }
	    j++;
	}
	
	
}
int main() 
{
		// your code goes here
		freopen("input.in", "r", stdin);
       freopen("output.in" , "w" , stdout);
		ll t,n,p,k;
		cin>>t; helping();
		//cout<<find_level(2)<<" "<<find_level(3)<<" "<<find_level(5)<<" ";
	for(int zz=1;zz<=t;zz++)
		{
			cout<<"Case #"<<zz<<": ";
		//	scanf(" %[^\n]s",s);
		  cin>>n>>k;
		  fill_arr(n);
		  p=find_level(k);
		  if(p==0)
		  {
		  	if(n&1)
		  	cout<<(n/2)<<" "<<n/2<<"\n";
		  	else
		  	{
		  	   cout<<(n/2)<<" "<<(n/2)-1<<"\n";	
		  	}
		  }
		  else
		  {
		  	ll x,y;
		  x=k-power_of_two[p-1];
		  y=arr[p][0].second;
		  if(y>=x)
		  {
		  	y=arr[p][0].first;
		  	if(y&1)
		  	cout<<(y/2)<<" "<<y/2<<"\n";
		  	else
		  	{
		  	   cout<<(y/2)<<" "<<(y/2)-1<<"\n";	
		  	}
		  }
		  else
		  {
		  	y=arr[p][1].first;
		  	if(y&1)
		  	cout<<(y/2)<<" "<<y/2<<"\n";
		  	else
		  	{
		  	   cout<<(y/2)<<" "<<(y/2)-1<<"\n";	
		  	}
		  }
	      }      
		  arr.clear();
	    }
	  return 0;
}

