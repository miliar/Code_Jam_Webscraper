#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <iomanip>

using namespace std;

int main() {
  int T; cin>>T;

  for(int t=1; t<=T; t++){
    double dest;
    int n;
    cin>>dest>>n;
    double ans=1e18;
    for(int i=0; i<n; i++){
      double start,speed; cin>>start>>speed;
      double finish = (dest-start) / speed;
      ans=min(ans, dest/finish);
    }
    printf("Case #%d: %.9lf\n", t, ans);
  }
}
