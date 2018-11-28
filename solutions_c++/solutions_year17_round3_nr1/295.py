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

#define NN 1000

using LL = long long int;
using namespace std;

int cas, ca;

double PI = 3.141592653589793;

struct Cake {
  LL r;
  LL h;
};

bool comp(Cake& a, Cake&b) {
  LL aa = a.r*a.h;
  LL bb = b.r*b.h;
  return aa>bb;
}
int N,K;
Cake ar[NN];
void main2() {
  cin>>N>>K;
  for (int i=0; i<N; ++i) {
    cin>>ar[i].r>>ar[i].h;
  }
  sort(ar, ar+N, comp);
  LL rtn = 0;
  for (int i=0; i<N; ++i) {
    int rem =K-1;
    LL cur = ar[i].r*2*ar[i].h+ar[i].r*ar[i].r;
    for (int j=0; j<N && rem > 0; ++j) {
      if (i==j) continue;
      Cake c = ar[j];
      if (c.r <= ar[i].r) {
        rem--;
        cur += c.r*2*c.h;
        if (rem ==0) break;
      }
    }
    if (rem > 0) continue;

    rtn =max(rtn, cur);
  }
  printf ("%.8f\n", PI * rtn);


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
