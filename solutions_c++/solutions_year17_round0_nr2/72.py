#include<bits/stdc++.h>
using namespace std;

char s[22];

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        scanf("%s",s);
        int n = strlen(s);
        for(int i=1;i<n;i++)
        {
            if(s[i] >= s[i-1])
                continue;
            for(int j=i;j<n;j++)
                s[j] = '9';
            i--;
            if(s[i] == '0')
                while(i >= 0 && s[i] == '0')
                {
                    s[i] = '9';
                    i--;
                }
            if(i>=0)
            {
                s[i]--;
                i--;
            }
        }
        for(int i=0;i<n;i++)
        {
            if(s[i] == '0') continue;
            for(int j=i;j<n;j++) putchar(s[j]);
            puts("");
            break;
        }
    }
}
