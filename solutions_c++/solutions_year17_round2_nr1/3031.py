#include <bits/stdc++.h>
using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);
    int t;
    double a[105];
    int l=1,i;
    cin>>t;
    while(t--)
    {
        double d,k,s;
        int n,i;
       double m=0,maxm=0;
        cin>>d>>n;
        for(i=1;i<=n;i++)
        {
            cin>>k>>s;
            m=(d-k)/s;
            maxm=max(m,maxm);
        }
        a[l]=d/maxm;
        l++;
    }
    for(i=1;i<l;i++)
        cout<<"Case #"<<i<<": "<<setprecision(15)<<a[i]<<endl;
   
  
}

