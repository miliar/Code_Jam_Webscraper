#include<bits/stdc++.h>

using namespace std;

int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k,t;

    scanf("%d",&t);

    int D,N;



    int u1,u2;

    for(int kk1=1;kk1<=t;kk1++)
    {
        double aa[1000+9];
        scanf("%d %d",&D,&N);

        for(i=0;i<N;i++)
        {
            scanf("%d %d",&u1,&u2);

            double ans;
            ans = (double)(D-u1);
        //    cout<<ans<<endl;
            ans = (double)ans/(double)(u2);
         //   cout<<ans<<endl;

            aa[i]=ans;
        }

        sort(aa,aa+N);

        //Case #1:
        printf("Case #%d: ",kk1);
        double fans;
        fans=(double)D/(double)aa[N-1];

        printf("%.9f\n",fans);




    }



}
