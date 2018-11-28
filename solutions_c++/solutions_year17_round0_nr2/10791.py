#include <iostream>
#include <sstream>
#include <string>

using namespace std;  

bool is_tidy(long long num) {
  ostringstream ss;
  ss << num;
  string num_str = ss.str();
  for (int i=1; i < num_str.length(); i++)
    if (num_str[i]<num_str[i-1])
      return false;
  return true;
}

int main() {
  int t;
  long long n;
  cin >> t;  
  for (int i = 1; i <= t; i++) {
    cin >> n;
    while (!is_tidy(n))n--;
    cout << "Case #" << i << ": " << n<< endl;
  }
}
