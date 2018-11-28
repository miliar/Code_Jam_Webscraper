#include <iostream>
#include <string>

using namespace std;

string makeTidy(string input) {
  int i =0;
  if (input.size() == 1)
    return input;
  while (i < input.size()-1 && input[i]<=input[i+1]) i++;
  string temp = "";
  if (i==0 && input[i] == '1') {
    for (int j=0; j < input.size()-1; j++) {
      temp += "9";
    }
    return temp;
  }
  if (i==input.size()-1)
    return input;
  
  while (i>0 && input[i] == input[i-1]) i--;
  if (i==0 && input[i] == '1') {
    for (int j=0; j < input.size()-1; j++) {
      temp += "9";
    }
    return temp;
  }
  input[i] = input[i]-1;
  for (int j=i+1; j < input.size(); j++) {
    input[j] = '9';
  }
  return input;
}

int main() {
  int numTrials;
  cin >> numTrials;
  for (int i=0; i < numTrials; i++) {
    int highestTidy = 0;
    string trial;
    cin >> trial;
    trial = makeTidy(trial);
    cout << "Case #" << i+1 << ": " << trial << endl;
  }
}
