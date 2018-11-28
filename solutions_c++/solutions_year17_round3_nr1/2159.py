// #include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
std::ifstream cin("../A-small-attempt3.in.txt");
std::ofstream cout("As.out");

const double PI = 3.1415926535897932384626433832795;

class Pie {
public:
  int r, h;

  Pie (int ra, int he) {
    r = ra;
    h = he;
  }
};

bool comp (const Pie &p1, const Pie &p2) {
  bool res = p1.r < p2.r;
  if (p1.r == p2.r) {
    res = p1.h < p2.h;
  }
  return res;
}

double solveCase() {
  int n, k;
  cin >> n >> k;

  vector<Pie> parr;

  for (int i = 0; i < n; i++) {
    int tmpR, tmpH;
    cin >> tmpR >> tmpH;
    Pie *newp = new Pie(tmpR, tmpH);
    parr.push_back(*newp);
  }

  sort(parr.begin(), parr.end(), comp);

  while (parr.size() > k) {
    vector<Pie>::iterator it, todel;
    double loss = 0;
    for (it = parr.begin(); it != parr.end(); it++) {
      double tmploss = 2*(double)it->r*(double)it->h*PI;
      if (it+1 == parr.end()) {
        double r2 = it->r, r1 = (it-1)->r;
        tmploss += r2*r2*PI - r1*r1*PI;
      }
      if (tmploss < loss || loss == 0) {
        loss = tmploss;
        todel = it;
      }
    }
    parr.erase(todel);
  }

  double res = (double)parr[k-1].r*(double)parr[k-1].r*PI;
  for (vector<Pie>::iterator it = parr.begin(); it != parr.end(); it++) {
    res += 2*(double)it->h*(double)it->r*PI;
  }

  // cout << "!!!" << parr[k-2].r << endl;
  return res;
}

int main() {
  int tcn;
  cin >> tcn;
  cout << std::fixed;
  for (int i = 1; i <= tcn; i++) {
    cout << "Case #" << i << ": " << solveCase() << std::endl;
  }
}
