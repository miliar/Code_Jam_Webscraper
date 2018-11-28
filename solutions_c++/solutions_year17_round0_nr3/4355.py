#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdint>

using namespace std;

//------------------------------------------------------
// helper functions
/*
  Description:
  Convert the integer part of a double to an integer string.

  Input:
  d: double, always assumed non-negative

  Output:
  S: integer part stored as string
*/
string double2str_int(double d) {
  string S;
  if(d == 0) {
    return "0";
  }else{
    int N = log10(d);
    for (int i = 0; i <= N; i++) {
      S += to_string( int( fmod(d/pow(10.0, N-i), 10.0) ) );
    }
    return S;
  }
}

//------------------------------------------------------


int main(int argc, char const *argv[]) {
  int T = 0;
  string N_str, K_str;
  double N_d, K_d;
  double fractpart;

  cin >> T; // number of test cases
  for (int i = 1; i <= T; ++i) {
    cin >> N_d; // read N as double
    cin >> K_d; // read K as double

    // Count the levels of the binary tree
    int logk1 = floor(log2(K_d+1));
    int logk2 = ceil(log2(K_d+1));

    // Make sure there are two levels
    if(logk1 == logk2) logk1 -= 1;

    // Get the average bath stall distances at the level of logk1
    double L_logk1 = (N_d+1)/pow(2.0,logk1) - 1;
    // Split L_logk1 into integer part and fractional part
    double int_L_logk1;
    fractpart = modf(L_logk1, &int_L_logk1);
    // Count how many distances have an additional plus 1
    double num_of_plus_1 = fractpart * pow(2.0,logk1);

    // logk1 is the level for the parent of the leaf nodes
    // logk2 is the level for the leaf nodes
    // Get the number of nodes that have lower leaves
    double num_lower = K_d + 1 - pow(2.0,logk1);

    // Look at the last node at level logk1 that has lower leaves
    double int_L_logk2;
    if (num_lower > num_of_plus_1) {
      fractpart = modf((int_L_logk1-1)/2.0, &int_L_logk2);
    }else{
      fractpart = modf(int_L_logk1/2.0, &int_L_logk2);
    }

    if(fractpart == 0) {
      cout << "Case #" << i << ": " << double2str_int(int_L_logk2) << " " << double2str_int(int_L_logk2) << endl;
    }else {
      cout << "Case #" << i << ": " << double2str_int(int_L_logk2+1) << " " << double2str_int(int_L_logk2) << endl;
    }

  }
  return 0;
}
