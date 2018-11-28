#include <bits/stdc++.h>
using namespace std;

#define ll double

int main()
{
freopen("A-small-attempt0.in","r",stdin);
freopen("ansa.out","w",stdout);
long int t,ctr=0;
    cin>>t;
    while(t--)
    {ctr++;
        long int n,k,i;
         cin>>n>>k;
         ll ar[n][2];

            for(i=0;i<n;i++)
            {
                cin>>ar[i][0]>>ar[i][1];
            }
                 vector<long int> selected;
                 vector<long int> selector(n);
                 fill(selector.begin(),selector.begin() + k, 1);
                 ll ans=-1.0;
                 do {
                     for (i=0;i<n;i++)
                      {
                        if (selector[i])
                        {
                            selected.push_back(i);
                        }
                     }
                    ll sum=0.0;
                     long int len =selected.size(),maxr=-1;
                     for(i=0;i<len;i++)
                     {
                        sum+=ar[selected[i]][0]*ar[selected[i]][1];
                        if(ar[selected[i]][0]>maxr)
                            maxr=ar[selected[i]][0];
                     }

                      sum=sum*2*3.14159265359;
                      sum+=3.14159265359*maxr*maxr;

                     if(sum>ans)
                        ans=sum;

                     selected.clear();
                 }
                 while (prev_permutation(selector.begin(), selector.end()));
                 cout<<setprecision(6)<<fixed;

        cout<<"Case #"<<ctr<<": "<<ans<<endl;

    }
    return 0;
}
