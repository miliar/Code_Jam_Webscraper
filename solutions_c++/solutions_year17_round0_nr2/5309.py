#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string.h>
using namespace std;
char digit[10]={'0','1','2','3','4','5','6','7','8','9'};
main()
{
    FILE* FileRead = fopen("B-large.in", "r");
    FILE* FileWrite = fopen("out.txt", "w");

    int n;
    fscanf(FileRead, "%d", &n);

    char input[100000];
    int ct,Min;
    int num[100000];
    for(int i = 0 ; i < n ; i++)
    {
        fscanf(FileRead, "%s", input);
        fprintf(FileWrite, "Case #%d: ", i+1);
        int m=strlen(input);
        if(m!=1)
        {
            bool nine=false;
            for(int j=0;j<m;j++)
            {
                num[j]=input[j]-'0';
            }
            for(int j=m-1;j>=1;j--)
            {
                if(num[j]<num[j-1]||num[j]==0)
                {
                    num[j]=9;
                    if(num[j-1]>0)num[j-1]-=1;
                }
            }
            for(int j=0;j<m;j++)
            {
                if(num[j]==0)continue;
                if(num[j]<num[j-1]&&j!=0)num[j]=9;
                fprintf(FileWrite,"%d",num[j]);
            }
        }
        else fprintf(FileWrite,"%c",input[0]);
        fprintf(FileWrite,"\n");
    }
}


