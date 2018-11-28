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
   	int i,j,k,n,r,c;
   	string a[50];
    cin>>test;
    bool check;
    for(int t=1;t<=test;t++)
    {
        cin>>r>>c;
        for(int i=0;i<r;i++)
        {
        	cin>>a[i];
        	int s=0;
        	for(int j=0;j<c;j++)
        	{
        		if(a[i][j]!='?')
        		{

        			while((a[i][s] == '?' || a[i][s]==a[i][j]) && s<c)
        			{
        				a[i][s]=a[i][j];
        				s++;
        			}
        			j=s-1;
        		}
        	}
        }


        int s=0;
    	for(int j=0;j<r;j++)
    	{
    		if(a[j][0]!='?')
    		{

    			while((a[s][0] == '?' || a[s][0]==a[j][0]) && s<r)
    			{
    				a[s]=a[j];
    				s++;
    			}
    			j=s-1;
    		}
    	}

        cout<<"Case #"<<t<<": "<<endl;

        for(int i=0;i<r;i++)
        	cout<<a[i]<<endl;

    }
    return 0;
}

