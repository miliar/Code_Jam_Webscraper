#include <bits/stdc++.h>

using namespace std;

int t,cs=1,r,c,cnt1[30][30], cnt2[30][30], cnt3[30][30];
char s[30][30], s2[30][30];

int main()
{
    freopen("A-large(1).in","r", stdin);
    freopen("A-large-output.txt", "w", stdout);
    scanf("%d",&t);

    while(t--)
    {
        scanf("%d %d",&r,&c);

        for(int i=0; i<r; i++)
        {
            scanf("%s",s[i]);
            strcpy(s2[i],s[i]);

            for(int j=0; j<c; j++)
            {
                cnt1[i][j]= (bool)(s[i][j]!='?');
                if(j) cnt1[i][j]+= cnt1[i][j-1];
            }
        }

        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                cnt2[i][j]= (bool)(s[i][j]!='?');
                if(i) cnt2[i][j]+= cnt2[i-1][j];
            }
        }

        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                cnt3[i][j]= cnt1[i][j];
                if(i) cnt3[i][j]+= cnt3[i-1][j];
            }
        }
        int x=0, y=0;

        while(x<r)
        {
//            printf("  %d %d\n",x,y);
            int cnt=0;

            y=0;
            int i=x;
            cnt= cnt1[x][c-1];
            while(cnt==0 && i<r-1)
            {
                i++;
                cnt+= cnt1[i][c-1];
            }
            if(cnt==0) break;
            char ch='a';
            while(y<c)
            {
                int j=y;
//                printf(" %d %d\n %d %d\n",x,y,i,j);
                cnt= cnt3[i][j];
//                printf("cnt %d\n",cnt);
                if(x) cnt-= cnt3[x-1][j];
//                printf("%d\n",cnt);
                if(y) cnt-= cnt3[i][y-1];
//                printf("%d\n",cnt);
                if(x && y) cnt+= cnt3[x-1][y-1];
//                printf("%d j %d\n",cnt,j);
                while(cnt==0 && j<c-1)
                {
                    j++;
                    cnt+= cnt2[i][j];
                    if(i) cnt-= cnt2[i-1][j];
//                    printf("%d\n",cnt);
                }
                if(cnt!=0)
                {
                    for(int q=x; q<=i; q++)
                    {
                        for(int w=y; w<=j; w++)
                        {
                            if(s[q][w]!='?') ch=s[q][w];
                        }
                    }
                }
//                cout<<ch<<endl;
//                printf("      %d %d\n",i,j);

                for(int q=x; q<=i; q++)
                {
                    for(int w=y; w<=j; w++)
                    {
                        s2[q][w]=ch;
                    }
                }
                y=j+1;
            }
            x= i+1;
        }

        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                if(s2[i][j]=='?') s2[i][j]= s2[i-1][j];
            }
        }

        printf("Case #%d:\n",cs++);

        for(int i=0; i<r; i++)
        {
            printf("%s\n",s2[i]);
        }
    }
}
