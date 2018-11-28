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

int main()
{
    long long t,c,k,i,n,cl,cr,clp,crp,l,r,l1,r1,l2,r2;
    cin>>t;
    bool flag;
    for(int z=1;z<=t;z++)
    {
        cin>>n>>k;
        l=r=n/2;
        if(n%2==0)
        {
            r--;
            cl=clp=crp=cr=1;
        }
        else
        {
            cl=clp=2;
            cr=crp=0;
        }
        if(k!=1)
        {
            c=1;
            flag=0;
            while(c<=n)
            {
                cl=clp;
                cr=0;
                l1=r1=l/2;
                if(l%2==0)
                    r1--;
                l2=r2=r/2;
                if(r%2==0)
                    r2--;
                c+=clp;
                if(k<=c)
                {
                    l=l1;
                    r=r1;
                    flag=1;
                    break;
                }
                c+=crp;
                if(k<=c)
                {
                    l=l2;
                    r=r2;
                    flag=1;
                    break;
                }
                if(r1==l1)
                    cl+=clp;
                else
                    cr+=clp;
                if(l2==l1)
                    cl+=crp;
                else
                    cr+=crp;
                if(r2==l1)
                    cl+=crp;
                else
                    cr+=crp;
                clp=cl;
                crp=cr;
                l=max(l1,l2);
                r=min(r1,r2);
            }
        }
        cout<<"Case #"<<z<<": "<<l<<" "<<r<<endl;
    }
    return 0;
}
