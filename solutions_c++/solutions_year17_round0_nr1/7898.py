#include <bits/stdc++.h>

#define MOD 1000000009

using namespace std;

int main()
{
    freopen("D:/codes/in.txt","r",stdin);
    freopen("D:/codes/out.txt","w",stdout);

    int t,n,i,j,l,m,cnt,ans;
    char s[1005];

     scanf("%d",&t);
     int tc=t;
     while(t--)
     {
        scanf("%s%d",&s,&n);
        printf("Case #%d: ",tc-t);

        l=strlen(s);
        cnt=0;
        for(i=0;i<l;++i)
        {
            if(s[i]=='-')
            {
                if(i<l-n+1)
                {
                    for(j=i;j<i+n;++j)
                        s[j]=='+' ? s[j]='-' : s[j]='+';
                    ++cnt;
                }
                else
                {
                    printf("IMPOSSIBLE\n");
                    cnt=-1;
                    break;
                }
            }
        }

        if(cnt>=0)
            printf("%d\n",cnt);

     }

	return 0;

}
