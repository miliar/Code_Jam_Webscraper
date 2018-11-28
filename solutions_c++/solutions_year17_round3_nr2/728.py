#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct interval {
  int i, f;
  bool t;
  interval(int i, int f, bool t) : i(i), f(f), t(t) {}
  interval() {}
};
bool compare(interval& x, interval& y){
  return x.i < y.i;
}
int prev(int i, int n) {
  if(i>0) return i-1;
  else return n-1;
}
int dist(int b, int a){
  if(b%1440>=a%1440) return b%1440-a%1440;
  else return 1440 + b%1440-a%1440;
}
int main(){
  ios_base::sync_with_stdio(false);
  int T;
  int n;
  int ac, aj, I, F;  
  cin >> T;
  for(int ind=0; ind<T; ind++){
    cin >> ac >> aj;
    vector<interval>is(ac+aj);
    vector<int>acc_c;
    vector<int>acc_j;
    for(int i=0; i<ac; i++) {
      cin >> I >> F;
      is[i] = interval(I, F, true);
    }
    for(int i=ac; i<(ac+aj); i++) {
      cin >> I >> F;
      is[i] = interval(I, F, false);
    }    
    sort(is.begin(), is.end(), compare);
    n = ac+aj;
    int t_c=0;
    int t_j=0;
    int n_changes = 0;
    for(int i=0; i<n; i++) {
      if(is[i].t) {
        t_c+=dist(is[i].f, is[i].i);
        if(is[prev(i, n)].t) {
          t_c += dist(is[i].i, is[prev(i, n)].f);
          acc_c.push_back(dist(is[i].i, is[prev(i, n)].f));
        }
        else
          n_changes +=1;
      } else {
        t_j+=dist(is[i].f, is[i].i);
        if(is[prev(i, n)].t)
          n_changes+=1;
        else {
          t_j +=dist(is[i].i, is[prev(i, n)].f);
          acc_j.push_back(dist(is[i].i, is[prev(i, n)].f));          
        }
      }
    }    
    cout << "Case #" << (ind+1) << ": ";
    if(t_c<=720 && t_j<=720) cout << n_changes << endl;
    else {
      if (t_c > 720 && t_j > 720 ) cout << "WEIRD" << endl;
      if (t_c > 720) {
        sort(acc_c.begin(), acc_c.end());
        int ne = acc_c.size();
        for(int i=ne-1; i>=0 && t_c > 720; i--) {
          t_c-=acc_c[i];
          n_changes+=2;          
        }
        if(t_c>720) cout << "WEIRD" << endl;        
      }
      if (t_j > 720) {
        sort(acc_j.begin(), acc_j.end());
        int ne = acc_j.size();
        for(int i=ne-1; i>=0 && t_j > 720; i--) {
          t_j-=acc_j[i];
          n_changes+=2;          
        }
        if(t_j>720) cout << "WEIRD" << endl;                
      }
      cout << n_changes << endl;
    }
  }
  return 0;
}