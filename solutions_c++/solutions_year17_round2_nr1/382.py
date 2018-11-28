#include<bits/stdc++.h>
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        int d,n;
        scanf("%d%d",&d,&n);
        double t=0.0;
        for(int i=0;i<n;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            t=max(t,1.0*(d-x)/y);
        }
        printf("Case #%d: %.8f\n",ti++,d/t);
    }
	return 0;
}
