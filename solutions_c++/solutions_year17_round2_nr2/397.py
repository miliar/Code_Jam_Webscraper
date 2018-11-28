#include <iostream>
#include <stdio.h>
#include <assert.h>
using namespace std;

std::string answer;
char color[6];
struct Counter {
  int n;
  int tc;
};

int tmp[2000];
int main()
{
  int numTests, N, c[6];
  color[0] = 'R';
  color[1] = 'O';
  color[2] = 'Y';
  color[3] = 'G';
  color[4] = 'B';
  color[5] = 'V';
  cin >> numTests;
  for (int test = 1; test <= numTests; test++) {
    cin >> N;
    int nc = 0;
    answer = "";
    for (int i = 0; i < 6; i++) {
      cin >> c[i];
      if(c[i] > 0) nc++;
    }
    if (nc == 1) {
      if (N == 1) {
        for (int i = 0; i < 6; i++)
          if (c[i] > 0)
            answer = answer + color[i];
      } else {
        answer = "IMPOSSIBLE";
      }
    } else if (nc == 2) {
      int cnt = 0;
      int x[2];
      for (int i = 0; i < 6; i++) 
        if (c[i] > 0) {
          x[cnt] = i;
          cnt++;
        }
      if ((c[x[0]] != c[x[1]]))
        answer = "IMPOSSIBLE";
      else if ((x[0] % 2 == 0 && x[1] % 2 == 0) || (x[0] + 3) % 6 == x[1]) {
        for (int i = 0; i < N; i++)
          answer = answer + color[x[i%2]];
      } else
        answer = "IMPOSSIBLE";
    } else {
      bool okay = true;
      Counter d[4];
      for (int i = 0; i < 6; i+=2) {
        if (c[(i + 3)%6] >= c[i])
          okay = false;
        d[i / 2].n = c[i] - c[(i+3)%6];
        d[i / 2].tc = i;
      }
      for (int i = 0; i < 3; i++)
        for (int j = i+1; j < 3; j++)
          if (d[i].n > d[j].n) {
            d[3] = d[i]; d[i] = d[j]; d[j] = d[3];
          }
      if (d[0].n + d[1].n < d[2].n)
        okay = false;
      if (!okay)
        answer = "IMPOSSIBLE";
      else {
        int bc = (d[0].n - (d[2].n - d[1].n)) / 2;
        int ac = bc + d[2].n - d[1].n;
        int ab = d[2].n - ac;
        //cout << bc << " " << ac << " " << ab << endl;
        assert(ab + bc == d[1].n);
        int cnt = 0;
        for (int i = 0; i < ac; i++) {
          tmp[cnt] = d[2].tc; cnt++;
          tmp[cnt++] = d[0].tc;
        }
        for (int i = 0; i < bc; i++) {
          tmp[cnt++] = d[1].tc;
          tmp[cnt++] = d[0].tc;
        }
        for (int i = 0; i < ab; i++) {
          tmp[cnt++] = d[2].tc;
          tmp[cnt++] = d[1].tc;
        }
        if (bc + ac < d[0].n) {
          assert(bc + ac == d[0].n - 1);
          tmp[cnt++] = d[0].tc;
        }
        bool been[6];
        been[0] = been[2] = been[4] = false;
        for (int i = 0; i < cnt; i++) {
          if (tmp[i] % 2 == 0 && !been[tmp[i]]) {
            been[tmp[i]] = true;
            for (int j = 0; j < c[(tmp[i] + 3) %6]; j++) {
              answer += color[tmp[i]];
              answer += color[(tmp[i] + 3) % 6];
            }
          }
          answer += color[tmp[i]];
        }
      }
    }
    cout << "Case #" << test << ": " << answer << endl;
  }
}
