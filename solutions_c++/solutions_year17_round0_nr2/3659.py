#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include<string>
#include<cstring>
#include<utility>
#include<set>
#include<cstdlib>
#include <algorithm>
using namespace std;
#define ll long long
vector<int> arr;
void fill(ll n)
{
      while(n>0)
	  {
	  	arr.push_back(n%10);
	  	n/=10;
	  }	
}
int main() 
{
		// your code goes here
		freopen("input.in", "r", stdin);
       freopen("output.in" , "w" , stdout);
		ll t,n,p,ans;
		cin>>t;
	for(int zz=1;zz<=t;zz++)
		{
		//	scanf(" %[^\n]s",s);
		cout<<"Case #"<<zz<<": ";
		cin>>n;
		fill(n);
		if(arr.size()<=1)
		{
			cout<<n<<"\n";arr.clear();continue;
		}
		p=arr[arr.size()-1];int flag=0;
		  for(int i=arr.size()-2;i>=0;i--)
		  {
		  	if(flag==1) arr[i]=9;
		  	else if(arr[i]>=p)
		  	{
		  		p=arr[i];
		  	}
		  	else
		  	{
		  		arr[i]=9;flag=1;
		  		arr[i+1]--;
		  		int j=i+2;
		  		while(j<arr.size()&&arr[j]>arr[j-1])
		  		{
		  			arr[j]--;
		  			arr[j-1]=9;
		  			j++;
		  		}
		  	}
		  }
		  ans=0;
		  for(int i=arr.size()-1;i>=0;i--)
		  {
		  	ans=ans*10+arr[i];
		  }
		  cout<<ans<<"\n";
		  arr.clear();
	    }
	  return 0;
}

