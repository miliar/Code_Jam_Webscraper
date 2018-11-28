#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

string getLastTidyNumber(string number) {
  int size = number.size();

  if(size == 1) { return number; }

  char buffer[size];

  for(int i=0;i<size;i++) {
    if(i == size - 1) {
      buffer[i] = number[i];
    } else if(number[i] > number[i+1]) {
      buffer[i] = number[i] - 1;
      for(int j=i+1;j<size;j++) {
        buffer[j] = '9';
      }
      for(int j=i;j>0;j--) {
        if(buffer[j] < buffer[j-1]) {
          buffer[j] = '9';
          buffer[j-1] = buffer[j-1] - 1;
        }
      }
      break;
    } else {
      buffer[i] = number[i];
    }
  }

  string result(buffer, size);

  return result.erase(0, min(result.find_first_not_of('0'), result.size()-1));
}


int main() {
  int n;
  unsigned long long input;

  cin>>n;

  for(int i=1;i<=n;i++) {
    cin>>input;

    string stringifiedInput = to_string(input);
    cout<<"Case #"<<i<<": "<<getLastTidyNumber(stringifiedInput)<<endl;
  }


  return 0;
}
