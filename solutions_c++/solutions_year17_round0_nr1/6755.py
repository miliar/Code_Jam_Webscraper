#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
using namespace std;
int main()
{
    FILE *fp;
    FILE *fp2;
    fp=fopen("A-large.in.txt","r");
    fp2=fopen("answer2.txt","w");
    int t;
    fscanf(fp,"%d",&t);
    for(int i=1; i<=t; i++)
    {
        char arr[1005];
        fscanf(fp,"%s",arr);
        int s;
        int cnt=0;
        fscanf(fp,"%d",&s);
        int len=strlen(arr);
        for(int a=0; a<=len-s; a++)
        {
            if(arr[a]=='-')
            {
                cnt++;
                for(int b=a; b<a+s; b++)
                {
                    if(arr[b]=='-')
                        arr[b]='+';
                    else if(arr[b]=='+')
                        arr[b]='-';
                }
              //  printf("cnt: %d  ",cnt);
              //  for(int b=0; b<len; b++)
              //      printf("%c",arr[b]);
              //  printf("\n");
            }
        }
        bool flag=false;
        for(int a=0; a<len; a++)
        {
            if(arr[a]=='-')
                flag=true;
        }
        if(flag)
            fprintf(fp2,"Case #%d: IMPOSSIBLE\n",i);
        else
            fprintf(fp2,"Case #%d: %d\n",i,cnt);
    }
    return 0;
}
