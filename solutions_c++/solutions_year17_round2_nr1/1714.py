#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        int d,n;
        scanf("%d %d",&d,&n);
        double mins=0.0;
        int mxd=0;
        int mxs=0;
        for(int i=0;i<n;i++)
        {
            int k,s;
            scanf("%d %d",&k,&s);
            if(1.0*(d-k)/s>mins)
            {
                mins=1.0*(d-k)/s;
            }
        }
        printf("Case #%d: %.6f\n",T,1.0*d/mins);
    }
    //cout << "Hello world!" << endl;
    return 0;
}
