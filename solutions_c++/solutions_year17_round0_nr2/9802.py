#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int num;
  cin >> num;

  vector<unsigned long> res(num,0);
  for(int i=0; i < num; ++i){
      vector<int> input_vec;
      unsigned long input;
      cin >> input;
      unsigned long tmp = input;
      while(tmp > 0) {
          input_vec.push_back(tmp % 10);
          tmp /= 10;
        }
      unsigned long local_res = 0;
      int len = input_vec.size();
          for(int j=0; j < len-1; ++j){
              if(input_vec[j] < input_vec[j+1]){
                  int k = j;
                  while(k>-1){
                        input_vec[k] = 9;
                        --k;
                  }
                  --input_vec[j+1];
                }
            }


      for(int j=len-1; j >= 0; --j){
        local_res = local_res * 10 + input_vec[j];
      }

      res[i] = local_res;
    }

  for(int i=0; i < num ; ++i){
      cout << "Case #" << i+1 << ": " << res[i] << "\n";

    }
  return 0;
}

