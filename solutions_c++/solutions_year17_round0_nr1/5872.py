#include <bits/stdc++.h>
using namespace std;
int t,i,j,k,l,m,ans;
char s[1111];
FILE *in,*out;
int main()
{
    in=fopen("A-large.in","r");
    out=fopen("output.out","w");
    for(fscanf(in,"%d",&t);i<t;i++)
    {
        fscanf(in,"%s %d",s,&k);
        l=strlen(s);
        ans=0;
        for(j=0;j<=l-k;j++)
            if(s[j]=='-')
            {
                ans++;
                for(m=0;m<k;m++)
                    if(s[j+m]=='-')
                        s[j+m]='+';
                    else s[j+m]='-';
            }
        for(j=l-k+1;j<l;j++)
            if(s[j]=='-')
            {
                ans=-1;
                break;
            }
        fprintf(out,"Case #%d: ",i+1);
        if(ans==-1)
            fprintf(out,"IMPOSSIBLE\n");
        else fprintf(out,"%d\n",ans);
    }
}

