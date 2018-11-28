#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define fillchar(a,x) memset(a,x,sizeof(a))
int main()
{
    ofstream myfile;
    myfile.open("1.txt");

    int d,t,n;
    int s[100005],k[100005];

    scanf("%d",&t);

    for(int l=1;l<=t;l++)
    {
        scanf("%d %d",&d,&n);

        for(int i=0;i<n;i++)
        {
            scanf("%d %d",&k[i],&s[i]);
        }

        double maxel=0;

        for(int i=0;i<n;i++)
        {
            double temp=(double)(d-k[i])/(double)s[i];

            if(temp>maxel)
            maxel=temp;
        }

        double ans=(double)d/maxel;

        //printf("%lf\n",ans);
        myfile.precision(10);
        myfile<<"Case #"<<fixed<<l<<": "<<ans<<endl;
    }
	return 0;
}
