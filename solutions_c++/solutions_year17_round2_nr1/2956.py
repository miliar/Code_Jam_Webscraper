#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    freopen("A-large(1).in", "r", stdin);
freopen("A-large2.out", "w", stdout);
int t;
cin>>t;
for(int loop=1;loop<=t;++loop)
{
    double s,temp2=0.0,ans=0.0;
    ll k,d,temp1;
    int n;
    cin>>d>>n;

    for(int i=0;i<n;++i)
    {
        cin>>k>>s;
        temp1=d-k;
        temp2=(temp1*1.0)/s;
        ans=max(temp2,ans);
    }
    ans=(d*1.0)/ans;
    cout<<"Case #"<<loop<<": ";
    printf("%f",ans);
    cout<<endl;
}


return 0;
}
