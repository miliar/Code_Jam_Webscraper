#include <bits/stdc++.h>
using namespace std;

int main() {
    int t,n,i,j,c=1,k;
    cin>>t;
    while(t>0)
    {
        cout<<"Case #"<<c<<": ";
        ++c;
        cin>>n>>k;
        long double u,ar[n],x;
        cin>>u;
        for(i=0;i<n;++i)
        cin>>ar[i];
        
        
    
        while(u>0)
        {
            
            sort(ar,ar+n);
            x=ar[0];
            for(i=1;i<n;++i)
            if(ar[i]!=x)
            break;
            
            if(i==n)
            {
                
                x=u/n;
                for(i=0;i<n;++i)
                ar[i]=ar[i]+x;
                break;
            }
            
            else
            {
                if((ar[i]-ar[0])*(i)<u)
                {
                    u=u-(ar[i]-ar[0])*(i);
                    x=ar[0];
                    for(j=0;j<i;++j)
                    ar[j]=ar[i];
                }
                else
                {
                    x=u/(i);
                    for(j=0;j<i;++j)
                    ar[j]=ar[j]+x;
                    break;
                }
            }
        }
        long double ans=1.0;
        for(i=0;i<n;++i)
        ans=ans*ar[i];
        printf("%.9Lf\n",ans);
        
        --t;
    }
	return 0;
}

