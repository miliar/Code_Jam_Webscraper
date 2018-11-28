#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

void transf(int s[50], string ss){
   int l = ss.length();
   for (int i = 0; i < l; i++)
      s[i] = ss[i] - '0';
}

void answer(string ss){
   int s[50];
   int l = ss.length();
   transf(s, ss);
   for (int i = l-1; i > 0; i--){
      if (s[i] < s[i-1]){
         s[i-1] = s[i-1]-1;
         for (int j = i; j < l; j++)
            s[j] = 9;
      }
   }
   int j = 0;
   for (j; j < l && s[j] == 0; j++);
   for (j; j < l; j++)
      cout << s[j];
}

int main()
{
   freopen("data.in", "r", stdin);
   freopen("data.out", "w", stdout);
   int T, n;
   string s;
   cin >> T;
   for (int i = 1; i <= T; ++i){
      cin >> s;
      cout << "Case #" << i << ": ";
      answer(s);
      cout << "\n";
   }

   return 0;
}
