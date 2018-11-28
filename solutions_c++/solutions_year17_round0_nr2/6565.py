#include <bits/stdc++.h>

using namespace std;

string solve(){
   string s;
   cin >> s;
   string res = "";
   res += s[s.size() - 1];
   s.erase(--s.end());
   int borrow = 0;
   while(s.size() > 0){
      if(s[s.size() - 1] > res[0]){
         int idx = -1;
         if(s[s.size() - 1] == '0'){
            for(int k = s.size() - 1; k >= 0; --k){
               if(s[k] != '0'){
                  idx = k;
                  break;
               }
            }
         }
         else{
            idx = s.size() - 1;
         }
         assert(idx >= 0);
         assert(s[idx] > '0');
         s[idx] = s[idx] - 1;
         for(int j = 0; j < res.size(); ++j) res[j] = '9';
      }
      res = s[s.size() - 1] + res;
      s.erase(--s.end());
   }
   while(res.size() > 0){
      if(res[0] == '0') res.erase(res.begin());
      else break;
   }
   return res;
}

int _main(int argc, char *argv[]) {
   int t;
   cin >> t;
   for(int test = 1; test <= t; ++test){
      string res = solve();
      cout << "Case #"<< test << ": " << res << endl;
      cerr << "Case #"<< test << ": " << res << endl;
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