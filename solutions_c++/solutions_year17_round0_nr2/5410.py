#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <math.h>

using namespace std;

int main()
{
    FILE *fp;
    fp=fopen("B-large.in","r");
    FILE *fpa;
    fpa=fopen("B-large-ans.txt","w");
    long long int ll,num;
    int l,SS[20],i,j,k,T,t,n1,n2;
    char S[20],d[2];
    fscanf(fp,"%d",&T);
    for(t=1;t<=T;t++)
    {
        fscanf(fp,"%s",S);
        l = strlen(S);
        k=100;
        for(i=l-2;i>=0;i--)
        {
            n1=S[i]-'0';
            n2=S[i+1]-'0';
            if(n1>n2)
            {
                k=i+1;
                n1-=1;
                n2=9;
            }
            itoa(n1,d,10);
            S[i] = d[0];
            itoa(n2,d,10);
            S[i+1] = d[0];
        }
        if(k!=100)
        {
            for(i=k+1;i<=l-1;i++)
            {
                S[i]='9';
            }
        }
        if(S[0]=='0')
        {
            for(i=0;i<=l-2;i++)
            {
                S[i]=S[i+1];
            }
            S[i]='\0';
        }
        fprintf(fpa,"Case #%d: %s\n",t,S);
    }

    fclose(fp);
    fclose(fpa);
    return 0;
}
