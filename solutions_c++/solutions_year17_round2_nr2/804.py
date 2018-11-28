#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

const char xA = 'R';
const char xAB = 'O';
const char xB = 'Y';
const char xBC = 'G';
const char xC = 'B';
const char xCA = 'V';

bool solve1(char *s, int A, int BC, char xA, char xBC) {
  if (A == BC) {
    for (int i = 0; i < A; i++) {
      s[i*2] = xA;
      s[i*2+1] = xBC;
    }
    return true;
  }
  return false;
}

bool solve3A(char *s, int A, int B, int C, int xA, int xB, int xC) {
  if (A > B+C)
    return false;
  int j = 0;
  for (int i = 0; i < A; i++) {
    s[j++] = xA;
    if (i < B)
      s[j++] = xB;
    if (A-C <= i)
      s[j++] = xC;
  }
  return true;
}

bool solve3(char *s, int A, int B, int C) {
  if (A >= max(B, C)) {
    return solve3A(s, A, B, C, xA, xB, xC);
  }
  if (B >= max(C, A)) {
    return solve3A(s, B, C, A, xB, xC, xA);
  }
  if (C >= max(A, B)) {
    return solve3A(s, C, A, B, xC, xA, xB);
  }
  fprintf(stderr, "hoge\n");
  return false;
}

void ins(char *s, char xA, int BC, char xBC) {
  char *p = strchr(s, xA);
  int n = strlen(p+1);
  memmove(p+1+BC*2, p+1, n);
  for (int i = 0; i < BC; i++) {
    p[1+i*2] = xBC;
    p[1+i*2+1] = xA;
  }
}

bool solve(char *s, int A, int AB, int B, int BC, int C, int CA) {
  if (AB == 0 && B == 0 && C == 0 && CA == 0)
    return solve1(s, A, BC, xA, xBC);
  if (BC == 0 && C == 0 && A == 0 && AB == 0)
    return solve1(s, B, CA, xB, xCA);
  if (CA == 0 && A == 0 && B == 0 && BC == 0)
    return solve1(s, C, AB, xC, xAB);
  if ((BC > 0 && A <= BC) || (CA > 0 && B <= CA) || (AB > 0 && C <= AB))
    return false;
  bool res = solve3(s, A-BC, B-CA, C-AB);
  if (!res)
    return false;
  if (BC > 0) {
    ins(s, xA, BC, xBC);
  }
  if (CA > 0) {
    ins(s, xB, CA, xCA);
  }
  if (AB > 0) {
    ins(s, xC, AB, xAB);
  }
  return true;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, A, AB, B, BC, C, CA;
    cin >> N >> A >> AB >> B >> BC >> C >> CA;
    char s[1010] = {};
    bool res = solve(s, A, AB, B, BC, C, CA);
    if (res) {
      printf("Case #%d: %s\n", i+1, s);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", i+1);
    }
  }
}
