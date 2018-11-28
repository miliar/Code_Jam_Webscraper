#include "mylib.h"


int solve(string t, size_t k) {
  charp s=(charp)t.c_str();
  size_t s_len=strlen(s);
  size_t count=0;
  // find first '-'
  for (size_t i=0; i<s_len; i++) {
    if (s[i]=='+') continue;
    if (i+k>s_len) return -1; // impossible
    // flip once
    count++;
    for (size_t j=0; j<k; j++) {
      s[i+j]^=('+'^'-');
    }
  }
  return (int)count;
}



int main(int ac, char *av[]) {
  return mainx(ac, av, [](int i, mifstream &fi, mofstream &fo) { 
    // solve(i, fi, fo); 
    string text=fi.nextString();
    size_t count=fi.nextInt();
    int result=solve(text,count);
    fo<<"Case #"<<i<<": ";
    if (-1<result) { fo<<result; }
    else { fo<<"IMPOSSIBLE"; }
    fo<<endl;
  });
}

