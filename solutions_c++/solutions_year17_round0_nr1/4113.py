#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){

  int T;
  cin >> T;

  for (int i = 0; i < T; i++){
    string input;
    cin >> input;

    int n_pancakes = input.size();
    vector<bool> pancakes;

    int k;
    cin >> k;

    for (int j = 0; j < n_pancakes; j++){
      if (input[j] == '+')
        pancakes.push_back(1);
      else
        pancakes.push_back(0);
    }

    int i_ll = 0, i_lr = k-1, i_rr = n_pancakes-1, i_rl = n_pancakes-k;

    int count = 0;
    while (i_ll <= i_rr && (i_rl >= 0 || i_lr <n_pancakes) ){

      if (!pancakes[i_ll]){
        count++;
        for (int k = i_ll; k <= i_lr; k++){
          pancakes[k] = pancakes[k] ^ 1;
        }
      }

      if (!pancakes[i_rr]){
        count++;
        for (int k = i_rr; k >= i_rl; k--){
          pancakes[k] = pancakes[k] ^ 1;
        }
      }

      i_ll++;
      i_lr++;
      i_rr--;
      i_rl--;
    }

    bool possible = true;

    for (int j = 0; j < n_pancakes; j++){
      if (!pancakes[j]){
        cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        possible = false;
        break;
      }
    }

    if (possible)
      cout << "Case #" << i+1 << ": " << count << endl;

  }

  return 0;
}
