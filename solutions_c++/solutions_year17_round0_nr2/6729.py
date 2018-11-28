#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
using namespace std;
char num[20];
bool che_num(int* arr,int len)
{
    int start=0;
    for(int a=0; a<len; a++)
    {
        if(arr[a]!=0)
        {
            start=a;
            break;
        }
    }
    for(int a=start; a<len-1; a++)
    {
        int b=a+1;
        if(arr[a]>arr[b])
            return false;
    }
    return true;
}
int main()
{
    int t;
    FILE *fp;
    FILE *fp2;
    fp=fopen("B-large.in","r");
    fp2=fopen("answer.txt","w");
    fscanf(fp,"%d",&t);
    for(int i=1; i<=t; i++)
    {
        fscanf(fp,"%s",num);
        int length=strlen(num);
        int number[20];
        for(int a=0; a<length; a++)
        {
            number[a]=num[a]-'0';
        }
        int start=0;
        int real_start;
        while(!che_num(number,length))
        {
            for(int a=0; a<length; a++)
            {
                if(number[a]!=0)
                {
                    start=a;
                    real_start=a;
                    break;
                }
            }
            //for(int a=start; a<length; a++)
            //    printf("%d",number[a]);
            //printf("\n");
            for(int a=start; a<length-1; a++)
            {
                if(number[a]>number[a+1])
                {
                    number[a]--;
                    for(int b=a+1; b<length; b++)
                        number[b]=9;
                }
            }
        }
        for(int a=0; a<length; a++)
        {
            if(number[a]!=0)
            {
                start=a;
                break;
            }
        }
        fprintf(fp2,"Case #%d: ",i);
        for(int a=start; a<length; a++)
            fprintf(fp2,"%d",number[a]);
        fprintf(fp2,"\n");
    }
    return 0;
}
