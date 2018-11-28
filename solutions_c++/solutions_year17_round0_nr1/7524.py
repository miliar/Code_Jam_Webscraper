#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<list>
#include<cmath>
#include<map>
#include<queue>
#include<stack>
#include<algorithm>
#include<set>
#include<complex>

using namespace std;

typedef long long ll;

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pii pair<ll,ll>
#define pll pair<ll,ll>
#define sc(t) scanf("%d",&t)
#define G getchar_unlocked
#define P putchar_unlocked
const ll K=1000000000000000007LL;
const ll N=750005;

inline ll inp()
{
    ll x=0;
    char c;
    while((c=G())<'0'||c>'9');
    while(c>='0'&&c<='9')
        x=(x<<1)+(x<<3)+c-'0',c=G();
    return x;
}

inline ll power(ll n,ll p,ll k)
{
    ll x=1;
    
    while(p){
        if(p%2)    x=(x*n)%k;
        if(p/=2)    n=(n*n)%k;
    }
    
    return x;
}

ll gcd(ll a,ll b)
{
    if(a<b)
        a=a+b,b=a-b,a=a-b;
    
    ll x;
    
    while(a%b)
        x=a%b,a=b,b=x;
    
    return b;
}

int main()
{
    int t,tc;
    t = 1;
    
    for(scanf("%d",&t),tc=1;tc<=t;tc++){
        
        ll n,i,j,k,flag=1,ans=0;
        string s;
        cin>>s>>k;
        
        for(i=0;i+k<=s.length();i++){
            if(s[i]=='-'){
                for(j=0;j<k;j++)
                    switch(s[i+j]){
                        case '+':
                            s[i+j]='-';
                            break;
                        case '-':
                            s[i+j]='+';
                            break;
                    }
                ans++;
            }
        }
        
        for(;i<s.length();i++)
            if(s[i]=='-')   flag = 0;
        cout<<"Case #"<<tc<<": ";
        if(flag)
            cout<<ans<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    
    return 0;
}
