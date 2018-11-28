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
      std::pair<std::string, int> data;
      
      input>>data.first>>data.second;
      
      return data;
    }

    template<typename TData> auto Solve(TData&& data) {
      auto& state=data.first;
      int K=data.second;
      int result=0;

      for (auto index=0;index<=state.size()-K;++index)
        if (state[index]=='-') {
          for (auto index2=index;index2<index+K;++index2) state[index2]=(state[index2]=='-')?'+':'-';
          ++result;
        }

      for (auto index = state.size()-K+1;index<state.size();++index) if (state[index]=='-') return -1;

      return result;                                                                                              
    }

    template<typename TSolution> void WriteOutput(std::ofstream& output,TSolution&& solution) const {
      if (solution<0) output<<"IMPOSSIBLE"; else output<<solution;
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