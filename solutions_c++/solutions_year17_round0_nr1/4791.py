#include <stdio.h>
#include <iostream>
using namespace std;

int count33(char cake[])
{
    int many = 0;
    for(int i=0;cake[i];i++) if(cake[i] == '-') many++;
    return many;
}

int main()
{
    int t;
    cin >> t;
    for(int k=1;k<=t;k++)
    {
        int cnt=0,len,fullLen;
        char cake[1010];

        scanf("%s %d",cake,&len);
        for(fullLen=0;cake[fullLen];fullLen++);

        for(int i=0;i<=fullLen-len+1;i++)
        {
            if(count33(cake) == 0) break;
            if(cake[i] == '-')
            {
                cnt++;
                for(int j=0;j<len;j++)
                {
                    if(cake[i+j] == '-') cake[i+j] = '+';
                    else cake[i+j] = '-';
                }
            }
        }

        if(count33(cake) != 0) printf("Case #%d: IMPOSSIBLE\n",k);
        else printf("Case #%d: %d\n",k,cnt);
    }
}
