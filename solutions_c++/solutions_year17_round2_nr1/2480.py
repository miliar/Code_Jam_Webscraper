#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("test1.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    long long int t,n,d,i,j,x=0;
    double k,s,ans,max1=0.0,an;
    cin>>t;
    while(t--)
    {
        long long int count=0;
        x++;
        max1=0.0;
        cout<<"Case #"<<x<<": ";
        cin>>d>>n;
        for(i=0;i<n;i++)
        {
            cin>>k>>s;
            ans=(d-k)/s;
            max1=max(ans,max1);
        }
        an=d/max1;
        printf("%.8lf",an);
        cout<<endl;
        //cout<<an<<endl;
    }
}
