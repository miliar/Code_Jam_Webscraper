// Oversized Pancake Flipper Google Code Jam 2017

#include <bitset>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

void printIt(const vector<bool> & v) {
  string s = "";
  for (bool b : v) {
    s += (b ? "1" : "0");
  }
  cout << s << endl;
}

struct Path {
  vector<bool> bits;
  long fsize;

  Path(const vector<bool> & b, long flipperSize) {
    bits = b;
    fsize = flipperSize;
  }

  long flipThem() {
    long num = 0;
    for (long i = 0; i < bits.size() - fsize + 1; ++i) {
      if (bits[i]) continue;
      flip(i);
      //cout << " flip " << i << " ";
      //printIt(bits);
      num++;
    }

    return allFlipped() ? num : -1;
  }

  // flip 
  void flip(long index) {
    for (long i = index; i < (index + fsize); ++i) {
      bits[i] = !bits[i];
    }
  }


  bool allFlipped() {
    for (auto i : bits) {
      if (!i) {
	return false;
      }
    }
    return true;
  }

};

void run() {
  string input;
  getline(cin, input);
  long count = atoi(input.c_str());
  for (long i = 0; i < count; ++i) {
    getline(cin, input);
    string pancakes = strtok((char*)(input.c_str()), " ");
    string flipperSize = strtok(0, " ");
    long fsize = atoi(flipperSize.c_str());
    //cout << "pancakes: " << pancakes << " size: " << fsize << endl;

    const size_t len = pancakes.size();
    vector<bool> bits(len, false);
    for (int j = 0; j < len; ++j) {
      bits[j] = ((input[j] == '-') ? false : true);      
    }
    Path p(bits, fsize);
    //printIt(p.bits);
    long flips = p.flipThem();
    cout << "Case #" << (i+1) << ": ";
    if (flips >= 0) {
      cout << flips;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
}

int main(int argc, const char* argv[]) {
  run();
}

  
