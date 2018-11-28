#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int N;

int tidy(int num)
{
    char str1[21],str2[21],ch;
    int i=0;
    int len;

    memset(str1, '\0',sizeof(str1));
    memset(str2, '\0',sizeof(str2));

    while(num!=0){
    ch = (num%10)+48;
    str1[i++] = ch;
    num /= 10;
    }
    len = strlen(str1);
    strcpy(str2,str1);

    sort(str2,str2+len);
    int mul = 1;
    num = 0;

    for(i=len-1; i>=0; i--,mul*=10){
            num = num + (str2[i]-48)*mul;
    }

   if(num == N){
        return 1;}
    else{
        return 0;}
}

int main()
{
    int t,i;

    scanf("%d",&t);
    for(i=1; i<=t; i++)
    {
        scanf("%d",&N);

        while(!tidy(N))
            N--;
        printf("Case #%d: %d\n",i,N);
    }
    return 0;
}
