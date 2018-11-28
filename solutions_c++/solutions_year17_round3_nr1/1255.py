#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

bool cmp(pair<int64_t, int64_t> a, pair<int64_t, int64_t> b) {
  if(a.first == b.first) return a.second > b.second;
  return (a.first > b.first);
}

bool cmp2(pair<int64_t, int64_t> a, pair<int64_t, int64_t> b) {
  return a.second > b.second;
}

void solve(istream& ifile) {
  double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;
  int T = 0;
  ifile >> T;

  for(int i = 0; i < T; ++i) {
    int N = 0;
    int K = 0;
    vector<pair<int64_t, int64_t> > PANCAKE;
    double ans = 0.0;
    ifile >> N >> K;
    for(int j = 0; j < N; ++j) {
      int64_t R = 0;
      int64_t H = 0;
      ifile >> R >> H;
      PANCAKE.push_back(make_pair(R*R, 2*H*R));
    }
    sort(PANCAKE.begin(), PANCAKE.end(), cmp);

    int l = PANCAKE.size();
    /*cerr << "===========" << endl;
    for(int j = 0; j < l; ++j) {
      cerr << PANCAKE[j].first << ' ' << PANCAKE[j].second << endl;
    }
    cerr << "===========" << endl;*/
    for(int j = 0; j < (l-K+1); ++j) {
      double tmpans = PANCAKE[j].first + PANCAKE[j].second;
      vector<pair<int64_t, int64_t> > tmp(l-j-1);
      copy(PANCAKE.begin()+j+1, PANCAKE.end(), tmp.begin());
      sort(tmp.begin(), tmp.end(), cmp2);
      for(int k = 0; k < (K-1); ++k) {
        tmpans += tmp[k].second;
      }
      if(tmpans > ans) ans = tmpans;
    }
    ans = ans * pi;
    cout << "Case #" << (i+1) << ": " << fixed << setprecision(10) << ans << endl;
  }
}

int main(int argc, char** argv) {
  if(argc != 2) {
    cerr << "Wrong usage." << endl;
    return 0;
  }
  ifstream ifile(argv[1]);

  solve(ifile);

  return 0;
}
