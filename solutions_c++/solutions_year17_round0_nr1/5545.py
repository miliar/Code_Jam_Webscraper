#include <bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  cin>>t;
  int a[105],l=1;
  while(t--)
  {
  	map<string, bool> mp;
  	string s,t,m;
  	int i,k,j;
  	map<string,int> dis;
  	cin>>s>>k;
  	queue<string> q;
  	for(i=0;i<s.size();i++)
  		t+='+';
  	if(s==t)
  	{
  		a[l]=0;l++;
  		continue;
  	}
  	else
  	{
  		q.push(s);
  		dis[s]=0;
  		mp[s]=true;
  		while(!q.empty())
  		{
  			m=q.front();
  			q.pop();
  		
  			for(i=0;i<=m.size()-k;i++)
  			{
  				s=m;
  				for(j=i;j<i+k;j++)
  				{
  					if(s[j]=='+')
  						s[j]='-';
  					else s[j]='+';
  				}
  				if(mp[s]==false)
  				{

  					q.push(s);
  					mp[s]=true;
  					dis[s]=dis[m]+1;
  				}
  			}
  		}
  	}
  	if(mp[t]==true)
  	{
  		a[l]=dis[t];l++;
  	}
  	else 
  	{
  		a[l]=-1;l++;
  	}
  }
  for(int i=1;i<l;i++)
  {
  	if(a[i]==-1)
  		cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
  	else
  		cout<<"Case #"<<i<<": "<<a[i]<<endl;
  }
}

