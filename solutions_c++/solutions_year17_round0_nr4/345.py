#include <bits/stdc++.h>

using namespace std;
using positions = set<pair<int,int>>;
using VI = vector<int>;
using VVI = vector<VI>;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
  for (int j = 0; j < w[i].size(); j++) {
    if (w[i][j] && !seen[j]) {
      seen[j] = true;
      if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);
  
  int ct = 0;
  for (int i = 0; i < w.size(); i++) {
    VI seen(w[0].size());
    if (FindMatch(i, w, mr, mc, seen)) ct++;
  }
  return ct;
}

positions mult_f(positions old_mult, int n) {
   VVI mat(n, VI (n,1));
   VI mr;
   VI mc;
   for(pair<int,int> p : old_mult) {
      for(int i = 0; i < n; ++i) {
         mat[p.first][i] = 0;
         mat[i][p.second] = 0;
      }
   }
   BipartiteMatching(mat,mr,mc);
   positions ans;
   for(int i = 0; i < n; ++i)
      if(mr[i] != -1) ans.insert({i,mr[i]});
   return ans;
}

// i+j in (0,2n-2)
// i-j in (-(n-1),n-1)
// n-1+i-j in (0,2n-2)
// a=i+j
// b=n-1+i-j
// i=(a+b-n+1)/2
// j=(a-b-1+n)/2
positions plus_f(positions old_plus, int n) {
   VVI mat((2*n) - 1, VI ((2*n) - 1,0));
   VI mr;
   VI mc;
   for(int i = 0; i < n; ++i) {
   for(int j = 0; j < n; ++j)
      mat[i+j][n-1+i-j] = 1;
   }
   for(pair<int,int> p : old_plus) {
      int i = p.first;
      int j = p.second;
      int a = i+j;
      int b = n-1+i-j;
      for(int c = 0; c < (2*n) - 1; ++c) {
         mat[a][c] = 0;
         mat[c][b] = 0;
      }
   }
   BipartiteMatching(mat,mr,mc);
   positions ans;
   for(int a = 0; a < (2*n) - 1; ++a) {
      int b = mr[a];
      if(b != -1) ans.insert({(a+b-n+1)/2,(a-b-1+n)/2});
   }
   return ans;
}

int main() {
   int t;
   cin >> t;
   for(int i = 1; i <= t; ++i) {
      cout << "Case #" << i << ": ";
      int n, m, cnt = 0;
      string s;
      positions old_mult, old_plus;
      cin >> n >> m;
      for(int j = 0; j < m; ++j) {
         int a, b;
         cin >> s >> a >> b;
         if(s != "+") {
            old_mult.insert({a-1,b-1});
            cnt++;
         }
         if(s != "x") {
            old_plus.insert({a-1,b-1});
            cnt++;
         }
      }
      positions new_plus = plus_f(old_plus,n);
      positions new_mult = mult_f(old_mult,n);
      set<pair<char,pair<int,int>>> order;
      for(pair<int,int> pos : new_plus) {
         if(new_mult.find(pos) == new_mult.end()
         && old_mult.find(pos) == old_mult.end())
            order.insert({'+',pos});
         else order.insert({'o',pos});
      }
      for(pair<int,int> pos : new_mult) {
         if(new_plus.find(pos) != new_plus.end()) continue;
         if(old_plus.find(pos) != old_plus.end())
            order.insert({'o',pos});
         else order.insert({'x',pos});
      }
      cout << cnt + new_plus.size() + new_mult.size() << " "
           << order.size() << endl;
      for(pair<char,pair<int,int>> ord : order)
         cout << ord.first << " " << ord.second.first+1 << " "
              << ord.second.second+1 << endl;
   }
}
