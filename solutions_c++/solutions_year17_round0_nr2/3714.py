#include <bits/stdc++.h>
#define ll long long 
#define m 1000000007
using namespace std;

map<string ,ll>mp;
vector<string>v;
ll a[100000000];
void dfs(string x,ll y)
{ 
	if(x.length()==19)
	return ;
	v.push_back(x);
	if(y<=1)
	{ 
	//v.push_back(x+"1");	
	dfs(x+"1",1);
	}
	if(y<=2)
	{ 
	//v.push_back(x+"2");	
	dfs(x+"2",2);
	}
	if(y<=3)
	{ 
	//v.push_back(x+"3");	
	dfs(x+"3",3);
	}
	if(y<=4)
	{ 
//	v.push_back(x+"4");	
	dfs(x+"4",4);
	}
	if(y<=5)
	{ 
//	v.push_back(x+"5");	
	dfs(x+"5",5);
	}
	if(y<=6)
	{ 
//	v.push_back(x+"6");	
	dfs(x+"6",6);
	}
	if(y<=7)
	{ 
//	v.push_back(x+"7");	
	dfs(x+"7",7);
	}
	if(y<=8)
	{ 
//	v.push_back(x+"8");	
	dfs(x+"8",8);
	}
	if(y<=9)
	{ 
//	v.push_back(x+"9");	
	dfs(x+"9",9);
	}
	
	 
	}
int main() {
	// your code goes here
	std::ios::sync_with_stdio(false);
	ll i;
	
/*	v.push_back("1");
	v.push_back("2");
	v.push_back("3");
	v.push_back("4");
	v.push_back("5");
	v.push_back("6");
	v.push_back("7");
	v.push_back("8");
	v.push_back("9");*/
	
	dfs("1",1);
	dfs("2",2);
	dfs("3",3);
	dfs("4",4);
	dfs("5",5);
	dfs("6",6);
	dfs("7",7);
	dfs("8",8);
	dfs("9",9);
	
//cout<<s.size();
//for(std::set<string >::iterator it=s.begin();it!=s.end();it++)
//sort(v.begin(),v.end());
for(i=0;i<v.size();i++)
{
	string c=v[i];
	ll n=c.length(),k=0;
	
	ll x=1;
	for(ll j=n-1;j>=0;j--)
	{
		k+=((c[j]-48)*x);
		x=x*10;
		
		
	}
	a[i]=k;
	
}
//cout<<v.size();
//cout<<v[v.size()-1];
sort(a,a+v.size());
ll n,j=1;
cin>>n;
while(n--)
{ll y,ans;
cin>>y;
ll l=0, h =4686823;
while(l<=h)
{
	ll mid=(l+h)/2;
	if(a[mid]<=y)
	{
		ans=a[mid];
		l=mid+1;
	}
	else
	h=mid-1;
} 
cout<<"Case #"<<j<<": "<<ans<<endl;
j++;
}

	return 0;
}
