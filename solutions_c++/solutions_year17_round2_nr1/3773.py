#include <bits/stdc++.h>
#define min(a,b) (((a) < (b)) ? (a) : (b))
#define max(a,b) (((a) > (b)) ? (a) : (b))
using namespace std;
long long int n, d, k, H[1001][2];

int main(){
  int tc, c=1;
  scanf("%d", &tc);
  while (tc--) {
    cin >> d >> n;
    long double minTime = 0;
    for(int i = 0; i<n; i++){
      cin>> H[i][0]>>H[i][1];
      minTime = max(minTime, (long double)(d-H[i][0])/(H[i][1]*1.0));
    }
    cout.precision(6);
    std::cout << "Case #" << c++ <<": " << fixed << d/minTime << std::endl;
}

}
