#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<array>
#include<vector>
#include<map>
#include<utility>
#include<bitset>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<utility>
using namespace std;
int main()
{   int temp,inc;
    cin>>temp;
    for(inc=1;inc<=temp;inc++)
    {   int a1,b1,i,j,l,r=0,m;
        cin>>a1>>b1;
        string s;
        char z[a1][b1],q;
        for(i=0;i<a1;i++)
        {   cin>>s;
            for(j=0;j<b1;j++)
                z[i][j]=s[j];
        }
        for(i=0;i<a1;i++)
        {   for(j=0;j<b1;j++)
            {   r=-1;
                q='?';
                for(l=r+1;l<b1;l++)
                {   if(z[i][l]>64)
                    {   for(m=r+1;m<l;m++)
                            z[i][m]=z[i][l];
                        q=z[i][l];
                        r=l;
                    }
                }
                for(l=b1-1;l>=0;l--)
                    if(z[i][l]==63 && q>64)
                        z[i][l]=q;
            }
        }
        for(i=0;i<a1;i++)
            if(z[i][0]>64)
                r=i;
        for(i=a1-1;i>=0;i--)
        {   if(z[i][0]=='?')
                for(j=0;j<b1;j++)
                    z[i][j]=z[r][j];
        }
        for(i=0;i<a1;i++)
        {   if(z[i][0]>64)
            {   for(j=i-1;j>=0;j--)
                {   if(z[j][0]<64)
                    {   for(m=0;m<b1;m++)
                            z[j][m]=z[i][m];
                    }
                    else
                        break;
                }
            }
        }
        cout<<"Case #"<<inc<<":\n";
        for(i=0;i<a1;i++)
        {   for(j=0;j<b1;j++)
                cout<<z[i][j];
            cout<<"\n";
        }
    }
    return 0;
}
