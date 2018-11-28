#include <bits/stdc++.h>
using namespace std;
main()
{
int t;
cin>>t;
int cas=1;
while(t--)
{
    string s;
    int n;
    cin>>s>>n;
    int l = s.length();
    bool a[l];
    for(int i = 0;i<l;i++)
    {
    	if(s[i]=='+') a[i] = 1;
    	else a[i] = 0;
    }
    int ans = 0;
    for(int i = 0;i<l;i++)
    {
    	if(a[i]==0&&i+n<=l)
    	{
    		ans++;
    		for(int j = i;j<i+n;j++)
    		{
    			a[j] = !a[j];
    		}
    	}
    	else if(a[i]==0&&i+n>l)
    	{
    		ans++;
    		for(int j = l-1;j>=l-n;j--)
    		{
    			a[j] = !a[j];
    		}
    	}

    }
    int f = 0;
    for(int i = 0;i<l;i++)
    {
    	if(a[i]==0)
    	{
    		f = 1;
    		break;
    	}
    }
    if(f==1)
    {
    	cout<<"Case #"<<cas<<": IMPOSSIBLE"<<endl;
    }
    else
    {
    	cout<<"Case #"<<cas<<": "<<ans<<endl;
    }

    cas++;
    }
}
