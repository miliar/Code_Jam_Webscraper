#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

int n;

char r(char x){
   if (x == '-')
      return '+';
   return '-';
}

void rev(string &s, int i, int k){
   for (int j = i; j > i-k; j--)
      s[j] = r(s[j]);
}

int answer(string s, int k){
   int l = s.length();
   int tor = 0;
   for (int i = l-1; i >= k-1; i--)
      if (s[i] == '-'){
         rev(s, i, k);
         tor++;
      }
   for (int i = 0; i < l; i++)
      if (s[i] == '-')
         return -1;
   return tor;
}

int main()
{
   freopen("data.in", "r", stdin);
   freopen("data.out", "w", stdout);
   int T, ans, k;
   string s;
   cin >> T;
   for (int i = 1; i <= T; i++){
      cin >> s >> k;
      cout << "Case #" << i << ": ";
      ans = answer(s, k);
      if (ans == -1)
         cout << "IMPOSSIBLE";
      else
         cout << ans;
      cout << "\n";
   }


   return 0;
}
