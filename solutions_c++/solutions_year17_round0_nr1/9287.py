#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;
char flip(char c){
    if(c=='-')
    c='+';
    else
    c='-';
    return c;
}
int main()
{
//Diverting the input stream into file "temp.in".Comment the below line to use console
freopen("input_file.in", "r", stdin);
//Diverting the output stream into file "temp.out".Comment the below line to use console
freopen("output_file.out", "w", stdout);

int testCase=1;
int testCases=1;
scanf("%d",&testCases);//Comment this line if there is only one test case
while(testCase<testCases+1)
{
/*---------------------------------------------------------------------*/
char s[1000];
int k=2;
scanf("%s %d",s,&k);
int size= strlen(s);
//printf("%s %d %d",s,k,size);
int count=0;
for(int i=0;i<size-k+1;i++){
    //printf("%c\n",s[i]);
    if(s[i]=='-'){
        int t=i;
        for(int j=0;j<k;j++){
        s[t]=flip(s[t]);
        t++;
        }
        count++;
    }
}
int flag=0;
for(int i=0;i<size;i++){
    if(s[i]=='-'){
    flag=1;
    break;
    }
}
if(flag==0)
printf("Case #%d: %d\n",testCase,count);
else
printf("Case #%d: IMPOSSIBLE\n",testCase);
/*---------------------------------------------------------------------*/
testCase++;
}
return 0;
}
