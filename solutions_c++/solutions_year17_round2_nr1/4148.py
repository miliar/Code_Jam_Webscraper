#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    ll T,cnt=1;
    cin>>T;
    while(T--)
    {
        double maxm=0.0;
        double D,N,K,S,t;
        cin>>D>>N;
        for(int i=0;i<N;i++)
        {
            cin>>K>>S;
            t=(D-K)/S;
           // cout<<t<<endl;
            if(t>maxm)
            {
                maxm=t;
            }
        }
        cout<<"Case #"<<cnt<<": ";
        if(maxm)
        printf("%lf\n",(D/maxm));
            //cout<<(D/maxm)<<endl;
        else
            printf("%lf\n",D);
        cnt++;
    }
	// your code goes here
	return 0;
}
