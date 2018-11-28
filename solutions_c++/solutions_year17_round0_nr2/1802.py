#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
using namespace std;

typedef long long ll;
int T;
ll n ;
char str[20];




int main()
{
    int ca = 1;
    freopen("B-large.in","r",stdin);
    freopen("B-large-out.txt","w",stdout);
    scanf("%d",&T);
    //cout<<T<<endl;
    while (T--)
    {
        scanf("%s",str);
      //  cout<<str<<endl;
        int len = strlen(str);
        for (int i = len -1 ; i >= 1 ; --i)
        {
            if (str[i-1]>str[i])
            {
                for (int j = i ; j < len ; j ++)
                    str[j] = '9';
                for (int j = i-1 ; j>=0 ;  --j)
                {
                    if (str[j]=='0')
                        str[j] ='9';
                    else
                    {
                        --str[j];
                        break;
                    }
                }
            }
        }
        printf("Case #%d: ",ca++);
        bool flag = false;
        for (int i = 0 ; i <len ; i ++)
        {
            if (str[i]!='0')
                flag= true;
            if (flag)
                putchar(str[i]);
        }
        putchar('\n');


    }

}
