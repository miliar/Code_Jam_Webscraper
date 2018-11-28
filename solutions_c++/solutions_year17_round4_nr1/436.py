#include <iostream>
#include <algorithm>
using namespace std;
int main() {
  int T;
  cin >> T;

  for(int t=1; t<=T; t++) {
    int N,P;
    cin >> N >> P;
    int a[4];
    a[0]=0;
    a[1]=0;
    a[2]=0;
    a[3]=0;
    for(int i=0; i<N; i++) {
      int x;
      cin >> x;
      a[x%P]++;
    }

    int z=0;

    if (P==2) {
      z+=a[0];
      a[0]=0;

      int m=a[1]/2;
      z+=m;
      a[1]-=2*m;

      if (a[0]+a[1]>0)
	z++;
    } else if (P==3) {
      z+=a[0];
      a[0]=0;

      int m=min(a[1],a[2]);
      z+=m;
      a[1]-=m;
      a[2]-=m;

      int n=a[1]/3;
      z+=n;
      a[1]-=3*n;

      n=a[2]/3;
      z+=n;
      a[2]-=3*n;

      if (a[0]+a[1]+a[2]>0)
	z++;
    } else if (P==4) {
      z+=a[0];
      a[0]=0;

      int m=min(a[1],a[3]);
      z+=m;
      a[1]-=m;
      a[3]-=m;

      int n=a[2]/2;
      z+=n;
      a[2]-=2*n;

      n=min(a[2],a[1]/2);
      z+=n;
      a[2]-=n;
      a[1]-=2*n;

      n=min(a[2],a[3]/2);
      z+=n;
      a[2]-=n;
      a[3]-=2*n;

      n=a[1]/4;
      z+=n;
      a[1]-=4*n;

      n=a[3]/4;
      z+=n;
      a[3]-=4*n;
      
      if (a[0]+a[1]+a[2]+a[3]>0)
	z++;
    }
    cout << "Case #" << t << ": " << z << endl;
  }
  return 0;
}
