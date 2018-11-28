#include <stdio.h>
#include <iostream>
#include <limits>
#include <vector>
#include <math.h>
using namespace std;
typedef unsigned long long ull;
vector<int> splitNumberToDigit(ull ans){
  vector<int> x;
  while(ans!=0){
    x.push_back(ans%10);
    ans=ans/10;
  }
  reverse(x.begin(),x.end());
  return x;
}
ull combineNumber(vector<int> x){
  ull sum=0;
  int cnt = 0;
  for(int i=x.size()-1;i>=0;i--){

    sum+=(x[i]*(ull)pow(10,cnt));
    cnt++;
  }
  return sum;
}
bool isTidy(ull number){
  vector<int> x = splitNumberToDigit(number);
  
  for(int i=0;i<x.size()-1;i++){
    if(!(x[i] <= x[i+1]))
      return false;
  }
  return true;
}
void myprogram(){
  int TC;
  cin >> TC;
  for(int cs=1;cs<=TC;cs++){
    ull N;
    cin >> N;
    if(N<10)
      cout << "Case #" << cs << ": "<< N << endl;
    else{
      ull ans = N;
      while(!isTidy(ans)){
        vector<int> x = splitNumberToDigit(ans);
        for(int i=0;i<x.size()-1;i++){
          if(x[i]>x[i+1]){
            x[i]--;
            for(int j=i+1;j<x.size();j++){
              x[j]=9;
            }
            break;
          }
        }
        ans = combineNumber(x);
      }
      cout << "Case #"<<cs<<": "<<ans << endl;
    }
  }
}
void test(){
  vector<int> x = splitNumberToDigit(87999);
  cout<<  combineNumber(x) << endl;
}
int main(){
  myprogram();
//  test();
}
