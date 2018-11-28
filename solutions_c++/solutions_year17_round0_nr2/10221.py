#include <bits/stdc++.h>

using namespace std;

bool checkasc(int x)
{
  string alpha = to_string(x);
  int last, now;
  last = alpha[0] - '0';
  for(int i = 1; i < alpha.size(); ++i)
  {
    if(alpha[i] - '0' < last) return false;
    last = alpha[i] - '0';
  }
  return true;
}

int main(){
  int t;
  scanf("%d", &t);
  for(int k = 1; k <= t; ++k)
  {
    int x, i;
    scanf("%d", &x);
    for(i = x; i >= 0; i--)
      if(checkasc(i)) break;

    printf("Case #%d: %d\n", k, i);

  }
  return 0;
}
