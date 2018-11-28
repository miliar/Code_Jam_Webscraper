#include<bits/stdc++.h>
#define MAX 100100
#define mod 1000000007
#define MS0(x) memset(x, 0, sizeof(x))
#define ll long long int
#define in(x) scanf("%I64d", &x)
#define ind(x) scanf("%d", &x)
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pid pair<int,double>
#define pii pair<int,int>
#define p_q priority_queue
#define gcd(a,b) __gcd(a,b)
using namespace std;
string to_string(int x)
{
    string s="";
    while(x!=0)
    {
        int d=x%10;
        s+=d+'0';
        x/=10;
    }
    reverse(s.begin(),s.end());
    return s;
}
int fun(int x)
{
    string s=to_string(x);
    //cout<<s<<"\n";
    int i;
    for(i=0;i<s.length();i++)
      {
        if(s[i]=='0')
            return 0;
    }
    for(i=1;i<s.length();i++)
    {
         if(s[i]-s[i-1]<0)
            return 0;
    }
    return 1;
}
int main()
{
        freopen("input.txt","r",stdin);
        freopen("out.txt","w",stdout);
 ios_base::sync_with_stdio(false);
 cin.tie(NULL);
 int t,tc;
 cin>>tc;
 for(t=0;t<tc;t++)
 {
    int n,i;
    cin>>n;
    int ans=0;
    for(i=n;i>=1;i--)
    {
        if(fun(i)==1)
        {
            ans=i;
            break;
        }
       
    }
     cout<<"Case #"<<(t+1)<<": "<<ans<<"\n"; 
 }
    return 0;
}
