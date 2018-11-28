// Tidy Numbers Google Code Jam 2017

#include <stdlib.h>

#include <bitset>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>


using namespace std;


bool isTidy(const string & s) {
  for (size_t i = 0; i < s.length()-1; ++i) {
    if (s[i] > s[i+1]) return false;
  }
  return true;
}

struct Path {
  string input;

  Path(const string & b) {
    input = b;
  }

  void calcTidyNum(string & tidy) {
    //cout << "calcTidyNum\n";
    tidy = input;
    for (size_t i = 0; i < tidy.length() - 1; ++i) {
      //cout << "index: " << i << endl;
      long j = i;
      if (tidy[i] > tidy[i+1]) {
        //cout << i << " " << (i + i) << endl;
        // set rest to nines
        // borrow backwards
        for ( j = i; j >= 0; --j) {
          tidy[j] -= 1;
          //cout << "set tidy[" << j <<"]" << endl;
          if (j != 0 && (tidy[j-1] <= tidy[j])) {
            break;
          }
          if (j == 0) break; // preserve j
        }
        j++;
        //cout << "j is now " << j << endl;
        for(; j < tidy.length(); ++j) {
          tidy[j] = '9';
        }

        return;
      }
    }

  }

};

void run() {
  string input;
  getline(cin, input);
  long count = atoi(input.c_str());
  for (long i = 0; i < count; ++i) {
    getline(cin, input);
    Path p(input);
    string tidy;
    p.calcTidyNum(tidy);

    size_t pos = 0;
    for (char c : tidy) {
      if (c == '0') {
        pos++;
      } else {
        break;
      }
      tidy = tidy.substr(pos);
    }

    cout << "Case #" << (i+1) << ": " << tidy << endl;

/*
    long long submit = stoll(tidy);
    long long ll = stoll(input);
    while (!isTidy(input)) {
      --ll;
      input = to_string(ll);
    }
    cout << "real answer: " << ll << endl;
    if (ll != submit) {
      cout << "##### ERROR, input was: " << input << endl;
    }
    */
  }
}

int main(int argc, const char* argv[]) {
  run();
}

  
