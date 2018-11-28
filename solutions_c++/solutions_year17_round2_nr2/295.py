#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, char> pic;

#define F first
#define S second

char sol[1005];

int main()
{
  int T;
  scanf("%d", &T);
  
  for (int t = 1; t <= T; t++)
  {
    printf("Case #%d: ", t);

    int N, R, O, Y, G, B, V;
    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

    if (2 * R > N || 2 * Y > N || 2 * B > N)
    {
      printf("IMPOSSIBLE\n");
      continue;
    }

    vector<pic> vec;
    vec.push_back(pic(R, 'R'));
    vec.push_back(pic(Y, 'Y'));
    vec.push_back(pic(B, 'B'));
    sort(vec.begin(), vec.end());
    reverse(vec.begin(), vec.end());

    int m0 = vec[0].F, m1 = vec[1].F, m2 = vec[2].F;
    char c0 = vec[0].S, c1 = vec[1].S, c2 = vec[2].S;
    sol[N] = '\0';

    int i;
    for (i = 0; m0; i += 2, m0--)
      sol[i] = c0;

    for (; i < N; i += 2, m1--)
      sol[i] = c1;

    for (i = 1; m1; i += 2, m1--)
      sol[i] = c1;

    for (; m2; i += 2, m2--)
      sol[i] = c2;

    printf("%s\n", sol);
  }

  return 0;
}
