#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <utility>

using namespace std;

struct Stall
{
  int pos;
  int Ls;
  int Rs;
  int occ = 0;
};

int main(int agrc, char **argv) {

  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
  	int N,K;
  	cin >> N >> K;

    int min_result = 0;
    int max_result = 0;

    vector<Stall> stalls;
    Stall s_0  = {0,0,0,1};
    stalls.push_back(s_0);
    for(int i = 1; i <= N; i++)
    {
      Stall s  = {i,i-1,abs(N-i),0};
      stalls.push_back(s);
    }
    Stall s_1  = {N,0,0,1};
    stalls.push_back(s_1);

    for(int k = 0; k < K; k++){

        vector<int> chosen;
        int max = -1;
        for(int i = 1; i <= N; i++){
            if(stalls.at(i).occ == 0){
                int min = (stalls.at(i).Ls < stalls.at(i).Rs ? stalls.at(i).Ls : stalls.at(i).Rs);
                if(min > max)
                {
                  max = min;
                  chosen.clear();
                  chosen.push_back(i);
                }
                else if(min == max)
                  chosen.push_back(i);
            }
        }

        int chosen_one;
        chosen.shrink_to_fit();
        if(chosen.size() == 1)
          chosen_one = chosen.at(0);
        else{
          vector<int> chosen_2;
          int max = -1;
          for (int i = 0; i < chosen.size(); i++){
            int pos = chosen.at(i);
            int max_ = (stalls.at(pos).Ls > stalls.at(pos).Rs ? stalls.at(pos).Ls : stalls.at(pos).Rs);
                if(max_ > max)
                {
                  max = max_;
                  chosen_2.clear();
                  chosen_2.push_back(pos);
                }
                else if(max_ == max)
                  chosen_2.push_back(pos);

          }

          chosen_one = chosen_2.at(0);

        }

      stalls.at(chosen_one).occ = 1;

      for(int i = 1; i <= N; i++){
          if(stalls.at(i).occ == 0){
              for(int l = i; l >= 0; l--){
                if(stalls.at(l).occ == 1){
                  stalls.at(i).Ls = abs(l-i)-1;
                  break;
                }
              }
              for(int r = i; r <= N+1; r++){
                if(stalls.at(r).occ == 1){
                  stalls.at(i).Rs = abs(r-i)-1;
                  break;
                }
              }
          }
      }

      min_result = (stalls.at(chosen_one).Ls < stalls.at(chosen_one).Rs ? stalls.at(chosen_one).Ls : stalls.at(chosen_one).Rs);
      max_result = (stalls.at(chosen_one).Ls > stalls.at(chosen_one).Rs ? stalls.at(chosen_one).Ls : stalls.at(chosen_one).Rs);

      chosen.clear();
      chosen.shrink_to_fit();
    }


    cout << "Case #" << t << ": " << max_result << " " << min_result << endl;

  }

  return 0;

}