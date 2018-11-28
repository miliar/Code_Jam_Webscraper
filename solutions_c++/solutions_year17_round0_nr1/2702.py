#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
  if(argc != 2) 
    return -1;

  ifstream in {argv[1]};
  bool cakes[1000];
  int loops;
  int size;
  string temp;
  int ncakes;
  int loop = 0;
  for(in >> loops; loops > 0; --loops) {
    in >> temp >> size;
    ncakes = temp.length();
    for(int i = 0; i < ncakes; i++) {
      cakes[i] = (temp[i] == '+' ? true : false);
    }


    int flips = 0;
    for(int i = 0; i + size <= ncakes; ++i) {
      if(!cakes[i]) {
        flips++;
        for(int j = 0; j < size; ++j) {
          cakes[i+j] = !cakes[i+j];
        }
      }
      //for(int a = 0; a < ncakes; a++) {
        //cout << (cakes[a] ? '+' : '-');
      //}
      //cout << endl;
    }
    bool check = true;
    for(int i = 0; i < size; ++i) {
      check = check && cakes[ncakes - 1 - i];
    }

    cout << "Case #" << ++loop << ": " << (check ? to_string(flips) : "IMPOSSIBLE") << endl;
  }

  
}
