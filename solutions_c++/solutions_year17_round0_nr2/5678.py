#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string.h>
using namespace std;
#define ll long long int
int main() {
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int cases=1;cases<=t;++cases)
    {
        ll n;
        cin>>n;
        ll anum[32], len=0;
        memset(anum,0,sizeof(anum));
        ll numa = n;
        while(numa)
        {
        	ll d=numa%10;
            anum[len++]=d;
            numa/=10;
		}
        if(len>1)
        {
            for(int i=0;i<len-1;++i)
            {
                if(anum[i]<anum[i+1])
                {
                    anum[i]=9;
                    if(anum[i+1]==0)
                        anum[i+1]=9;
                    else
                        anum[i+1]--;
                    //i=-1;
                }
                else if(anum[i+1]==0)
                {
                    anum[i]=9;
                    //i=0;
                }
             }
            for(int i=len-2;i>=0;--i)
            {
                if(anum[i]<anum[i+1])
                {
                    anum[i]=9;
                }
            }
        }
        ll ans=0;
        for(int i=len-1;i>=0;--i)
        {
        	ans = ans*10 + anum[i];
        	//cout<<anum[i]<<" ";
		}
        cout<<"Case #"<<cases<<": "<<ans<<endl;
    }
  return 0;
}
