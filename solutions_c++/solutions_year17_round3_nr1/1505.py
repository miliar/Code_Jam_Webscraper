#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
typedef long long ll;

int T, N, K;
double pi = 3.14159265358979323846;
struct cake{
  double r;
  double h;
  double rh;
};
cake c[1100];

bool compare1(cake c1, cake c2){
  if(c1.r == c2.r)  return c1.h < c2.h;
  else return c1.r < c2.r;
}
bool compare2(cake c1, cake c2){
  return c1.rh < c2.rh;
}

int main(){
  cin >> T;
  for(int i2 = 1; i2 <= T; i2++){
    cin >> N >> K;
    for(int i = 0; i < N; i++){
      cin >> c[i].r >> c[i].h;
      c[i].rh = c[i].r*c[i].h;
    }

    sort(c, c+N, compare1);
    cake tmp[1100];

    double ma = 0;
    for(int i = N-1; i >= K-1; i--){
      for(int i = 0; i < N; i++)  tmp[i] = c[i];
      sort(tmp, tmp+i, compare2);
      double sum = c[i].rh;
      for(int j = 0; j < K-1; j++){
        sum += tmp[i-j-1].rh;
        //cout << tmp[i-j-1].rh << endl;
      }
      sum = (sum*2 + c[i].r*c[i].r)*pi;
      ma = max(ma, sum);
      //cout << sum/pi << " " << i << endl;
    }

    cout << "Case #" << i2 << ": ";
    printf("%.9f", ma); cout << endl;
  }

    return 0;
}
