#include <cstdio>
#include <cstring>
#include <cstdio>
#include <string>
using namespace std;

string benerin(string s) {
  int n = s.length();
  bool ok = 1;
  for(int i = 0;i < n-1;++i) {
    if(s[i] > s[i+1]) {
      ok = 0;
      for(i=i+1;i < n;++i) s[i] = '0';
    }
  }

  long long X;
  sscanf(s.c_str(), "%lld", &X);

  if(!ok) {
    --X;
    char p[25]; sprintf(p, "%lld", X);
    return benerin(p);
  } else
    return s;
}

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1;t <= T;++t) {
    printf("Case #%d: ", t);

    char s[25];
    scanf("%s", s);
    printf("%s\n", benerin(s).c_str());
  }
}
