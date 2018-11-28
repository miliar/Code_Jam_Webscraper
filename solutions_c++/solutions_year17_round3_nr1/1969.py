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
      int N,K;
      std::vector<std::pair<int,int> > pancakes;
      
      input>>N>>K;
      for (int index=0;index<N;++index) {
        int R,H;
        input>>R>>H;
        pancakes.push_back(std::make_pair(R,H));
      }

      return std::make_pair(K,pancakes);
    }

    template<typename TData> auto Solve(TData&& data) {
      std::string PI("31415926535897932384626433832795");
      int K=data.first;
      auto& pancakes=data.second;
      long long int result=0;

      if (K>1)
        for (int index = 0;index<pancakes.size();++index)
          for (int index2 = index + 1;index2<pancakes.size();++index2)
            if (static_cast<long long int>(pancakes[index].first)*static_cast<long long int>(pancakes[index].second)<static_cast<long long int>(pancakes[index2].first)*static_cast<long long int>(pancakes[index2].second)) std::swap(pancakes[index], pancakes[index2]);

      for (int index = 0;index<pancakes.size();++index) {
        long long int currentResult = static_cast<long long int>(pancakes[index].first)*static_cast<long long int>(pancakes[index].first) + 2*static_cast<long long int>(pancakes[index].first)*static_cast<long long int>(pancakes[index].second);
        int remaining = K - 1;

        if (remaining>0)
          for (int index2 = 0;index2<pancakes.size();++index2)
            if ((index2!=index)&&(pancakes[index2].first <= pancakes[index].first)) {
              currentResult += 2*static_cast<long long int>(pancakes[index2].first)*static_cast<long long int>(pancakes[index2].second);
              if (--remaining == 0) break;
            }

        if (remaining == 0) result = std::max(result, currentResult);
      }

      std::string l;
      while (result>0) {
        l.push_back(result%10);
        result/=10;
      }
      
      std::string r(50,0);
      std::reverse(PI.begin(),PI.end());
      for (char& c : PI) c -= '0';

      for (int index=0;index<PI.size();++index)
        for (int index2=0;index2<l.size();++index2) {
          r[index+index2]+=PI[index]*l[index2];
          if (r[index + index2]>=10) {
            r[index+index2+1]+= r[index + index2]/10;
            r[index + index2]= r[index + index2]%10;
          }
        }
      for (char& c:r) c+='0';
      r.insert(r.begin()+31,'.');
      std::reverse(r.begin(),r.end());

      auto iterator = r.begin();
      while (*iterator=='0') ++iterator;

      return std::string(iterator,r.end()-22);
    }

    template<typename TSolution> void WriteOutput(std::ofstream& output,TSolution&& solution) const {
      output<<solution;
    }
};

void main() {
  std::ifstream input("Input.Txt");
  std::ofstream output("Output.Txt");
  int testCount;

  input>>testCount;
  for (int testCase=1;testCase<=testCount;++testCase) {
    Task task;

    output<<"Case #"<<testCase<<": ";
    task.WriteOutput(output,task.Solve(task.ReadInput(input)));
    if (testCase!=testCount) output<<std::endl;
  }
}