
#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int t,n;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        double d,x,y,ans=-1,temp;
        cin>>d;
        cin>>n;
        while(n--)
        {
            cin>>x>>y;
            temp=(d-x)/y;
            if(temp>ans)
                ans=temp;
        }
        printf("Case #%d: ",i+1);
        cout<<setprecision(6)<<fixed<<d/ans<<endl;
    }
}
