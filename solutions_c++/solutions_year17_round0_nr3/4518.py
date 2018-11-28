#include <bits/stdc++.h>
using namespace std;
 
#define N 100005
#define fi first
#define se second
#define MOD 1000000007
 
#define pb push_back
 
#define ll long long
 
#define eps 1.0e-7
#define inf 1e9 + 5
#define double long double

#define pp pair<int,int>


int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t,i,n,m,k;
  string s ;

  cin>>t ;
  for(int i = 1; i <= t; i++)
  {
  	
  	cin>>n>>k;
  	map<int,int> mp;
  	mp[n]++;

  	for(int j = 0;j<k-1;j++)
  	{
  		auto it = mp.end();
  		it--;
  		int key = it->fi;
  		mp[key]--;
  		if(mp[key]==0) mp.erase(key);
  		if(key%2==0)
  		{
  			if(key/2- 1 > 0) mp[key/2 - 1]++;
  			if(key/2 > 0) mp[key/2]++;
  		}
  		else
  		{
  			if(key/2 > 0)
  			mp[key/2] += 2;
  		}
  		
  	}

  	int mx, mn;
  	auto it = mp.end();
  	it--;
  	int key = it->fi;

  	if(key%2==0)
  	{
  		mx = key/2;
  		mn = key/2 - 1;
  	}
  	else
  	{
  		mn = mx = key/2;
  	}
  	
  
    cout << "Case #" << i << ": "<<mx<<" "<<mn<<"\n";
    

    }



}