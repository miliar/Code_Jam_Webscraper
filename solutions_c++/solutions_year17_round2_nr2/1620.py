#include<bits/stdc++.h>
using namespace std;
#define pi pair<int,int>
#define mp make_pair
#define pb push_back

char ind(int i)
{	if(i==0)return 'R';
	if(i==1)return 'Y';
	if(i==2)return 'B';
}

int rev(char c)
{
	if(c=='R')return 0;
	if(c=='Y')return 1;
	if(c=='B')return 2;
}

int main()
{
	int t;
	cin>>t;
	int cased=1;
	while(t--)
	{	int n;
		cin>>n;
		int r,o,y,g,b,v;
		cin>>r>>o>>y>>g>>b>>v;
		vector<pi> arr;
		
		while(o)
		{	
		}
		
		
		arr.pb(mp(r,0));
		arr.pb(mp(y,1));
		arr.pb(mp(b,2));
		
		
		
		sort(arr.begin(),arr.end());
		
		int min1 = arr[0].first;
		string collect = "";
		string ans = "";
		collect += ind(arr[0].second);
		collect = ind(arr[1].second) + collect;
		collect = ind(arr[2].second) + collect;
		for(int i=0;i<min1;i++)
		{	ans += collect;
		}
		
		min1 = arr[1].first-arr[0].first;
		
		collect = "";
		collect +=  ind(arr[1].second);
		collect =  ind(arr[2].second) + collect;
		
		for(int i=0;i<min1;i++)ans+=collect;
		
		
		string str="";
		min1 = arr[2].first-arr[1].first;
		
		int size = ans.size()-1;
		
		for(int i=0;i<(size);i++)
		{	str +=  ans[i];
			if(rev(ans[i])!=arr[2].second and rev(ans[i+1])!= arr[2].second)
			{	if(min1>0)
				{	str += ind(arr[2].second);
					min1--;
				}
			}
		}
		
		if(ans.size()>0)str += ans[ans.size()-1];
		
		cout<<"Case #"<<cased<<": ";
		if(min1>0)
		{    cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{	cout<<str<<endl;	
		}
		cased++;
	}
	
	
}
