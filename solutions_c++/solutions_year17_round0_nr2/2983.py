#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;

typedef pair<ll,int> plli;
typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 20

char S[MAXN];

int main() {
  int TEST;
  scanf("%d",&TEST);
  FOR(test,TEST) {
    memset(S,0,sizeof(S));
    scanf("%s", &S[0]);

    int N = strlen(S);

    FOR(i,N-1) {
      if (S[i] > S[i+1]) {
        int j = i;
        while(j>0 && S[j-1] == S[j]) --j;
        assert(S[j] > '0');
        S[j]--;
        for (int k = j+1; k<N; ++k) {
          S[k] = '9';
        }

        break;
      }
    }

    char * ans = &S[0];
    while(*ans == '0') ++ans;
    printf("Case #%d: %s\n",test+1,ans);
  }
}






