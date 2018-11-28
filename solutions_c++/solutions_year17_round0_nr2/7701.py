#include<bits/stdc++.h>

#define vi vector <int>
#define vlli vector <long long>

#define pb push_back
#define mp make_pair

#define ff first
#define ss second

#define foreach(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define all(x) x.begin(),x.end()

#define ll long long

#define INF 3f3f3f3f
#define MOD 1000000007
#define MAXN 1005
using namespace std;

int isvalid(string a)
{
	for(int i=1;i<a.size();i++)
	{
		if(a[i-1]>a[i])
		 return 0;
	}
	return 1;
}
int main()
{
	//N = 1002;
	freopen("B-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
    
	int T;
	scanf("%d",&T);
	int t=1;
	while(T--)
	{
		printf("Case #%d: ",t++);
		string s;
		cin >> s;
		if(s.size()==1)
		{
			cout  << s << endl;
			continue;
		}
		for(int i=0;i<s.size();i++)
		 s[i]=s[i]-'0';
		
		long long ans =0;
		for(int i=0;i<s.size()-1;i++)
	     ans = ans * 10 +9;
	     
	    string temps=s;
	    long long tempans1=0;
		for(int j=0;j<s.size();j++)
		{
					tempans1 = tempans1 * 10 + temps[j]; 
		}
				
		if(isvalid(temps))
			ans = max(ans,tempans1);
		   
	    for(int  i=s.size()-1;i>=0;i--)
	    {
	    	if(s[i]==0)
	    	{
	    		
			}
			else 
			{
				temps[i] = s[i]-1;
				for(int j=i+1;j<s.size();j++)
				 temps[j] = 9;
				long long tempans=0;
				for(int j=0;j<s.size();j++)
				{
					tempans = tempans * 10 + temps[j]; 
				}
				if(isvalid(temps))
				ans = max(ans,tempans);
			}
			temps= s;
		}
		cout << ans << endl;
	}
	
	return 0;
}
