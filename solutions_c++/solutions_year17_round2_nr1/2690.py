#include "mylib.h"



void solve(int t, mifstream &fi, mofstream &fo) {
  double d=fi.nextInt();
  int n=fi.nextInt();
  double maxtime=0.0;
  for (int i=0; i<n; i++) {
    double k=fi.nextInt();
    double s=fi.nextInt();
    double timeleft=(d-k)/s;
    if (timeleft>maxtime) maxtime=timeleft;
  }
  double maxspeed=d/maxtime;
  fo<<"Case #"<<t<<": "<<std::fixed<<std::setprecision(6)<<maxspeed<<endl;
}


/*
3

2525 1
2400 5

300 2
120 60
60 90

100 2
80 100
70 10
*/

int main(int ac, char *av[]) {
  return mainx(ac, av, [](int t, mifstream &fi, mofstream &fo) {
    solve(t, fi, fo);
  });
}

