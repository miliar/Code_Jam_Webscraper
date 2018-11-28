#include <bits/stdc++.h>
using namespace std;
int T;
long double P[1000];
long double need(int i)
{
    long double ret=0;
    for (int j=0;j<i;j++)
        ret+=P[i]-P[j];
    return ret;
}
int main()
{

    freopen("in","r",stdin);
    freopen("out","w",stdout);

    cin>>T;
    for (int tt=1;tt<=T;tt++)
    {
        int n,k;
        cin>>n>>k;
        long double U;
        cin>>U;
        for (int i=0;i<n;i++)
            cin>>P[i];
        sort(P,P+n);
        long double ret=0;
        for (int i=0;i<n;i++)
        {
            long double op=need(i);
            if (op>U)
                break;
            op=U-op;
            long double add=op/(i+1);
            long double cur=1;
            bool no=0;
            for (int j=0;j<=i;j++)
                cur*=P[i]+add,no=(P[i]+add>1.0);
            for (int j=i+1;j<n;j++)
                cur*=P[j];
            if (!no)
            ret=max(ret,cur);
        }
        printf("Case #%d: ",tt);
        cout<<setprecision(10)<<fixed<<ret<<endl;
    }
}
