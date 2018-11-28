#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  ll T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    string num;
    cin >> num;
    const int sz = num.size();
    for (int i = 0; i < sz - 1; i++)
      if (num[i] > num[i + 1]) {
        int base = i;
        while (base >= 0 && num[base] == num[i])
          base--;
        base++;

        num[base]--;
        for (int j = base + 1; j < sz; j++)
          num[j] = '9';
        break;
      }
    if (num[0] == '0')
      num = num.substr(1);
    cout << "Case #" << tt << ": " << num << '\n';
  }

  return 0;
}
