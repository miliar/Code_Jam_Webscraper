#include<algorithm>
#include<cassert>
#include<cstring>
#include<iostream>
#include<list>
#include<map>
#include<set>
#include<sstream>
#include<string>
#include<unordered_map>
#include<unordered_set>
#include<utility>
#include<vector>
#include<cmath>

#define NN 50

using LL = long long int;
using namespace std;

int cas, ca;
double ar[NN];

void main2() {
  int n,k;
  cin>>n>>k;
  double unit;
  cin>>unit;
  for (int i=0; i<n; ++i) {
    cin>>ar[i];
  }
  sort(ar, ar+n);
  ar[n] = 1;
  n++;
  for (int i=1; i<n; ++i) {
    double diff = ar[i]- ar[i-1];
    double fill = 0;
    bool done = false;
    if (diff * i <= unit) {
      fill = diff;
    } else {
      fill = unit / i;
      done = true;
    }

    for (int j=0; j<i; ++j) {
      ar[j] += fill;
      unit -= fill;
    }
    if (done) break;
  }
  double rtn = 1;
  for (int i=0; i<n; ++i) {
    rtn *= ar[i];
  }

  printf("%.7f\n", rtn);
}

int main(int argc, char *argv[]) {
  cin>>cas;
  bool showtime = argc > 1;
  time_t starttime = 0;
  if (showtime) {
    time(&starttime);
  }
  for(ca = 1; ca<=cas; ++ca) {
    if (showtime) {
      cerr<<ca<<"/"<<cas<<" "<<time(NULL) - starttime<<endl;
    }
    cout<<"Case #"<<ca<<": ";
    main2();
  }
}
