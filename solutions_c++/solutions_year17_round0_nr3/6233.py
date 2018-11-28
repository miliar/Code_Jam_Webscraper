#include <bits/stdc++.h>

using namespace std;

struct node{
   int size, l ,r;
   node(){}
   node(int a ,int b, int c ){
      size = a;
      l = b;
      r = c;
   }
   node(int a , int b ){
      l = a;
      r = b;
      size = (r-l+1);
   }
   bool operator <(const node& rhs) const{
      if(size > rhs.size){
         return true;
      }
      else if(size  == rhs.size)
         return l < rhs.l;
      return false;
  }
  bool operator ==(const node& rhs) const{
      if(size == rhs.size && l == rhs.l && r == rhs.r)
      return true;
      return false; 
  }
};



void solve() {
   int n,k;
   cin >> n >> k;
   vector<int> v(n+3,0);
   v[0] = v[n+1] = 1;
   set<node> s;
   s.insert(node(n,1,n));
   int pos;
   for(int i = 1; i <= k; i++){
      struct node cur = *s.begin();
      s.erase(s.begin());
       pos = (cur.l + cur.r)/2;
      if(cur.r != cur.l){
         if(cur.r != cur.l + 1)
            s.insert(node(cur.l,pos-1));
         s.insert(node(pos+1,cur.r));
      }
      v[pos] = 1;
   }
   /*for(int i = 0; i <= n + 1; i++){
      cout << v[i] << " ";
   }
   cout << endl;*/
   int prev = 0;
   vector<pair<int,int> > vals(n+3);
   for(int i = 1; i <= n+1; i++){
      vals[i].first = (i-prev-1);
      if(v[i] == 1)
         prev = i;
   }
   prev = n + 1;
   for(int i = n; i >= 0; i--){
      vals[i].second = (prev-i-1);
      if(v[i] == 1)
         prev = i;
   }
   cout << max(vals[pos].first,vals[pos].second) << " " << min(vals[pos].first,vals[pos].second) << endl;
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

