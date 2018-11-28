#include <bits/stdc++.h>

using namespace std;







 typedef long long ll;
 ll c=0;







//vector<vector<int> > v;

int main()
{
  int t;
  cin >>t;
 for(int j=0;j<t;j++)
  {
  	string s;
  	cin >>s;
  	ll k;
  	cin >>k;
  	ll count =0;
  	int a[s.size()];
  	for(int i=0;i<s.size();i++)
  	{
  		if(s[i]=='-')
  			a[i]=0;
  		else if(s[i]=='+')
  			a[i]=1;
  		
  	}
  	for(int i=0;i<=s.size()-k;i++)
  	{
  		if(a[i]==0)
  		{
  			for(int j=0;j<k;j++)
  			{
  			a[i+j]=!a[i+j];
  	
  			}
		count++;

  		}

  	}


  bool pos=true;
  for(int i=0;i<s.size();i++)
  	{
  		if(!a[i])
  			pos=false;
  	}

if(pos)
cout <<"Case #"<<j+1<<": "<<count<<endl;
else
cout <<"Case #"<<j+1<<": "<<"IMPOSSIBLE"<<endl;

  }

	return 0;
}