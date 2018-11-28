#include<stdio.h>
#include<string.h>
char a[10000];


int main()
{
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    int T,ll=0;
    fscanf(in,"%d",&T);
    while(T--)
    {
        ll++;
        int k,c=0;
        fscanf(in,"%s %d",a,&k);
        int l= strlen(a),i;
        for(i=0;i<=l-k;i++)
        {
            if(a[i]=='-')
            {
                c++;
                for(int j=i;j<i+k;j++)
                {
                    if(a[j]=='-'){a[j]='+';}
                    else{a[j]='-';}
                }
            }
        }
        fprintf(out,"Case #%d: ",ll);
        for(i=0;i<l;i++){if(a[i]=='-'){break;}}
        if(i==l){fprintf(out,"%d",c);}
        else{fprintf(out,"IMPOSSIBLE");}
        fprintf(out,"\n");
    }
}
