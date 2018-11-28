#include <iostream>
#include <sstream>

using namespace std;

string itos(int num){
  string str;
  ostringstream convert;
  convert << num;
  str = convert.str();
  return str;
}

int ctoi(char ch){
  return ch - '0';
}

int main(){
  int tests = 0, count = 0;
  std::cin >> tests;
  string str;
  int num[tests];
  int resps[tests];

  for (int i = 0; i < tests; i++) {
    std::cin >> num[i];
  }

  for (int i = 0; i < tests; i++) {
    for (int j = num[i]; j >= 0; --j) {
      str = itos(j);
      for (int k = 0; k < (str.length() - 1); k++) {
        if(ctoi(str[k]) > ctoi(str[k+1])){
          ++count;
          break;
        }
      }
      if(count == 0){
        resps[i] = j;
        break;
      }
      count = 0;
    }
  }

  for (int i = 0; i < tests; i++) {
    std::cout << "Case #" << i+1 << ": " << resps[i] << endl;
  }
  return 0;
}
