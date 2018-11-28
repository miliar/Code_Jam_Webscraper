#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#define ll long long int
using namespace std;
void convert(int *b,int d,int n){
  for(int i=d-1;i>=0;i--)
  {
    b[i]=n%10;
    n=n/10;
  }
}
bool tidy(int *b,int d){
  for(int i=0;i<d-1;i++)
  {
    if(b[i+1]<b[i])
      return false;
  }
  return true;
}
int count_digits(long long int n){
  int d=0;
  while(n>0){
    n=n/10;
    d++;}
  return d;
}
void print(int *b,int d){
  for(int i=0;i<d;i++)
    printf("%d",b[i]);
  printf("\n");
}
int main(){
  int TC;
  cin>>TC;
  for(int t_i=0;t_i<TC;t_i++){
    long long int n;
    scanf("%lld",&n);
    int d=count_digits(n);
    long long int x=0;
    for(int i=0;i<d;i++)
      x=x*10+1;
    if(n>=x){
      int b[d];
      convert(b,d,n);
      int k=1000;
      while(!tidy(b,d)&&k--){
        int j;
        for(j=0;j<d-1;j++){
          if(b[j]>b[j+1])
            break;

      }
      b[j]--;
      j++;
        for(;j<d;j++){
          b[j]=9;
      }
      }
      printf("Case #%d: ",t_i+1);
      for(int i=0;i<d;i++)
        printf("%d",b[i]);
      printf("\n");
    }
    else{
      cout<<"Case #"<<t_i+1<<": "<<string(d-1,'9')<<endl;
    }
  }
  return 0;
}
