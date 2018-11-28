#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main ()
{
int i,j,t,k,r,p;
char s[20];
char a[20];
char c;
FILE *in = fopen("input.txt","r");    
FILE *out= fopen("output.txt","w");
fscanf(in, "%d", &t);
for (i=0;i<t;i++)
    {
    fscanf(in, "%s", s);
    p=0;
    r=0;
    for (j=0;j<strlen(s)-1;j++)
        {
        if (s[j]==s[j+1])
            {r++;}
        if (s[j]<s[j+1])
            {r=0;}    
        if (s[j]>s[j+1])
            {
            if (s[j]=='1')
                {
                fprintf(out, "Case #%d: ", i+1);    

                for (k=0;k<strlen(s)-1;k++)
                    {
                    fprintf(out,"9");
                    }
                fprintf(out,"\n");
                p=1;
                break;
                }
            fprintf(out, "Case #%d: ", i+1);

            for (k=0;k<j-r;k++)
                {
                fprintf(out,"%c",s[k]);
                }
            fprintf(out,"%c",s[j]-1);

            for (k=j-r+1;k<strlen(s);k++)
                {
                fprintf(out,"9");
                }
            fprintf(out,"\n");
            p=1;
            break;    
            }
                
        }
    if (p==0)
        {
        fprintf(out, "Case #%d: ", i+1);
        fprintf(out,"%s\n",s);
        }
    

    }  



    
    
}
