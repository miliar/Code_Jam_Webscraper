#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
int checkminus(char Z[],int ll)
{
    for(int m=0;m<ll;m++)
    {
        if(Z[m]=='-')
            return 1;
    }
    return 0;
}
int getminus(char Z[],int ll)
{
    for(int m=0;m<ll;m++)
    {
        if(Z[m]=='-')
            return m;
    }
    return 0;
}
int main()
{
    FILE *fp;
    fp=fopen("A-large.in","r");
    FILE *fpa;
    fpa=fopen("ans1Large.txt","w");
    int T,t,j,K,l,i,ll,c,ni;
    char S[1001];
    fscanf(fp,"%d",&T);
    for(t=1;t<=T;t++)
    {
        c=0;
        ni=1;
        fscanf(fp,"%s %d",S,&K);
        l = strlen(S);
        if(!checkminus(S,l))
        {
            fprintf(fpa,"Case #%d: 0\n",t);
            continue;
        }
        else
        {
            do
            {
                ll=getminus(S,l);
                if(ll>(l-K))
                    ll=l-K;
                for(i=ll;i<(ll+K);i++)
                    if(S[i]=='+')
                        S[i]='-';
                    else
                        S[i]='+';
                c++;
                if(c>3000)
                {
                    fprintf(fpa,"Case #%d: IMPOSSIBLE\n",t);
                    ni=0;
                    break;
                }
            }while(checkminus(S,l));
            if(ni)
                fprintf(fpa,"Case #%d: %d\n",t,c);
        }
    }

    fclose(fp);
    fclose(fpa);
    return 0;
}

