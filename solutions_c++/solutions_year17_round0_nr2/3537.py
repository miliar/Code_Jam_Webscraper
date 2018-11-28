#include<bits/stdc++.h>
using namespace std;

char s[35];

int main()
{
    FILE *f,*g;
    f = fopen("in.txt","r");
    g = fopen("out.txt","w");
    int t,i,j;
    fscanf(f,"%d",&t);
    int t1 = t;
    while(t--)
    {
        fscanf(f,"%s",s);
        int f = 1;
        while(f)
        {
            f = 0;
            for(i=1;s[i];i++)
            {
                if(s[i-1] > s[i])
                {
                    f = 1;
                    s[i-1]-=1;
                    for(j=i;s[j];j++)
                    {
                        s[j] = '9';
                    }
                    break;
                }
            }
        }
        for(i=0;s[i]=='0';i++);
        fprintf(g,"Case #%d: %s\n",t1-t,s+i);
    }
    return(0);
}
