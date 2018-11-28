#include<iostream>
#include<string>

using namespace std;

string num;
bool found = false;
char answer[100000000001];

void gen (char root, int pos, bool used) {
  if (found) return ;

  if (pos >= num.length()) {
    found = true;
    return ;
  }

  for(char a = '9' ; a >= root ; a--) {
    if (found) break;

    if (!used && a > num[pos]) continue;
    answer[pos] = a;
    // cout << "num=" << num[pos] << ", " << a << ", pos=" << pos << endl;
    if (a < num[pos]) gen(a, pos + 1, true);
    else gen(a, pos + 1, used);
  }
  return ;
}

int main () {
  int t;

  cin >> t;
  for (int i = 0 ; i < t ; i++) {
    cin >> num;
    found = false;
    gen('0', 0, false);

    cout << "Case #" << (i+1) << ": "; 
    for (int j = 0 ; j < num.length(); j++) {
      if (j == 0 && answer[j] == '0') continue;
      cout << answer[j];
    }
    cout << endl;
  }

  return 0;
}
