#include <iostream>
#include <string>

using namespace std;

int cas, N, H, p, s;
double timex, maxx;

int main() {
  cin>>cas;

  for (int k=1; k<=cas; ++k) {
    cin>>N>>H;
    maxx = 0;
    for (int i=0; i<H; ++i) {
      cin>>p>>s;
      timex = N-p;
      timex = timex/s;
      if (timex>maxx) maxx=timex;
    }
    cout<<"Case #"<<k<<": ";
    printf("%.6lf\n", N/maxx);
  }
  return 0;
}


