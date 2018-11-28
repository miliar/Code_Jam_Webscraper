#include <bits/stdc++.h>
using namespace std;

int main() 
{
    double t,d,n,j,s,k,a,max;long long int i;
    cin>>t;
    for(i=0;i<t;i++)
        {
        cin>>d>>n;        
       cin>>k>>s;
        k=d-k;
        k=k/s;
        max=k;
        for(j=1;j<n;j++)
            {
            cin>>k>>s;
            k=d-k;
            k=k/s;           
            if(k>max)
                max=k;
        }
        cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(9)<<d/max<<endl;
    }
    return 0;
}
