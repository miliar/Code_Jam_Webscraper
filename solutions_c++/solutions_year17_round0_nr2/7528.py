#include <bits/stdc++.h>
using namespace std;

int main()
{   long long t,ii,j;
    scanf("%lld",&t);
    for(ii=1;ii<=t;ii++)
    {   string str;
        cin>>str;
        long long i,l=str.length();
        bool b=0;
        for(i=0;i<(l-1);i++)
        {   if(str[i]>str[i+1])
            {   if(str[i]=='1')
                {   b=1;
                    break;
                }
                else
                {   for(j=i;j>0;j--)
                        if(str[j-1]!=str[i])
                            break;
                    str[j]--;
                    for(j=j+1;j<l;j++)
                        str[j]='9';
                    break;
                }
            }
        }
        printf("Case #%lld: ",ii);
        if(b)
        {   for(i=0;i<(l-1);i++)
                printf("9");
        }
        else if(!b)
        {   for(i=0;i<l;i++)
                printf("%c",str[i]);
        }
        printf("\n");
    }
    return 0;
}
