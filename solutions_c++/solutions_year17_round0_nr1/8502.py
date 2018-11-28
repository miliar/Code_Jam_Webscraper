/*
deepansh_946
*/
#include<bits/stdc++.h>
#define gc getchar
#define pc putchar
#define lli long long int
#define MOD 1000000007
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define pd(x) printf("%d",x)
#define plld(x) printf("%lld",x)
#define ss(x) scanf("%s",&x)
#define ps(x) printf("%s",x)
#define code int t; cin>>t; while(t--)
#define gcd __gcd
#define INF LLONG_MAX
using namespace std;

bool ans(string s,int n,int l,int j1)
{
    int i=0 , j , k , temp , temp1=0;
    int count1 = 0;
    while(i<n)
    {
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                if( i >=(n-l+1) )
                {
                    cout<<"Case #"<<j1<<": "<<"IMPOSSIBLE"<<endl;
                    temp1 = 1;
                    break;
                }
                j = i;
                while(j<i+l)
                {
                    if(s[j]=='+')
                    {
                        s[j]='-';
                    }
                    else
                    {
                        s[j]='+';
                    }
                    j++;
                }
                count1++;
            }
        }
        if(temp1==1)
        {
            break;
        }
    }
    if(temp1!=1)
    {
        cout<<"Case #"<<j1<<": "<<count1<<endl;
    }
    return false;
}

int main()
{
    freopen("in.in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        string s;
        cin >> s;
        int l;
        cin >> l;
        bool che = ans(s , s.size() , l , i);
    }
}
