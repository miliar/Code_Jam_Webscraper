#include <bits/stdc++.h>

using namespace std;

int n,q;
long long arr[2][109];
vector<vector<long double> >dist;
vector<vector<long double> >dist2;
void flyd()
{
    dist2=dist;
    for(int k=0;k<n;k++)
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(dist2[i][j]>dist2[i][k]+dist2[k][j])
                    dist2[i][j]=dist2[i][k]+dist2[k][j];
}
vector<vector<long long> >dist3;
vector<vector<long long> >dist4;
void flyd2()
{
    dist4=dist3;
    for(int k=0;k<n;k++)
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(dist4[i][j]>dist4[i][k]+dist4[k][j])
                    dist4[i][j]=dist4[i][k]+dist4[k][j];
}

int main()
{
    freopen("in5.txt","r",stdin);
    freopen("out5.txt","w",stdout);
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++){
        dist.clear();
        dist3.clear();
        cin>>n>>q;
        for(int f=0;f<n;f++)
            cin>>arr[0][f]>>arr[1][f];
        for(int f=0;f<n;f++)
        {
            vector<long long>v;
            for(int f1=0;f1<n;f1++)
            {
                long long x;
                cin>>x;
                if(x==-1)
                    x=1e18;
                v.push_back(x);
            }
            dist3.push_back(v);
        }
        flyd2();
        for(int f=0;f<n;f++)
        {
            vector<long double>v;
            for(int f1=0;f1<n;f1++)
            {
                if(dist4[f][f1]>arr[0][f])
                    dist4[f][f1]=1e18;
                v.push_back(1.0*dist4[f][f1]/arr[1][f]);
            }
            dist.push_back(v);
        }
        flyd();
        int a,b;
        cout<<"Case #"<<tc<<":";
        while(q--)
        {
            cin>>a>>b;
            cout<<" "<<setprecision(9)<<fixed<<dist2[a-1][b-1];
        }
        cout<<endl;
    }
}
