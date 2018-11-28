#include <iostream>
#include <string>
#include <sstream>

using namespace std;

long firstTidy(long i) {
  stringstream ss;
  ss << i;
  string s = ss.str();
  char prev = s[0];
  for (int i = 1; i < s.size(); i ++) {
    char curr = s[i];
    if (curr < prev) {
      //  cout << "Not tidy: " << curr << ", " << prev << endl;
      s[i-1] = prev - 1;
      for (int j = i; j < s.size(); j++) {
        s[j] = '9';
      }
      long result;
      stringstream ss2;
      ss2 << s;
      ss2 >> result;
      //cout << result << endl;
      return firstTidy(result);
    }
    prev = curr;
  }
  return i;
}


int main() {
  int tc;
  cin >> tc;
  for (int i = 0; i < tc; i++) {
    long N;
    cin >> N;
    long result = firstTidy(N);
    cout << "Case #" << i+1 << ": " << result << endl;
  }
}
