#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        long long D,N;
        double ans=0;
        cin>>D>>N;
        while(N--)
        {
            long long p,x;
            cin>>p>>x;
            if((((D-p)*1.0)/(x*1.0))>ans)
                ans=(((D-p)*1.0)/(x*1.0));
        }
        double s= (D*1.0)/(ans*1.0);
        cout<<"Case #"<<i<<": ";
        //cout<<s;
        printf("%0.6f",s);
        cout<<endl;
    }
}
