#include <bits/stdc++.h>
using namespace std;
main()
{
int t;
cin>>t;
int cas=1;
while(t--)
{
    long long n;
    cin>>n;
    string s = to_string(n);
    int len = s.length();
    int no[len];
    for(int i = 0;i<len;i++)
    {
        no[i] = s[i]-48;
    }
    int j=1;
    int ans[len];
    ans[0] = no[0];
    for(int i = 0;i<len-1;i++)
    {
        if(no[i]<=no[j])
    		{
    			ans[j] = no[j];
    			j++;
    		}
    		else{
    			int l = j-1;
    			ans[l]--;
    			while(ans[l]<ans[l-1]&&l-1>=0)
    			{
    				ans[l-1]--;
    				l--;
    			}
    			for(int k = l+1;k<len;k++)
    			{
    				ans[k] = 9;
    			}
    			break;
    		}
    }
    int i = 0;
    while(ans[i]==0)
    {
    	i++;
    }
    cout<<"Case #"<<cas<<": ";
    for(;i<len;i++) cout<<ans[i];
    cout<<endl;
    cas++;
    }
}
