#include <bits/stdc++.h>

using namespace std;

bool check(string s){
   for(int i = 0; i < s.size(); ++i){
      if(s[i] == '-') return false;
   }
   return true;
}

void solve(){
   string s;
   cin >> s;
   int k, n;
   n = s.size();
   cin >> k;
   int res = 0;
   for(int i = 0; i < n; ++i){
      if(s[i] == '-'){
         if(i + k - 1 >= n) break;
         for(int j = i; j < i + k; ++j){
            s[j] = (s[j] == '+' ? '-' : '+');
         }
         ++res;
      }
   }
   if(check(s)) cout << res << endl;
   else cout << "IMPOSSIBLE" << endl;
}

int _main(int argc, char *argv[]) {
   int t;
   cin >> t;
   for(int test = 1; test <= t; ++test){
      cout << "Case #" << test << ": ";
      solve();
      cerr << test << endl;
   }
   return 0;
}

//{
int correct(int argc, char *argv[]) {
   return 0;
}
int tests(int argc, char *argv[]) {
   return 0;
}
int main(int argc, char *argv[]) {
   if(argc >= 2 && argv[1][0] == '1') {
      correct(argc, argv);
   } else if(argc >= 2 && argv[1][0] == '2') {
      tests(argc, argv);
   } else {
      _main(argc, argv);
   }
   return 0;
}//}