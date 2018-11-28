#include <iostream>
using namespace std;
#define ll long long

int main()
{   ll t,i1;
    scanf("%lld",&t);
    for(i1=1;i1<=t;i1++)
    {   ll a,b,i,j,k=0,l,r=0,m;
        scanf("%lld%lld",&a,&b);
        string s;
        char z[a][b],q;
        for(i=0;i<a;i++)
        {   cin>>s;
            for(j=0;j<b;j++)
                z[i][j]=s[j];
        }
        for(i=0;i<a;i++)
        {   for(j=0;j<b;j++)
            {   r=-1;
                q='?';
                for(l=r+1;l<b;l++)
                {   if(z[i][l]>64)
                    {   for(m=r+1;m<l;m++)
                            z[i][m]=z[i][l];
                        q=z[i][l];
                        r=l;
                    }
                }
                for(l=b-1;l>=0;l--)
                    if(z[i][l]==63 && q>64)
                        z[i][l]=q;
            }
        }
        for(i=0;i<a;i++)
        {   if(z[i][0]>64)
            {   for(j=i-1;j>=0;j--)
                {   if(z[j][0]<64)
                    {   for(m=0;m<b;m++)
                            z[j][m]=z[i][m];
                    }
                    else
                        break;
                }
            }
        }
        for(i=0;i<a;i++)
            if(z[i][0]>64)
                r=i;
        for(i=a-1;i>=0;i--)
        {   if(z[i][0]=='?')
                for(j=0;j<b;j++)
                    z[i][j]=z[r][j];
        }
        for(i=0;i<a;i++)
        {   for(j=0;j<b;j++)
                printf("%c",z[i][j]);
            printf("\n");
        }
    }
    return 0;
}

