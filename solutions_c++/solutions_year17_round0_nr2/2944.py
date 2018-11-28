#include <bits/stdc++.h>

using namespace std;

int T, f, cs;
string s;

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);

  cin >> T;
  while(T--){
    cin >> s;
    f = s.size();
    for(int i = s.size() - 1; i; --i){
      if(s[i] < s[i - 1]){
        f = i;
        --s[i - 1];
      }
    }
    for(int i=f; i<s.size(); i++)
      s[i] = '9';
    if(s[0] == '0')
      s.erase(s.begin());
    cout << "Case #" << ++cs << ": " << s << "\n";
  }
  return 0;
}
