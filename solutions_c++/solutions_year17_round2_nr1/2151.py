#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>

using namespace std;

long double solve(int D, int N) {
  map<int, int> hs;
  vector<int> positions;
 //// cout << "solve\n";
  for (int i = 0; i < N; ++i) {
    int pos;
    int speed;
    cin >> pos;
    cin >> speed;
    hs[pos] = speed;
    positions.push_back(pos);
 // cout << "pos " << pos << "speed" << speed << endl;
  }

  sort(positions.begin(), positions.end());
  //cout << "after sort\n";
  long double t = 0;
  for (int i = N-1; i >= 0; --i) {
      int pos = positions[i];
      int speed = hs[pos];
  //cout << "pos " << pos << "speed" << speed << endl;
      long double newTime = (D-pos+0.0)/(speed+0.0);
      //cout << "time: " << newTime << endl;
      if (i != N-1) {
         t = max(newTime, t);
      } else {
          t = newTime;
      }
  }

  long double res = D/t;
  //cout << "Res: " << res << endl;
  return res;
}

int main() {

    ofstream fout;
    fout.open("output.txt");

    if (fout.is_open()) {
        int D, N;

        int num_tests = 0;
        cin >> num_tests;

        unsigned count = 1;
        //fout.precision(8);
        while ( count <= num_tests ) {
            cin >> D >> N;
            fout << "Case #" << count << ": ";
            fout << fixed << setprecision(8) << solve(D, N) << endl; 
            count++;
        }
        fout.close();
    } else {
        cout << "Can't open file!";
    }
    return 0;
}