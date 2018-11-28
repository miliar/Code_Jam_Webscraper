#include <bits/stdc++.h>
using namespace std;
double pb[60][60];
double cp(const vector<double>&y,int k)
{
    for(int i=0;i<60;i++)
        for(int j=0;j<60;j++)
            pb[i][j]=0;
    pb[0][0]=1.0;
    for(int i=0;i<y.size();i++)
    {
        for(int j=0;j<=53;j++)
        {
            pb[i+1][j+1]+=pb[i][j]*y[i];
            pb[i+1][j]+=pb[i][j]*(1-y[i]);
        }
    }
    double re=0;
    for(int i=k;i<=53;i++)
    {
        re+=pb[y.size()][i];
    }
    return re;
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("C3.out","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int n,k;
        cin>>n>>k;
        double x;
        cin>>x;
        vector<double> y;
        for(int i=0;i<n;i++)
        {
            double z;
            cin>>z;
            y.push_back(z);
        }
        sort(y.begin(),y.end());
        vector<double> z;
        for(int i=0;i<k;i++)
        {
            z.push_back(y.back());
            y.pop_back();
        }
        double an=0;
        sort(z.begin(),z.end());
        double cu=z[0];
        int cn=1;
        for(int i=1;i<z.size();i++)
        {
            if(cn*(z[i]-cu)>x)
            {
                cu+=x/cn;
                x=0;
                break;
            }
            x-=cn*(z[i]-cu);
            cu=z[i];
            cn++;
        }
        cu+=x/cn;
        cu=min(cu,1.0);
        for(int i=0;i<cn;i++)
        {
            z[i]=cu;
        }
        for(int i=0;i<z.size();i++)
            y.push_back(z[i]);
        an=1;
        for(int i=0;i<y.size();i++)
            an*=y[i];
        printf("Case #%d: %.9f\n",tt,an);
    }
}
