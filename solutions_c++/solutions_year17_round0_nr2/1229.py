#include<bits/stdc++.h>
using namespace std;
int n;
char s[25];
main()
{
    int time,cnum=1;
    int i,j,ok;
    freopen("B-large.in","r",stdin);
    freopen("B_out.txt","w",stdout);
    scanf("%d",&time);
    while(time--)
    {
        scanf(" %s",s);
        n = strlen(s);
        for(i=n-2;i>=0;i--)
        {
            if(s[i]>s[i+1])
            {
                s[i] = s[i]-1;
                for(j=i+1;j<n;j++) s[j] = '9';
            }
        }
        printf("Case #%d: ",cnum++);
        ok = 0;
        for(i=0;i<n;i++)
        {
            if(ok) printf("%c",s[i]);
            else if(s[i]!='0') printf("%c",s[i]), ok = 1;
        }
        printf("\n");
    }
}
