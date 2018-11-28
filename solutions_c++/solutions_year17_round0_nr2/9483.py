#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
int main(){
  int testcases;
  int tn=1;
  scanf("%d",&testcases);
  long long n;
  while(testcases--){
    scanf("%lld",&n);
    std::vector<int> vec;
    while(n){
      vec.push_back(n%10);
      n=n/10;
    }
    int size = vec.size();
    //std::reverse(vec.begin(),vec.end());
    for(int i=1;i<size;i++){
      if(vec[i] >vec[i-1]){
        int ptr = i-1;
        while(ptr>=0 && vec[ptr] < vec[ptr+1]){
          vec[ptr]= 9;
          ptr--;
        }
        vec[i]--;
      }
    }
    long long res=0;
    for(int i=size-1;i>=0;i--){
      res = res*10+vec[i];
    }
    printf("\nCase #%d: %lld",tn,res);
    tn++;
  }
  return 0;
}
