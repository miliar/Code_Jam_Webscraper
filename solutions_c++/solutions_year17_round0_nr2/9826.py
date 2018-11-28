#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;
void program();
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
int n;
scanf("%d",&n);
while(n>0){
if(n%10==n){
    printf("Case #%d: %d\n",testCase,n);
    break;
}
else{
int arr[1000];
int count=0;
int t=n;
while(t>=1){
    int temp=t%10;
    arr[count]=temp;
    t=t/10;
    count++;
}
int tidy=0;
for(int i=0;i<count-1;i++){
    if(arr[i]<arr[i+1]){
        tidy=1;
        break;
    }
    // printf("%d ",arr[i]);
}
//printf("%d %d\n",n,tidy);
if(tidy==0){
    printf("Case #%d: %d\n",testCase,n);
    break;
}
}
n--;
}
/*---------------------------------------------------------------------*/
testCase++;
}
return 0;
}
