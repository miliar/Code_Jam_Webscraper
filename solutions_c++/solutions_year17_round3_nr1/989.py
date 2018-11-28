#include<bits/stdc++.h>
using namespace std;
long long  r[1010],h[1010];
double pi = acos(-1);

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

        for(int i=0;i<n;i++)
        {
            cin>>r[i]>>h[i];
        }

        long long fans=0;

        for(int i=0;i<n;i++)
        {
            long long ans=(2*r[i]*h[i])+(r[i]*r[i]);

            vector<long long> vc;

            for(int j=0;j<n;j++)
            {
                if(j!=i && r[j]<=r[i])
                {
                    vc.push_back(2*r[j]*h[j]);
                }
            }

            if(vc.size()<k-1)
            {
                 continue;
            }

            sort(vc.begin(),vc.end());

            int cnt=0;

            for(int j=vc.size()-1;j>=0;j--)
            {
                if(cnt==(k-1)) break;
                ans+=vc[j]; cnt++;
            }
            fans=max(fans,ans);


        }

        double oans= 1.0*fans*pi;

        cout<<fixed<<setprecision(10)<<oans<<endl;

	}
}
