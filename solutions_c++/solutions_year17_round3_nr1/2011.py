
#include <iostream>
#include <string>
#include <vector>
#include <limits>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>

#define rep(i, a, b) for(int (i) = (a); (i) < (b); ++(i))

using namespace std;

const long double PI = 3.141592653589793238L;

struct Pancake{
    uint64_t r;
    uint64_t h;
    bool operator<(Pancake const &rhs) const {
        //if(h == rhs.h) return r > rhs.r;
        return r*h > rhs.r*rhs.h;
    }
};

void solve(){
    int n, k;
    cin >> n >> k;
    vector<Pancake> pancakes;
    rep(i, 0, n){
        pancakes.push_back({});
        cin >> pancakes.back().r >> pancakes.back().h;
    }
    sort(pancakes.begin(), pancakes.end());
    uint64_t ans = 0;
    for(auto biggest = pancakes.begin(); biggest != pancakes.end(); ++biggest) {
        vector<Pancake> used_pancakes;
        //cout << "Biggest " << biggest->r << " " << biggest->h << endl;
        used_pancakes.push_back(*biggest);
        auto it = pancakes.begin();
        rep(i, 0, k-1){
            while(it->r > biggest->r || it == biggest){
                ++it;
                if(it == pancakes.end()) break;
            }
            if(it == pancakes.end()) break;
            used_pancakes.push_back(*it);
            ++it;
            //cout << "Using " << used_pancakes.back().r << " " << used_pancakes.back().h << endl;
        }
        if(used_pancakes.size() != k) continue;
        uint64_t area = (biggest->r * biggest->r);
        for (auto const &p : used_pancakes) {
            //cout << "Using " << p.r << " " << p.h << endl;
            area += p.r * 2 * p.h;
        }
        //cout << area << endl;
        if(area > ans) ans = area;
    }

    cout << std::setprecision(std::numeric_limits<long double>::digits10 + 1) << ans * PI << endl;
}

int main(){
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i){
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
