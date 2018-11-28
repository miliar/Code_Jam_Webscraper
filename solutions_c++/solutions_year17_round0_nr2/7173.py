#include<bits/stdc++.h>
#define ll long long
#define cases int t;  cin>>t;   while(t--)
ll mod =1e9+7;
template<typename T> 
inline ll pwr(T base,T n){ll ans=1;while(n>0){ if(n%2==1)ans=ans*base;  base=base*base; n/=2;} return ans;}
struct range{int l,h;}; 
using namespace std;
int main()
{
ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin>>t;
    int k=0;
    while(k<t)
    { ll int n;
        cin>>n;
        
        ll int a=0;
        
        int i=0;
        int p,r,prev=0;
        int last=-1;
        if(n/10==0){cout<<"Case#"<<k+1<<": "<<n<<"\n";k++;continue;}
        ll q=n;
        while(n)
        {
        if(i==0)
        {
            p=n%10;
            n/=10;
            i++;
        }
        else
        {
        r=n%10;
        if(r>p)last=i;
        if(r==p && i-last==1)last=i;
        n/=10;
        p=r;
        i++;
        }
        }
        int l=last;
        cout<<"Case#"<<k+1<<": ";    
        ll int z=0;
        if(last>0)
        {while(last--)q/=10;
        q--;}
        if(q || l==-1)cout<<q;
        for(int j=0;j<l;j++)cout<<'9';
        cout<<"\n";
        k++;
    }
    return 0;
}