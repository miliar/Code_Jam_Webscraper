#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <array>
#include <forward_list>
#include <list>
#include <stack>
#include <algorithm>
#include <functional>
#include <limits>
#include <memory>
#include <tuple>
#include <initializer_list>
#include <utility>
#include <iterator>
#include <bitset>

using namespace std;

bool flip(string& pancakes, size_t start, int k){
  if(start + k > pancakes.size())
    return false;
  
  for(size_t i = start; i < start + k; ++i){
    pancakes[i] = pancakes[i] == '+' ? '-' : '+';
  }
  
  return true;
}

int main()
{
//  ifstream arq(getenv("MYARQ"));
//  cin.rdbuf(arq.rdbuf());
  
  string line;
  int test_cases;
  getline(cin, line);
  stringstream(line) >> test_cases;
  
  for (int i = 1; i <= test_cases; ++i) {
    string pancakes{};
    int k{0};
    
    getline(cin, line);
    stringstream(line) >> pancakes >> k;
    size_t index{0};
    size_t count{0};
    
    for(; index < pancakes.size(); ++index){
      if(pancakes[index] == '+')
        continue;
      
      if(!flip(pancakes, index, k))
        break;
      
      ++count;
    }
    
    string result{};
    for(size_t j = index; j < pancakes.size(); ++j){
      if(pancakes[j] == '-'){
        result = "IMPOSSIBLE";
        break;
      }
    }
    
    if(result.empty()){
      result = to_string(count);
    }
    
    cout << "Case #" << i << ": " << result << endl;
  }
  
  return 0;
}
