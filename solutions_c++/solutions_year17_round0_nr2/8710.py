#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int T,n,i,j,k;
    string ar;
    scanf("%d",&T);
    for(j=1;j<=T;j++)
    {
        cin>>ar;
        n=ar.length();
        for(i=n-1;i>0;i--)
        {
            if(ar[i]>=ar[i-1])
                continue;
            else
            {
                ar[i-1]--;
                for(k=i;k<n;k++)
                    ar[k]='9';
            }
        }
        printf("Case #%d: ",j);
        if(ar[0]!='0')
            cout<<ar[0];
        for(i=1;i<n;i++)
            cout<<ar[i];
        cout<<endl;

    }
}
