#include <iostream> 
#include <fstream>
#include <map>
#include <sstream>
#include <cmath>

using namespace std; 

int main() { 
  unsigned long long int n = 0, k = 0;
  string n2;
  string s="";
  int count = 0;
  int round = 1;
  
  ifstream inFile("input.in");
  ofstream outFile("output.out");

  if(inFile.is_open()){
    getline(inFile,s);
    while(getline(inFile,s, ' ')){
      getline(inFile,n2);
      istringstream f(s);
      istringstream f2(n2);
      f >> n;
      f2 >> k;
      int finalmax = -999999;
      int finalmaxmax = -999999;

      //set up stalls
      int stalls[n+2] = {};
      int jank[n+2] = {};
      stalls[0] = 1;
      stalls[n+1] = 1;
      
      for(int person = 0; person < k; person++){
          int curMax = -999999;
          int maxPos=0;
          
          int curMax2 = -999999;
          int maxPos2=0;
          
        for(int i = 1; i < n+2; i++){
          int L=0, R=0;

          //unoccupied
          if(stalls[i] == 0){
            for(int j = i-1; j >=0; j--){
              if(stalls[j] == 0){
                L++;
              }else{
                break;
              }
            }
            for(int k = i+1; k < n+2; k++){
              if(stalls[k] == 0){
                R++;
              }else{
                break;
              }
            }
            if(min(L,R) > curMax){
              jank[i] = max(L,R);
              maxPos = i;
              curMax = min(L,R);
              if(max(L,R) > curMax2){
                maxPos2 = i;
                curMax2 = max(L,R);
                //cout << L << " " << R << endl;
              }
            }
           // cout << L << " " << R << endl;
            
          }

        }
        stalls[maxPos] = 1;
        finalmax = curMax;
        finalmaxmax = jank[maxPos];
      }
      cout << "Case #" << round << ": "<< finalmaxmax << " " << finalmax << endl;
      outFile <<"Case #" << round << ": "<< finalmaxmax << " " << finalmax << endl;
      // for(int i = 0; i < n+2; i++){
      //   cout << stalls[i];
      // }
      round++;

    }
    
  }

  inFile.close();
  outFile.close();
} 





