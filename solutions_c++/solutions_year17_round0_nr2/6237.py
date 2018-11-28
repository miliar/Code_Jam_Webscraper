#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

string solve(const std::string &num);

int main(){
  int n_num;
  cin >> n_num;
  vector<string> v(n_num);
  int i;
  for (i = 0; i < n_num; i++){
    cin >> v[i];
    printf("Case #%d: %s\n",i+1, solve(v[i]).c_str());
  }
  return 0;
}

string solve(const std::string &num){
  int num_digit = num.size();
  if (num_digit == 1){
    return num;
  }
  string ans{};
  stack<char> s;
  stack<char> s_aux;
  char max = '0';
  int j = 0;
  while (num[j] >= max){
    s.push(num[j]);
    max = num[j];
    j++;
  }
  if (j == num_digit) return num;
      char last = s.top();
      s.pop();
      
      while(!s.empty() && last == s.top()){
        s.pop();
      }
      last = last - 1;
      s.push(last);
      int num_9 = num_digit - s.size();
      while(num_9--){
        s.push('9');
      }
      while(!s.empty()){
        s_aux.push(s.top());
        s.pop();
      }
      while (s_aux.top() == '0')
        s_aux.pop();
      while(!s_aux.empty()){
        ans += s_aux.top();
        s_aux.pop();
      }
     
      return ans;
}