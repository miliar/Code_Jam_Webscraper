#include <bits/stdc++.h>

using namespace std;

int pos(string &s,int k){
   int ans = 0;
    for(int i = 0; i <= s.length() - k; i++){
       if(s[i] == '-'){
         ans ++;
         for(int j =i; j < i  + k; j++){
            s[j] = (s[j] == '-' ? '+' : '-');
         }
       }
    }
   for(int i = 0;i < s.length(); i++){
      if(s[i] == '-')
         return -1;
   }
   return ans;
}

void solve() {
   string s;
   cin >> s;
   int k;cin >> k;
   string t = s;
   reverse(t.begin(), t.end());
   //cout << s << " ";
   int ans = pos(s,k);
   //cout << s << " " ;
   //cout << t << " " ;   
   int x = pos(t,k);
   //cout << t << "\n " ;

   if(ans == -1 && x == -1){
      cout << "IMPOSSIBLE\n";
      return;
   }
   if(ans != -1 && x != -1){
      cout << min(ans,x) << endl;
      return;
   }
   if(ans != -1){
      cout << ans << endl;
   }
   else
      cout << x << endl;
}

int main() {
   assert(freopen("input.txt","r",stdin));
   assert(freopen("output.txt","w",stdout));
   int t; cin>>t;
   for(int i = 1;i <= t;i++) {
      cerr<<"Executing Case #"<<i<<endl;
      cout<<"Case #"<<i<<": ";
      solve();
   }

}
