#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("init.in","r",stdin);
freopen("output.out","w",stdout);
    int n,cases=1;
    scanf("%d",&n);

    while(n--)
    {
        char ch[10005];
        int num;
        scanf("%s %d",&ch,&num);

        int len = strlen(ch);
        int cnt=0;

        for(int i=0;i<len;i++)
        {
            if(ch[i]=='-' && (i+num)<=len) {
               cnt++;
            for(int j=0;j<num;j++)
            {
                    if(ch[j+i]=='+') ch[j+i]='-';
                      else ch[j+i]='+';
            }

            }
        }

        for(int i=0;i<len;i++)
            if(ch[i]=='-') cnt=-1;

        if(cnt==-1) printf("Case #%d: IMPOSSIBLE\n",cases++);
        else printf("Case #%d: %d\n",cases++,cnt);


    }
    return 0;
}
