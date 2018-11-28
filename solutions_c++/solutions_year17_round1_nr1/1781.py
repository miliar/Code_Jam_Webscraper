#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in", "r" , stdin);
    freopen("output.out", "w", stdout);
    int caseno=0,t;
    cin>>t;
    long long int ci=1;
    while(caseno++<t)
    {
        cout<<"Case #"<<caseno<<":\n";
        int n,k,left,right,odd=0,even=0,num=0,l=0,freq[250]={0};
        char a[30][30]={0};
        int r,c,i,j;
        cin>>r>>c;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                cin>>a[i][j];
                if(a[i][j]!='?'&&l==0)
                {
                    num=i;
                    l=1;
                }
            }
        }
        for(i=0;i<r;i++)
        {
            A:
            for(j=0;j<c;j++)
            {
                if(a[i][j]!='?')
                    break;
            }
            if(j==c)
            {
                if(i>0)
                {
                    for(j=0;j<c;j++)
                        a[i][j]=a[i-1][j];
                    continue;
                }
                else
                {
                    for(j=0;j<c;j++)
                        a[i][j]=a[num][j];
                    goto A;
                }
            }
            a[i][0]=a[i][j];
            for(j=1;j<c;j++)
            {
                if(a[i][j]=='?')
                    a[i][j]=a[i][j-1];
            }
        }
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
                cout<<a[i][j];
            cout<<"\n";
        }
    }
    return 0;
}
