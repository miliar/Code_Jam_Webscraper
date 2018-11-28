#include<bits/stdc++.h>
using namespace std;

char s[1010];

int main()
{
    FILE *f,*g;
    f = fopen("in.txt","r");
    g = fopen("out.txt","w");
    int t,k,i,j;
    char ch;
    fscanf(f,"%d",&t);
    int t1 = t;
    while(t--)
    {
        fscanf(f,"%c",&ch);
        fscanf(f,"%s %d",s,&k);
        int l = strlen(s),countx=0;
        for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                countx++;
                if(i+k-1 <= l-1)
                {
                    for(j=i;j<=i+k-1;j++)
                    {
                        if(s[j]=='+')
                        {
                            s[j] = '-';
                        }
                        else if(s[j]=='-')
                        {
                            s[j] = '+';
                        }
                    }
                }
            }
        }
        int f = 1;
        for(i=0;i<l;i++)
        {
            if(s[i] == '-')
            {
                f = 0;
                break;
            }
        }
        if(f)
        {
            fprintf(g,"Case #%d: %d\n",t1-t,countx);
        }
        else
        {
            fprintf(g,"Case #%d: IMPOSSIBLE\n",t1-t);
        }
    }
    return(0);
}
