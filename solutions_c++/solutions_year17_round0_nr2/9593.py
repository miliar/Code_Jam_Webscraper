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

bool is_special_case(const string& number){
  auto itr = number.begin();
  
  char ch = *itr;
  int trip = atoi(&ch);
  
  while(itr != number.end()) {
    ch = *itr++;
    int digit = atoi(&ch);
    
    if(digit != 1 && digit != 0)
      return false;
    
    if(trip == digit)
      continue;
    
    if(digit == 1)
      return false;
    
    trip = digit;
  }
  
  return number.back() == '0';
}

string get_string_of_9s(size_t count){
  return string(count, '9');
}

string reduce(const string& str){
  if(str.empty())
    return "";
  
  auto r_itr = str.rbegin();
  char ch = (*r_itr);
  int prev = atoi(&ch) - 1;
  string result = to_string(prev);
  ++r_itr;
  
  while(r_itr != str.rend()){
    ch = (*r_itr);
    int num = atoi(&ch);
    
    if(num > prev){
      result += to_string(num - 1);
    }
    else{
      result += (*r_itr);
    }
    
    ++r_itr;
  }
  
  reverse(result.begin(), result.end());
  return result;
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
    cout << "Case #" << i << ": ";
    
    string number;
    getline(cin, number);
    
    if(is_special_case(number)){
      cout << get_string_of_9s(number.size() - 1) << endl;
      continue;
    }
  
    string result;
    auto itr = number.begin();
    result += (*itr);
    char ch = (*itr);
    int prev = atoi(&ch);
    ++itr;
    
    while (itr != number.end()) {
      ch = (*itr);
      int current = atoi(&ch);
      
      if(current >= prev){
        result += (*itr);
      }
      else{
        if(result.back() == 1)
          result.pop_back();
        else{
          result = reduce(result);
        }
        
        result += '9';
        result += get_string_of_9s(distance(itr, number.end()) - 1);
        
        break;
      }
      
      ++itr;
      prev = current;
    }
    
    auto found = result.find_first_not_of("0");
    if(found != 0)
      result = result.substr(found, string::npos);
    
    if(result.size() == number.size()){
      auto result_itr = result.begin();
      auto number_itr = number.begin();
      string final_result;
      
      while(result_itr != result.end()){
        char ch = *result_itr;
        int r = atoi(&ch);
        
        ch = *number_itr;
        int n = atoi(&ch);
        
        if(n == r){
          final_result += ch;
        }
        else{
          final_result += to_string(r);
          final_result += get_string_of_9s(distance(result_itr, result.end()) - 1);
          result = final_result;
          break;
        }
        
        ++result_itr;
        ++number_itr;
      }
    }
    
    cout << result << endl;
  }
  
  return 0;
}
