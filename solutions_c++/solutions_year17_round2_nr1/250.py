#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int main(){
  const int c = getInt();

  REP(cc,c){
    const int d = getInt();
    const int n = getInt();

    double t = 0;
    REP(i,n){
      const int k = getInt();
      const int s = getInt();
      t = max(t, (double)(d - k) / s);
    }

    printf("Case #%d: %.10f\n", cc + 1, d / t);
  }

  return 0;
}
