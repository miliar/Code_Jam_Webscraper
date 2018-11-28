#include<bits/stdc++.h>
#include<math.h>
#define INPUT
using namespace std;
int main()
{
    #ifdef INPUT
        freopen("input.cpp", "r", stdin);
        freopen("out.cpp", "w", stdout);
    #endif // INPUT
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        int n,k,j,temp,p,q,r,ans1,ans2,exp,s;
        cin>>n>>k;
        exp = log2(k);
        s = pow(2,exp);
        temp = n;
        temp = temp - s + 1;
        p = temp%s;
        q = temp/s;
        temp = k - s + 1;
        if(temp<=p)
            q++;
        if(q%2==0)
        {
            ans1 = q/2;
            ans2 = ans1 - 1;
        }
        else
        {
            ans2 = q/2;
            ans1 = ans2;
        }
        cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
