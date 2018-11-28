#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#define cin ifile
#define cout ofile

using namespace std;

long double s[200],ans[200];
long long D[200][200],lim[200];

int main()
{
    ifstream ifile("C-small-attempt0.in");
    ofstream ofile("out1.txt");
    int t;
    cin>>t;

    for(int fff=1;fff<=t;fff++)
    {
        int n,q;
        cin>>n>>q;
        for(int i=0;i<n;i++)
        {
            cin>>lim[i]>>s[i];
        }

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
                cin>>D[i][j];
        }
        long double inf=1e16;
        ans[n-1]=0;
        for(int i=n-2;i>=0;i--)
        {
            long long dist=0;
            ans[i]=inf;
            for(int j=i+1;j<n;j++)
            {
                dist+=D[j-1][j];
                if(dist>lim[i])
                    break;
                ans[i]=min(ans[i],ans[j]+dist/s[i]);
            }
        }
        while(q--)
        {
            int a,b;
            cin>>a>>b;
        }

        cout<<"Case #"<<fff<<": "<<fixed<<setprecision(8)<<ans[0]<<"\n";
    }
    return 0;
}
