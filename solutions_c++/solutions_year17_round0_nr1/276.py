#include <cstdio>
#include <cassert>
#include <cstring>
#include <queue>

using namespace std;

void run() {
  char s[2000];
  scanf("%1999s",s);
  int len=strlen(s);
  int k;
  scanf("%d", &k);
  int sol=0;
  deque<int> rotend;
  int i;
  for (i=0;i<k && i+k<=len;++i) {
    if (s[i]=='+') {
      if (int(rotend.size())%2==1) {
	rotend.push_back(i+k);
	++sol;
      }
    } else if (s[i]=='-') {
      if (int(rotend.size())%2==0) {
	rotend.push_back(i+k);
	++sol;
      }
    } else assert(false);
  }
  for (;i+k<=len;++i) {
    while (!rotend.empty() && rotend.front()<=i) rotend.pop_front();
    if (s[i]=='+') {
      if (int(rotend.size())%2==1) {
	rotend.push_back(i+k);
	++sol;
      }
    } else if (s[i]=='-') {
      if (int(rotend.size())%2==0) {
	rotend.push_back(i+k);
	++sol;
      }
    } else assert(false);
  }
  for (;i<len;++i) {
    while (!rotend.empty() && rotend.front()<=i) rotend.pop_front();
    assert(s[i]=='+' || s[i]=='-');
    if (s[i]=='+' && int(rotend.size())%2==1 ||
	s[i]=='-' && int(rotend.size())%2==0) {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  printf("%d\n",sol);
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
  }
  return 0;
}
