#include<stdio.h>

#define OUTFILE "output.txt"

void output(int,int);

FILE *inputfile, *outputfile;

int main(void)
{
    int T;
    int n;

    inputfile= fopen("B-small-attempt0.in","r");

    if(inputfile!=NULL)
    {

    outputfile=fopen(OUTFILE, "w");

    fscanf(inputfile,"%d", &T);

    for(int i=1;i<=T;i++)
    {
        fscanf(inputfile,"%d",&n);
        output(n,i);
    }

    fclose(inputfile);
    fclose(outputfile);

    }

    else
    {
        printf("\nError in opening file");
    }
}

void output(int n, int num)
{
    int previousDigit, temp, previousTidy;
    bool isTidy;

        for(int i=1;i<=n;i++)
        {
            temp=i;
            previousDigit=temp%10;
            temp/=10;
            isTidy=true;
            while(temp!=0)
            {
                if(temp%10>previousDigit)
                {
                    isTidy=false;
                    break;
                }
                previousDigit=temp%10;
                temp/=10;
            }
            if(isTidy==true)
                previousTidy=i;
        }

        fprintf(outputfile,"Case #%d: %d\n", num, previousTidy);

}

