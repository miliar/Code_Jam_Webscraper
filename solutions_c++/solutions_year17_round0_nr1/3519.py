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

vector<char> vec;

void flip(int x, int k)
{
	for(int i=x;i<x+k;i++)
	{
		if(vec[i]=='-')vec[i]='+';
			else vec[i]='-';
	}
	return;
}

bool check()
{
	foi(vec.size())if(vec[i]=='-')return false;
	return true;
}


int main()
{
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		string s;
		int k;
		cin>>s>>k;
		vec.resize(s.length());
		foi(s.length())vec[i]=s[i];
		int count1=0,count2=0;
		for(int i=0;i<vec.size()+1-k;i++)
		{
			if(vec[i]=='-')
			{
				flip(i,k);
				count1++;
			}
		}
		cout<<"Case #"<<test<<": ";
		if(check())cout<<count1<<endl;
		else cout<<"IMPOSSIBLE"<<endl;


	}
}