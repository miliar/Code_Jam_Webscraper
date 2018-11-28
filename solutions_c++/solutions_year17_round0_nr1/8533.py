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
int main()
{
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
 ios_base::sync_with_stdio(false);
 cin.tie(NULL);
 int t,tc;
 cin>>tc;
 for(t=0;t<tc;t++)
 {
    string s;
    int k;
    cin>>s>>k;
    int i=0;
    int ans=0;
    int flag=0;
    int j;
    while(i<s.length()&&flag==0)
    {
        if(s[i]=='-')
        {
           if(i+k-1<s.length())
           {
             for(j=i;j<i+k;j++)
             {
                if(s[j]=='+')
                  s[j]='-';
                else if(s[j]=='-')
                    s[j]='+';
             }
             ans++;
             i++;
           }
           else
           {
            flag=1;
           }
        }
        else if(s[i]=='+')
        {
           i++;
        }
    }
    if(flag==0)
        cout<<"Case #"<<(t+1)<<": "<<ans<<"\n";
    else
       cout<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<"\n"; 
 }
    return 0;
}
