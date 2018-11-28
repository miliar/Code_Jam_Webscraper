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
#define ull unsigned long long int


int main()
{
	ull t;
	cin>>t;
	for(ull test=1;test<=t;test++)
	{
		ull n,k;
		cin>>n>>k;
		map<ull,ull> m;
		m[n]=1;
		cout<<"Case #"<<test<<": ";
		while(k>0)
		{
			map<ull,ull>::iterator it=m.end();
			it--;
			ull a=it->first,b=it->second;
			m.erase(it);
			if(b>=k)
			{
				if(a%2==0)
				{
					cout<<a/2<<" "<<a/2-1<<endl;
				}
				else
				{
					cout<<a/2<<" "<<a/2<<endl;
				}
				break;
			}
			else
			{
				if(a%2==0)
				{
					m[a/2]+=b;
					m[a/2-1]+=b;
				}
				else
				{
					m[a/2]+=b;
					m[a/2]+=b;
				}
				k-=b;
			}
		}
	}
}