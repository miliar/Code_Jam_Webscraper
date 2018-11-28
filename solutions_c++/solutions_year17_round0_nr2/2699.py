#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define N 1000005
#define hg ios_base::sync_with_stdio(0);cin.tie(0)
#define ff first
#define ss second
#define gcd __gcd
#define inf (1<<30)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define all(xx) xx.begin(),xx.end()
#define bitcit __builtin_popcount
#define mset(x,y) memset(x,y,sizeof(x))
#define INF 1e18
#define PI acos(-1)
#define ll long long
#define endl "\n"

int main() {
    hg;
    int t,tt=1;
    int n,m;
    int i,j,k;
    int f=0,l;
    string s,ans;
    int temp;
    cin>>t;
    while(t--)
    {
    	cin>>s;
    	l=s.size();
    	ans="";
    	f=0;
    	for(i=l-1;i>0;i--)
    	{
    		if((s[i]-'0') < (s[i-1]-'0'))
    		{
    			if(i==1 && s[i-1]=='1')
    			{
    				f=1;
    				for(j=0;j<l-1;j++){
    					ans+='9';
    				}
    			}
    			else
    			{
    				temp=(s[i-1]-'0');
    				temp--;
    				s[i-1]=(temp+'0');
    				for(j=i;j<l;j++)
    				{
    					s[j]='9';
    				}
    			}
    		}
    		
    	}
    	cout<<"Case #"<<tt<<": ";
    	if(f)
    		cout<<ans<<"\n";
    	else
    		cout<<s<<"\n";
    	tt++;
    }
    
    
    return 0;
}