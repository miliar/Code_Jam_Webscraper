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
    freopen("input_2.txt", "r", stdin);
    freopen("output_2.txt", "w", stdout);

    int test;
   	int ans=0;
   	string s;
   	int i,j,k,n;
    cin>>test;
    bool check;
    for(int t=1;t<=test;t++)
    {
        cin>>s;
        n=s.length();
       	for(i=n-1;i>0;i--)
       	{
       		if(s[i]<s[i-1])
       		{
       			s[i-1]--;
       			for(j=i;j<n;j++)
       				s[j]='9';
       		}
       	}
        while(*(s.begin())=='0')
        	s.erase(s.begin());
        cout<<"Case #"<<t<<": "<<s<<endl;
       
    }
    return 0;
}

