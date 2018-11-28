#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("F:\\in.in","r",stdin);
    freopen("C:\\Users\\User\\Desktop\\out.in","w",stdout);
    int t=0,ns;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int i,n;
        cin>>n;
        int k=n;
        for(i=k;i>=0;i--)
        {    n=i;
            while(n!=0 && (n%10) >= (n/10)%10 )
            {
                n/=10;
            }
            if(n==0)break;
        }
        printf("Case #%d: %d\n",j,i);
    }
    return 0;
}
