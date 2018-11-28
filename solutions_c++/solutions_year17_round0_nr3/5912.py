#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
#define ll long long int


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int cases=1;cases<=t;++cases)
    {
        ll n,k;
        cin>>n>>k;
        ll LR[n][2], O[n];
        memset(O,0,sizeof(O));
        ll ans1 = 0, ans2 = 0;
        for(int i=0;i<k;++i)
        {
            memset(LR,0,sizeof(LR));
            ll max_minLR=0;
            for(int j=0;j<n;++j)
            {
                if(O[j]!=1)
                {
                    int L=0,R=0;
                    for(int l=j-1;l>=0 && O[l]!=1;--l)
                        L++;
                    for(int l=j+1;l<n && O[l]!=1;++l)
                        R++;
                   LR[j][0] = L;
                   LR[j][1] = R;
                   if(min(L,R) > max_minLR)
                       max_minLR = min(L,R); 
                   
                }
            }
            int occupy = 0, max_maxLR = -1;
            for(int j=0;j<n;++j)
            {
                if(O[j]!=1)
                {
                    //cout<<j<<" ";
                    if(min(LR[j][0],LR[j][1])==max_minLR)
                    {
                        if(max(LR[j][0],LR[j][1]) > max_maxLR)
                        {
                            max_maxLR = max(LR[j][0],LR[j][1]);
                            occupy = j;                            
                        }
                    }
                }
            }
            O[occupy] = 1;
            ans1 = max_maxLR;
            ans2 =max_minLR;
            //cout<<"! ";
            //cout<<occupy+1<<"\n";
        }
        cout<<"Case #"<<cases<<": "<<ans1<<" "<<ans2<<endl;
    }
}