#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
#define For(i,a,b) for(int i=a;i<b;i++)
#define test() ull t;cin>>t;while(t--)
#define pb push_back
#define mkp make_pair
#define Vint vector<int>
#define Vull vector<ull>
#define tn ull n;cin>>n
#define nl cout<<endl
#define tnm ull n,m;cin>>n>>m
#define MOD 1000000007

ull ch(ull n)
{
    ull rem,divi,i=0;
    ull ans=n;
    while(n>0)
    {
        ull dig=pow(10,i);
        rem=n%10;
        divi=(n/10)%10;
        if(divi>rem)
        {
            ans-=(rem*dig+1);
            n=ans;
            //cout<<divi<<" "<<rem<<" "<<ans<<endl;
        }
        n/=10;
        i++;
    }
    return ans;
}
int main()
{
    ull t;
    cin>>t;
	for(int i=0;i<t;i++)
    {
        ull n,ans=0;
        cin>>n;
        ans=ch(n);
        cout<<"Case #"<<i+1<<": "<<ans;
        nl;
    }

	return 0;
}
