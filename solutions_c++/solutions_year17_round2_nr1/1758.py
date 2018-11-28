#include<bits/stdc++.h>
#include <stdio.h>
using namespace std;

void fun()
{
    double d;
    int n;
    scanf("%lf %d",&d,&n);
    double maxi=0;
    for(int i=0;i<n;i++)
    {
        double distance,velocity;
        cin>>distance>>velocity;
        maxi=max(maxi,(d-distance)/velocity);
    }
    double ans=d/maxi;
    cout<<fixed<<setprecision(10)<<ans;
}
int main()
{
    bool testing=1;
    if(testing==1)
    {
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    }
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        fun();
        cout<<endl;
    }
    return 0;
}
