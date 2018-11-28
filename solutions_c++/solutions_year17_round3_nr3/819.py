#include<bits/stdc++.h>
using namespace std;
double yy[110];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int t;
	cin>>t;

	int n,k;



	for(int trm=1;trm<=t;trm++)
	{
		cout<<"Case #"<<trm<<": ";

        cin>>n>>k;

        double u;
        cin>>u;

        double rr;

        double fans=0;

        for(int i=0;i<n;i++)
        {
            cin>>rr;
            yy[i]=rr;
        }

        sort(yy,yy+n);

        int kk;

        for(int i=n-1;i>=0;i--)
        {
            double xy=0;

            for(int j=0;j<=i;j++)
            {
                xy+=yy[j];
            }
            xy+=u;

            xy=min(xy,1.0*(i+1));

            double ans=1;

            for(int j=0;j<=i;j++)
            {
                ans=ans*(xy/(i+1));
            }

            xy/=(i+1);

            if(xy>=yy[i])
            {
                fans=ans;

                kk= i;
                break;
            }
        }

        for(int i=kk+1;i<n;i++)
        {
            fans*=yy[i];
        }

        cout<<fixed<<setprecision(10)<<fans<<endl;


	}
}
