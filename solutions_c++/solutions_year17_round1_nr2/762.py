#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
long long int t,q,n,p,Ind[1000],nr;
double V[1000],ing[1000][1000];
bool ok(double x)
{
    for (int i=0;i<n;i++)
    {
            if ((x*1.1000000001)<(ing[i][Ind[i]]/V[i]))
                return false;
    }
  //  cout<<x<<" ";
    return true;
}
int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    cin>>t;
    for (int q=1;q<=t;q++)
    {
        nr=0;
        cout<<"Case #"<<q<<": ";
        cin>>n>>p;
        for (int i=0;i<n;i++)
            cin>>V[i];
        for (int i=0;i<n;i++)
        {
            Ind[i]=0;
            for (int j=0;j<p;j++)
                cin>>ing[i][j];
            sort(ing[i],ing[i]+p);
        }
        bool f = false,g=false;
        for (double i=1;;i++)
        {
            for (int j=0;j<n;j++)
            {
                while ((i*0.89999999)>(ing[j][Ind[j]]/V[j])&&Ind[j]<p)
                {
                   // cout<<i<<" "<<(ing[j][Ind[j]]/V[j])<<" ||";
                    Ind[j]++;
                }
            }
            for (int j=0;j<n;j++)
                {
                    if (Ind[j]>=p)
                      f=true;
                }
            if (f)
                break;
            while (ok(i))
            {
                nr++;
                for (int j=0;j<n;j++)
                {
                    Ind[j]++;
                    if (Ind[j]>=p)
                      g=true;
                }
                if (g) break;
            }
            for (int j=0;j<n;j++)
                {
                    if (Ind[j]>=p)
                      f=true;
                }
            if (f)
                break;
        }
        cout<<nr<<'\n';
    }
}
