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
    int l=0;
    while(l<t)
    {
        string s;
        cin>>s;
        
        int a[s.size()];
        
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')a[i]=0;
            else a[i]=1;
        }
        
        //for(int i=0;i<s.size();i++)cout<<a[i];
        
        int k;
        cin>>k;
        int sum=0,flag=0;
        for(int i=0;i<=s.size()-k;i++)
        {
            if(a[i]==0)
            {
                sum++;
                for(int j=i;j<i+k;j++)
                if(a[j]==0)a[j]=1;
                else a[j]=0;
            }
        }
        
        for(int i=0;i<s.size();i++)
        {
            if(a[i]==0){flag=1;break;}
        }
        //for(int i=0;i<s.size();i++)cout<<a[i];
        cout<<"Case #"<<l+1<<": ";
        if(flag==0)cout<<sum<<"\n";
        else cout<<"IMPOSSIBLE\n";
        l++;
    }
    return 0;
}