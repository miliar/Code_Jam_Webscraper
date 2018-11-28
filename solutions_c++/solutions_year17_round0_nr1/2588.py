#include <bits/stdc++.h>
using namespace std;

#define min(a,b) ((a<b) ? (a) : (b))
#define max(a,b) ((a>b) ? (a) : (b))
#define ll long long
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORL(i,n) for(long long i=0;i<n;i++)
#define MOD 1000000007
#define PI 3.141592653589
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);

int main()
{
    fastio
    freopen("input_1.txt", "r", stdin);
    freopen("output_1.txt", "w", stdout);

    int test;
   	int ans=0;
   	string s;
   	int i,j,k,n;
    cin>>test;
    bool check;
    for(int t=1;t<=test;t++)
    {
        cin>>s>>k;
        ans=0;
        check=true;
        n=s.length();
        FOR(i,n)
        {
        	if(s[i]=='-')
        	{
        		ans++;
        		//cout<<endl;
        		for(j=i;j<k+i;j++)
        		{
        			//cout<<j<<" ";
        			if(j>=n)
        			{
        				check=false;
        				break;
        			}
        			if(s[j]=='+')
        				s[j]='-';
        			else
        				s[j]='+';

        		}
        		if(!check)
        			break;
        	}
        }
        if(check)
        	cout<<"Case #"<<t<<": "<<ans<<endl;
        else
        	cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;

    }
    return 0;
}

