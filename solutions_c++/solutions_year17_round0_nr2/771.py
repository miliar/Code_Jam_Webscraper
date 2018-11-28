#include <iostream>

using namespace std;

unsigned long long sol(unsigned long long num) {
  if (num<10) return num;

  unsigned long long ret, m;
  int x, y;

  while (1) {
    ret = num;
    m = 1;
    x = -1;
    y = -1;

    while (1) {
      if (ret<10) {x=y=-1; break;}
      x = (ret/10)%10;
      y = ret%10;
      if (x>y) {
        num = num/m*m;
        break;
      }
      ret = ret/10;
      m = m*10;
    }
    if (x<0 || y<0) break;

    num = num - m*y - 1;
  }
  return num;
}


int main() {
  int cas;
  unsigned long long num;

  cin>>cas;
  for (int k=1; k<=cas; ++k) {
    cin>>num;
    cout<<"Case #"<<k<<": "<<sol(num)<<endl;
  }
  return 0;
}
