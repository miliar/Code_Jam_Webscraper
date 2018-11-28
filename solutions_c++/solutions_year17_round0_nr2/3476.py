#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <math.h>
#include <map>
#include <queue>
#include <algorithm>
#include <list>

using namespace std;


#define ll long long int
#define umm(x,y) unordered_map<x,y >
#define pb push_back
#define foi(n) for(int i=0;i<n;i++)
#define foj(n) for(int j=0;j<n;j++)
#define foi1(n) for(int i=1;i<=n;i++)
#define vi vector<int>
#define vvi vector<vi >
#define vll vector<ll>
#define vvll vector<vll >
#define si size()


vi tidy;

bool is_tidy(int n)
{
	int curr=n%10;
	while(n!=0)
	{
		if(n%10>curr)return false;
		curr=n%10;
		n/=10;
	}
	return true;
}

int main()
{
	foi1(1000)if(is_tidy(i))tidy.pb(i);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		int n;
		cin>>n;
		cout<<"Case #"<<test<<": ";
		for(int i=tidy.size()-1;i>=0;i--)
		{
			if(tidy[i]<=n)
			{
				cout<<tidy[i]<<endl;
				break;
			}
		}
	}
}