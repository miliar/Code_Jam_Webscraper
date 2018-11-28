#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){

  int T;

  cin >> T;

  // for (int n_case = 1; n_case <= T; n_case++){
  //
  //   int vec[7];
  //
  //   int N;
  //
  //   cin >> N;
  //   int max_available = 0;
  //   for (int i = 0; i < 6; i++){
  //     cin >> vec[i];
  //     if (vec[i] > vec[max_available])
  //       max_available = i;
  //   }
  //
  //   string sol;
  //
  //   int first_index = max_available;
  //   int last_position = -1;
  //   bool possible = true;
  //   bool decreased_max = true;
  //   while (possible && N > 0){
  //     if (decreased_max){
  //       while (vec[first_index]==0)
  //         first_index = (first_index + 1)%6;
  //     }
  //     if (first_index == last_position){
  //       possible = false;
  //     }
  //     else {
  //       last_position = first_index;
  //       vec[first_index]--;
  //       if (first_index == 0)
  //         sol = sol + 'R';
  //       else if (first_index == 1)
  //         sol = sol + 'O';
  //       else if (first_index == 2)
  //         sol = sol + 'Y';
  //       else if (first_index == 3)
  //         sol = sol + 'G';
  //       else if (first_index == 4)
  //         sol = sol + 'B';
  //       else if (first_index == 5)
  //         sol = sol + 'V';
  //       first_index = (first_index+2)%6;
  //       N--;
  //     }
  //   }
  //
  //   if (possible)
  //     cout << "Case #" << n_case << ": " << sol << endl;
  //   else
  //     cout << "Case #" << n_case << ": " << "IMPOSSIBLE" << endl;
  //
  // }

  for (int n_case = 1; n_case <= T; n_case++){

    int vec[7];

    int N;

    cin >> N;
    int max_available = 0;
    for (int i = 0; i < 6; i++){
      cin >> vec[i];
      if (vec[i] > vec[max_available])
        max_available = i;
    }

    string sol;
    bool possible = true;
    int current_index = max_available;
    int last_decreased = -1;
    int initial_index = max_available;
    while (possible && N > 0){
      // cout << current_index << endl;
      if (vec[current_index] > 0){
        if (current_index == last_decreased){
          possible = false;
        }
        else {
          last_decreased = current_index;
          vec[current_index]--;
          N--;
          if (current_index == 0)
            sol = sol + 'R';
          else if (current_index == 1)
            sol = sol + 'O';
          else if (current_index == 2)
            sol = sol + 'Y';
          else if (current_index == 3)
            sol = sol + 'G';
          else if (current_index == 4)
            sol = sol + 'B';
          else if (current_index == 5)
            sol = sol + 'V';
        }
      }
      int maximum = 0;
      for (int i = 0; i < 6; i++){
        if (vec[i] > maximum && i != last_decreased){
          current_index = i;
          maximum = vec[i];
        }
        if (vec[i] == maximum && i != last_decreased && i == initial_index){
          current_index = i;
          maximum = vec[i];
        }
      }
    }
    // cout << sol << endl;
    if (possible && sol[0] != sol[sol.size()-1])
      cout << "Case #" << n_case << ": " << sol << endl;
    else
      cout << "Case #" << n_case << ": " << "IMPOSSIBLE" << endl;

  }

  return 0;
}
