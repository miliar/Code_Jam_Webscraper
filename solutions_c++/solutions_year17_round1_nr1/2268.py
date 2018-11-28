#include<bits/stdc++.h>
using namespace std;
char a[100][100];
long long i,j,k,l,m,n,t,x,y;
int main()
{
    cin>>t;m=0;
    while(t--)
    {++m;
        cin>>x>>y;
        for(i=0;i<x;++i)
        {
            cin>>a[i];
        }k=0;
        for(i=0;i<x;++i)
        {k=0;
            for(j=0;j<y;++j)
            {
                if(a[i][j]=='?')
                {
                   k++;
                }
            }
            //cout<<a[i]<<k;
            if(k!=y)
            {
                 for(j=1;j<y;++j)
                    {
                        if(a[i][j]=='?')
                            {
                                a[i][j]=a[i][j-1];
                            }
                    }
                    for(j=y-2;j>=0;--j)
                    {
                        if(a[i][j]=='?')
                            {
                                a[i][j]=a[i][j+1];
                            }
                    }
            }
            else
            {
                if(i!=0){
                for(j=0;j<y;++j)
                    {
                         a[i][j]=a[i-1][j];
                    }
            }}
        }
            for(i=x-2;i>=0;--i)
            {
                k=0;
                for(j=0;j<y;++j)
                {
                    if(a[i][j]=='?')
                    {
                        k++;
                    }
                }//cout<<a[i]<<k;
                if(k==y)
                {
                    for(j=0;j<y;++j){
                    a[i][j]=a[i+1][j];}
                }
            }



         cout<<"Case #"<<m<<":\n";
            for(i=0;i<x;++i)
            {
                cout<<a[i]<<"\n";
            }
    }
    return 0;
}
