#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>

using namespace std;

vector<long long> split(long long N) {
  vector<long long> ret;
  while (N>0) {
    // N is reversed
    ret.push_back(N % 10);
    N/=10;
  }
  return ret;
}

void output(const vector<long long> &v,long long idx) {
  for (long long i=v.size()-1;i>=0;i--) {
    if (i > idx) std::cout << v[i];
    else if (i == idx) {
      if (v[i] == 1 && idx == v.size()-1) {
      } else {
        std::cout << v[i]-1;
      }
    }
    else std::cout << 9;
  }
}

int main(int argc, char *argv[]) {
  // std::ifstream ifs("a.txt");
  std::ifstream ifs(argv[1]);
  assert(ifs.is_open());
  long long t;
  ifs >> t;
  for (long long num=0;num<t;num++) {
    long long N;
    ifs >> N;
    vector<long long> v = split(N);
    // std::cout << v << "\n";
    // for (long long a : v) std::cout << a;
    // std::cout << "\n";
    long long i;
    int backpointer=v.size()-1;
    for (i=v.size()-1;i>0;i--) {
      if (v[i] > v[i-1]) {
        // std::cout << (v[i]-1)*pow(10,i-1)-1 << "\n";
        std::cout << "Case #" << num+1 << ": ";
        output(v,backpointer);
        std::cout << "\n";
        break;
      } else if (v[i] < v[i-1]) {
        backpointer = i-1;
      }
    }
    if (i==0) {
      std::cout << "Case #" << num+1 << ": " << N << "\n";
    }
  }
}
