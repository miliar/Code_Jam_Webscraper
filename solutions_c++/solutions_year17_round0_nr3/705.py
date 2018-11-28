#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
using namespace std;

int t;
long long n,k;
long long ans1,ans2;
map<long long,long long>mp;
map<long long,long long>::iterator it;
int main()
{
    int i,j,times;
    freopen("C-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    
    cin>>t;
    //cout<<t<<' '<<"!!!!"<<endl;
    
    for(times=1;times<=t;times++)
    {
        cin>>n>>k;
        mp.clear();
        mp[n]=1;
        
        //cout<<n<<' '<<k<<endl;
        
        while(true)
        {
            it=mp.end();
            it--;
            
            long long g,c;
            g=it->first;
            c=it->second;
            mp.erase(it);
            long long ll,rr;
            if(k<=c)
            {
                ans1=ans2=g/2;
                if(g%2==0)
                {
                    ans2--;
                }
                break;
            }
            
            ll=rr=g/2;
            if(g%2==0)
            {
                ll--;
            }
            
            if(mp.find(ll)!=mp.end())
            {
                mp[ll]+=c;
            }
            else
            {
                mp[ll]=c;
            }
            if(mp.find(rr)!=mp.end())
            {
                mp[rr]+=c;
            }
            else
            {
                mp[rr]=c;
            }
            
            k-=c;
        }
        
        cout<<"Case #"<<times<<": "<<ans1<<" "<<ans2<<endl;
    }
    
    
    return 0;
} 
