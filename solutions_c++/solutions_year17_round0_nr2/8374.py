//
//  main.cpp
//  codejam
//
//  Created by Carlos Spaggiari Roa on 4/7/17.
//  Copyright © 2017 ARSC. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <set>




using namespace std;
int cases;

string buffer;
int n;



//
//void printfs(){
//  for (int j = 0 ; j < buffer.size() ; ++j){
//    buffer[j] += 48;
//  }
//  
//  for (int j = 0 ; j < buffer.size() ; ++j){
//    if (buffer[j] > '0') {
//      cout << &buffer[j];
//      break;
//    }
//  }
//  
//  for (int j = 0 ; j < buffer.size() ; ++j){
//    buffer[j] -= 48;
//  }
//  
//}


void tidy() {
  bool bad = true;
  while (bad) {
    bad = false;
    for (int i = 0 ; i < buffer.size()-1 ; ++i){
      if (buffer[i] > buffer[i+1]){
        --buffer[i];
        bad = true;
        for (int j = i+1 ; j < buffer.size() ; ++j){
          buffer[j] = 9;
        }
      }
    }
  }
  
}


int main(int argc, const char * argv[]) {
  
  cin >> cases;
  
  for (int i = 0 ; i < cases ; ++i){
    buffer = "";
    cin >> buffer;
    
    for (int j = 0 ; j < buffer.size() ; ++j){
      buffer[j] -= 48;
    }
    
    tidy();
    
    for (int j = 0 ; j < buffer.size() ; ++j){
      buffer[j] += 48;
    }
    
    
    
    for (int j = 0 ; j < buffer.size() ; ++j){
      if (buffer[j] > '0') {
        printf("Case #%d: %s\n", i+1, &buffer[j]);
        break;
      }
    }
    
    
  }
  
  
  
    return 0;
}
