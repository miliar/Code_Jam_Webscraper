#include <bits/stdc++.h>

#define NN 1000

using LL = long long int;
using namespace std;

int cas, ca;

int n,p;
int ar[4];
bool left;


void main2() {
  memset(ar, 0, sizeof(ar));
  cin>>n>>p;
  int x;
  for (int i=0; i<n; ++i) {
    cin>>x;
    ar[x%p]++;
  }
  int tot = ar[0];

  if (p == 2) {
    tot += ar[1]/2 + (ar[1]%2);
  }

  if (p == 3) {
    int mi = min(ar[1], ar[2]);
    int mx = max(ar[1], ar[2]) - mi;
    tot += mi;
    tot+= mx/3;
    if (mx %3) tot++;
  }

  if (p==4) {
    int mi = min(ar[1], ar[3]);
    int mx = max(ar[1], ar[3]) - mi;
    tot += mi;

    mi = min(mx/2, ar[2]);
    tot += mi;
    ar[2] -= mi;
    mx -= 2*mi;

    tot += ar[2]/2;
    ar[2] %= 2;

    tot += mx/4;
    mx %= 4;

    if (mx || ar[2]) tot++;
  }


  cout<<tot<<endl;
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
