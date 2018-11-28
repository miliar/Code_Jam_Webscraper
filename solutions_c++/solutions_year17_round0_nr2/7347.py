#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;

string ComputeTidy(string number)
{
  char curr, next;
  int length = number.length(); 
  long long int N = atoll(number.c_str());
  if(length == 1) return number;
  for(int i = length - 1; i > 0; --i){
    curr = number.at(i-1);
    next = number.at(i);
    if(curr > next){
      N -= atoll(number.substr(i, length-i).c_str()) + 1;
    } 
    number = to_string(N);
  }
  return number;
}

void GetAnswer()
{
  int T;
  string number, answer;
  cin >> T;
  for(int i = 1; i <= T; ++i){
    cin >> number;
    answer = ComputeTidy(number);
    cout << "Case #"<<i<<": "<<answer<< endl;
  }
}

int main()
{
  GetAnswer();
  return 0;  
}      
