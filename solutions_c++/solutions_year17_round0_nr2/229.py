#include <bits/stdc++.h>
using namespace std;


char s[10050];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",ti++);
        scanf("%s",s);
        int f=-1;
        for(int i=1;s[i];i++)
            if(s[i]<s[i-1])
            {
                s[f=i-1]--;
                int p=i-1;
                while(p>0)
                {
                    if(s[p]<s[p-1])
                        s[f=p-1]--;
                    else
                        break;
                    p--;
                }
                break;
            }
        if(f==-1)
            puts(s);
        else
        {
            for(int i=f+1;s[i];i++)
                s[i]='9';
            int p=0;
            while(s[p]=='0')p++;
            puts(s+p);
        }
    }
    return 0;
}
