#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  freopen("/Users/Derek/Documents/Programming/Live Contests/Code Jam 2017/Qualification/B-large.in", "r", stdin);
  freopen("/Users/Derek/Documents/Programming/Live Contests/Code Jam 2017/Qualification/P2large.out", "w", stdout);
  int t;
  string n;
  scanf("%i", &t);

  for (int zzz = 0; zzz < t; zzz ++) {
    cin >> n;
    string m = n;

    for (int i = 1; i < n.length(); i ++) {
      if (n[i] < n[i-1]) {
        for (int j = i; j < n.length(); j ++)
          n[j] = '9';
        if (n[i-1] == '0')
          n[i-1] = '9';
        else
          n[i-1] --;

        break;
      }
    }

    for (int i = n.length() - 1; i > 0; i --) {
      if (n[i] < n[i-1]) {
        n[i] = '9';
        if (m[i-1] == '0')
          n[i-1] = '9';
        else
          n[i-1] --;
      }
    }

    bool started = false;
    printf("Case #%i: ", zzz + 1);
    for (int i = 0; i < n.length(); i ++) {
      if (n[i] != '0' && !started) {
        started = true;
      }
      if (started) {
        printf("%i", n[i] - '0');
      }
    }
    printf("\n");
  }
}
