#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <limits>
#include <map>
#include <stack>
#include <string>
#include <queue>
#include <vector>

class Task {
  private:
  public:
    auto ReadInput(std::ifstream& input) {
      std::string number;
      input>>number;
      return number;
    }

    template<typename TData> auto Solve(TData&& data) {
      auto& number=data;
      for (int index=1;index<number.size();++index)
        if (number[index]<number[index-1]) {
          int index3=index-1;
          
          while ((index3>0)&&(number[index3]==number[index3-1])) --index3;--number[index3];

          for (int index2=index3+1;index2<number.size();++index2) number[index2]='9';
          break;
        }
      auto iterator = number.begin();
      while (*iterator=='0') ++iterator;
      return std::string(iterator,number.end());                                                                                              
    }

    template<typename TSolution> void WriteOutput(std::ofstream& output,TSolution&& solution) const {
      output<<solution;
    }
};

void main() {
  std::ifstream input("Input.Txt");
  std::ofstream output("Output.Txt");
  int testCases;

  input>>testCases;
  for (int testCaseIndex=1;testCaseIndex<=testCases;++testCaseIndex) {
    Task task;
    
    output<<"Case #"<<testCaseIndex<<": ";
    task.WriteOutput(output,task.Solve(task.ReadInput(input)));
    output<<std::endl;
  }
}