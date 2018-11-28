#include <bits/stdc++.h>
 
#define long long long int
using namespace std;
 
#define Max 100005+5
#define cons 1000000000+7
#define mp make_pair
#define pb push_back
#define INF 1e12
#define INF2 1e9+9
#define pi 3.141592653589
#define x first
#define y second
 

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;cin>>t;
    int case_No=0;

    while(t--)
    {
    	case_No++;
    	char s[2000];
    	cin>>s;
    	int k;cin>>k;
    	int x=strlen(s);

    	int ans=0;
    	bool flag=true;

    	for(int i=0;i<x;i++)
    	{
    		if(s[i]=='-')
    		{

    			if(x-i<k)
    			{
    				flag=false;
    				break;
    			}
    			else
    			{
    				ans++;
    				for(int j=i;j<i+k;j++)
    				{
    					if(s[j]=='-')s[j]='+';
    					else s[j]='-';
    				}
    			}
    		}
    	}
    	cout<<"Case #"<<case_No<<": ";
    	if(flag)
    		cout<<ans<<"\n";
    	else cout<<"IMPOSSIBLE"<<"\n";
    }
    return 0;
}