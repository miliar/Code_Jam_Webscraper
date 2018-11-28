#include<iostream>
#include<string> 
#include<stdlib.h>
#include<sstream>
#include<algorithm>
#include <stdint.h> 
using namespace std; 

int main(){

 int T; 
 string line; 
 getline(cin,line); 
 T = atoi(line.c_str()); 
 for(int i = 0 ; i < T;++i){
    
  getline(cin,line); 
  int64_t j = 0 ; 
  for(j = 0 ; j < line.size()-1 ; ++j){
     if( line[j] <= line[j+1] ) 
       continue;   
     else 
       break;
  }

  cout<<"Case #"<<i+1<<": "; 
  if(j == line.size() - 1){
   cout<<line<<endl; 
   continue;  
  }
  stringstream ss(""); 
  ss<<string(line.size()-j-1,'9'); 
  
  int64_t k = j; 
  for(; k >0 ; --k){
      if(line[k] -1 < line[k-1]){
        ss<<'9'; 
        continue; 
      } else{
       ss<<(char)(line[k] -1); 
       break; 
      }
  }
  if(k == 0 ) {
     if(line[0] -1 > '0'){
      ss<<(char)(line[0]-1); 
     }
     line = ss.str(); 
     reverse(line.begin(),line.end());
     cout<<line<<endl; 
   } else{
     line = string(line.begin(),line.begin()+k);
     string temp = ss.str(); 
     reverse(temp.begin(),temp.end()); 
     line = line + temp; 
     cout<<line<<endl; 
   }

 }
}
