// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdio.h>
using namespace std;

int ans(string line, int k){
  int sz = line.length();
  int co = 0;
  bool is = true;
  for(int i=0; i< sz ;i++){
    if(line.at(i)=='-'){
      co++;
      for(int j=0;j<k;j++){
        //printf("%d ",i+j);
        if(i+j>=sz){
          return -1;
        }
        if(line.at(i+j)=='-'){
          //-를 플러스로
          line.replace(i+j,1,"+");
        }else{
          //+를 -로
          line.replace(i+j,1,"-");
        }
      }
    }
  }
  return co;
}

int main(){
  FILE* pFile;
  int n,k; string line;
  pFile = fopen("a.txt","w");
  scanf("%d", &n); printf("%d\n",n);
  for(int i=1; i<=n;i++){
    cin >> line;
    cin >> k;
    int out = ans(line,k);
    if(out == -1){
      fprintf(pFile,"Case #%d: IMPOSSIBLE\n",i);
    }else{
      fprintf(pFile,"Case #%d: %d\n",i,out);
    }
  }
}
