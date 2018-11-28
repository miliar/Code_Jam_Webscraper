#include <iostream>
#include <string>

void print(int caseNum, std::string output) {
  std::cout << "Case #" << caseNum << ": " << output << std::endl;
}

int main() {
  std::string line;
  getline(std::cin, line);
  int T = std::stoi(line);

  for (int t = 1; t <= T; ++t) {
    std::string input;
    getline(std::cin, input);

    std::string output;
    int inputSize = input.size();
    int mark = 0;
    int prevNumber = input[0]-'0';
    bool insertLast = true;
    for (int i = 1; i < inputSize; ++i) {
      if (input[i]-'0' == prevNumber) continue;
      if (input[i]-'0' < prevNumber) {
        if (prevNumber != 1) output += '0'+(prevNumber-1);
        for (int j = mark+1; j < inputSize; ++j) {
          output += '9';
        }
        insertLast = false;
        break;
      } else {
        output += input.substr(mark, i-mark);
        mark = i;
        prevNumber = input[i]-'0';
      }
    }
    if (insertLast) {
      output += input.substr(mark);
    }

    print(t, output);
  }

  return 0;
}
