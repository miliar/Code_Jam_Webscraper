#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

# define M_PI           3.14159265358979323846  /* pi */

template <class T>
void print_out(int l, T ret) {
  cout.precision(20);
  cout << "Case #" << l << ": " << ret << endl;
}

struct greaterx
{
    template<class T>
    bool operator()(T const &a, T const &b) const { return a > b; }
};

void solve(double& ret, int K, vector< pair<long long,long long> > p, double act_ret) {
  if(K == 0 && act_ret > ret) {
    ret = act_ret;
    return;
  }

  
  vector< pair<long long,long long> > tmp;
  for (unsigned int x = 0; x < p.size(); ++x) {
      tmp = p;
      long long R = tmp[x].first;
      long long H = tmp[x].second;
      tmp.erase(tmp.begin()+x);
      solve( ret, (K-1), tmp, (act_ret+(M_PI*(2*R*H))) );
  }
}

int main(void) {
  int T; cin >> T; cin.ignore();
  for (int l = 1; l <= T; ++l) {
    /* DO PROBLEM STUFF HERE --> */
    int N, K; cin >> N >> K; cin.ignore();
    
    // PI *(R*R + 2*R*H)
    
    vector< pair<long long,long long> > p;
    multimap<long long,int> areas;
    multimap<long long,int> sides;
    for (int i = 0; i < N; ++i) {
        long long R,H; cin >> R >> H; cin.ignore();
        p.push_back(make_pair(R,H));
        areas.insert(make_pair(R*R+2*R*H, i));
        sides.insert(make_pair(2*R*H, i));
    }
    
    double ret = 0;
    double act_ret = 0;
    
    sort(p.begin(), p.end(), greaterx());
    
    vector< pair<long long,long long> > tmp;
    for (unsigned int x = 0; x < p.size(); ++x) {
      tmp = p;
      long long R = tmp[x].first;
      long long H = tmp[x].second;
      tmp.erase(tmp.begin()+x);
      solve( ret, (K-1), tmp, (act_ret+(M_PI*(R*R+2*R*H))) );
    }
    
    
    /*
    double ret = (areas.rbegin()->first)*M_PI;
    p[(areas.rbegin()->second)] = make_pair(0,0);
    int used = (areas.rbegin()->second);
    
    cerr<<endl;
    for (auto y = p.begin(); y != p.end() ; ++y) {
      cerr<<y->first<<","<<y->second<<";";
    }
    cerr<<endl;
    
    --K;
    
    cerr<<"biggest: "<<ret<<endl;
    
    for (int i = 0; i < K;++i) {
        cerr<<p[(sides.rbegin()->second)].first<<" "<<p[(sides.rbegin()->second)].second<<endl;
        
        if ((sides.rbegin()->second) != used) {
          ret += (sides.rbegin()->first)*M_PI;
          // ++i;
          cerr<<"---"<<endl;
        }
        else {
          --i;
        }
        sides.erase(prev(sides.end()));
    }
    
    cerr<<"ret: "<<ret<<endl;*/

    print_out(l, ret);
    
    /* <-- DO PROBLEM STUFF HERE */
  }
  return 0;
}



