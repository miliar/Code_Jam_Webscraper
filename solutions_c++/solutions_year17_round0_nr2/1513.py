#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    int T; cin>>T;
    for (int tt = 1; tt <= T; tt++) {
      long long N; cin>>N;
      char str[20];
      int d = 1;
      while(d) {
        sprintf(str,"%lld", N);
        int pos = 1;
        while (str[pos] && str[pos-1] <= str[pos]) {
          pos++;
        }
        d = strlen(str) - pos;
        if (d) {
          long long m =1;
          for (int i = 0; i < d; i++) {
            m *= 10;
          }
          N = (N/m-1)*m + (m-1);
        }
      }
      cout << "Case #"<<tt<<": "<<N<<"\n";
    }
}
