// Lavina Jain
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define INF 1e20
#define MAX 1000000007
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL);
#define cases int t; cin>>t; while(t--)

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

bool func(int n)
{
    int prev=9,num;
    while(n>0)
    {
        num=n%10;
        n=n/10;
        if(num>prev)
            return false;
        prev=num;
    }
    return true;
}

int main()
{
    int t,n,i,ans;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        cin>>n;
        for(i=n;i>0;i--)
        {
            if(func(i))
            {
                ans=i;
                break;
            }
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }
    return 0;
}
