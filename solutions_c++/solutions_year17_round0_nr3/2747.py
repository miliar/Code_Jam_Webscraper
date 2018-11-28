#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

const int MAGIC = 1000000;

int main(int argc, char** argv) {
  if(argc != 2) 
    return -1;
  

  ifstream in {argv[1]};
  int loops;
  int loop = 0;
  map<long long int, long long int, greater<long long int>> holes;

  for(in >> loops; loops > 0; --loops) {
    long long int n, k;
    in >> n >> k;

    holes.clear();
    holes[n] = 1;

    long long int i = 0;
    long long int a;
    while(i < k) {
      a = holes.begin()->first;
      long long int b = holes[a];
      holes.erase(holes.begin());

      holes[a/2] += b;
      holes[(a-1)/2] += b;

      i+= b;
    }

    cout << "Case #" << ++loop << ": " << max(a/2, (a-1)/2) << " " << (min(a/2, (a-1)/2)) << endl;
  }

  
}
