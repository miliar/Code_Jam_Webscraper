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
int k;
int n;
string initial;
string desired;
set<string> dp;


int recur(string buffer){
  int best = -1;
  if (buffer == desired){
    return 0;
    
  } else if (dp.find(buffer) != dp.end()){
    return -1;
  } else {
    
     dp.insert(buffer);
    for (int i = 0 ; i <= initial.size() - k ; ++i){
      string aux = buffer;
      for (int j = i ; j < i+k ; ++j){
        aux[j] = aux[j] == '+' ? '-' : '+';
      }
//      cout << aux << "   " << i << "  " << i+k << "\n";
      
      int a = recur(aux);
      if (a != -1) {
        if (best == -1 || best > a) best = a + 1;
      }
      
    }
  }
  if (best != -1)
    dp.erase(dp.find(buffer));
  return best;
}



int main(int argc, const char * argv[]) {
  
  cin >> cases;
  
  for (int i = 0 ; i < cases ; ++i){
    dp.clear();
    cin >> initial;
    cin >> k;
    desired = "";
    for (int i = 0 ; i < initial.size() ; ++i){
      desired += "+";
    }
//    cout << " --> " + initial << "\n";
    
    n = recur(initial);
    
    if (n == -1 ) printf("Case #%d: IMPOSSIBLE\n", i+1);
    else
      printf("Case #%d: %d\n", i+1, n);
    
  }
  
  
  
    return 0;
}
