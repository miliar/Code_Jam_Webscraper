#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-largeoutput.out","w",stdout);
    long long int t,n,k,val,i,j,mini,maxi,maxi1;
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lld %lld",&n,&k);
        n=n+1;
        k=k-1;
        queue<long long int> q;
        map<long long int, long long int > m;
        q.push(n);
        m[n]=1;
        j=1;
        while(j<=k)
        {
            if(q.size()==0)
            break;
            val=q.front();
            if(j+m[val]>k+1)
            break;
            q.pop();
            if((val+1)/2!=1)
            {
                if(m[(val+1)/2]==0)
                q.push((val+1)/2);
                m[(val+1)/2]+=m[val];
            }
            if(val/2!=1)
            {
                if(m[val/2]==0)
                q.push(val/2);
                m[val/2]+=m[val];
            }
            j+=m[val];
            m[val]=0;
        }
        if(q.size()==0)
        {
            mini=0;
            maxi=0;
        }
        else
        {
            maxi1=0;
            while(!q.empty())
            {
                val=q.front();
                if(val>maxi1)
                maxi1=val;
                q.pop();
            }
            mini=maxi1/2-1;
            maxi=(maxi1+1)/2-1;
        }
        //printf("%lld %lld %lld\n",mini,maxi,maxi1);
        printf("Case #%lld: %lld %lld\n",i,maxi,mini);
    }
	return 0;
}
