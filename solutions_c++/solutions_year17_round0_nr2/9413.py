#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
using namespace std;

int isGood(char arr[]){
    int length=strlen(arr);
    for(int i=0;i<(length-1);i++){
        int a=arr[i],b=arr[i+1];
        if(a>b){
            return 0;
        }
        
    }
    return 1;
}

void repair(char arr[]){
    int length=strlen(arr);
    char rest;
    for(int j=0;j<(length-1);j++){
          int a=arr[j]-48,b=arr[j+1]-48;
          if(a>b){
              arr[j]--;
              if(a==1){
                  rest='9';
              }
              else rest=arr[j];
              for(int k=(j+1);k<length;k++){
                  arr[k]='9';
              }
          }
    }
    if(isGood(arr)==0)
    repair(arr);
}

int main()
{
    int t;
    char arr[20];
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        scanf("%s",&arr);
        int length=strlen(arr);
        if(length>1)
        repair(arr);
        printf("Case #%d: ",i);
        for(int j=0;j<length;j++){
            if(arr[j]!='0')
            printf("%c",arr[j]);
        }
        printf("\n");
    }
    return 0;
}