#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <algorithm>
using namespace std;

char swap(char x){
  if(x == '-'){
    return '+';
  }
  return '-';

}

string flip(string pc, int start, int end){
    for(int i=start;i<end;i++){
      pc[i] = swap(pc[i]);
    }
  return pc;

}
bool happy_check(string pc){
  for(int i=0;i<pc.length();i++){
    if(pc[i] == '-'){
      return false;
    }
  }
  return true;
}

int count_operation(string pc, int K){
  int count = 0;
  for(int p = 0;p<=pc.length()-K;p++){
    if(pc[p] == '-'){
      pc = flip(pc, p, p+K);
      count++;
    }
  }
  if(happy_check(pc)){
    return count;
  }
  return -1;
}


int main(){
  int K;
  int count = 1;
  int res;
  string pancake, mystr;
  ifstream Afile("A-large.txt");
  ofstream output("ans.txt");
  getline(Afile, mystr);
  if(Afile.is_open()){
    while(getline(Afile, mystr)){
        stringstream stream(mystr);
        stream>>pancake;
        stream>>K;
        res = count_operation(pancake, K);
        if(res != -1){
          output<<"Case #"<<count<<": " << res <<endl;
        }
        else{
          output<<"Case #"<<count<<": " << "IMPOSSIBLE" <<endl;
        }

        count++;
    }
  }
  Afile.close();
  return 0;
}
