#include <iostream> 
#include <fstream>
#include <map>
#include <sstream>
#include <cmath>

using namespace std; 

int main() { 
  unsigned long long int size = 0, k = 0;
  string n;
  string s="";
  int count = 0;
  int round = 1;
  
  ifstream inFile("input.in");
  ofstream outFile("output.out");

  if(inFile.is_open()){
    getline(inFile,s);
    while(getline(inFile,s, ' ')){
      int imp = 0;
      count = 0;
      getline(inFile,n);
      istringstream f(n);
      f >> k;
      size = s.length();
      
      for(int i = 0; i < size; i++){
        if(s[i] == '-'){
          if(i > size-k){
            cout << "IMPOSSIBLE" << endl;
            imp = 1;
            break;
          }else{
            for(int j = i; j < i+k; j++){
              if(s[j] == '-') s[j] = '+';
              else s[j] = '-';
            }
          }
          count++;
        }
      }
      if(imp){
        outFile <<"Case #" << round << ": "<< "IMPOSSIBLE" << endl;
      }else{
        outFile <<"Case #" << round << ": "<< count << endl;
      }
      round++;
    }
  }
  
  inFile.close();
  outFile.close();
} 





