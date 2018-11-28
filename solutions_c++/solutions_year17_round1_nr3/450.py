#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <list>
using namespace std;

template<class P0, class P1> ostream &operator<<(ostream &os, const pair<P0, P1> &p) { return os << "(" << p.first << "," << p.second << ")"; }
template<class T> void _dump(const T &t) { cerr << "["; for (auto it = t.begin(); it != t.end(); ++it) cerr << " " << *it; cerr << " ]" << "\n"; } 

#define dump(x) { cerr << #x << ": "; _dump(x); }
#define trace(x) { cerr << #x << ": " << x << "\n"; }

#if 0
#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;
#define Integer cpp_int
#endif

int ceilFrac(int p, int q) {
  return (p+q-1)/q;
}

int dHealth0, dAttack0, kHealth0, kAttack0, buff, debuff;

int main(void) {
  int T; cin >> T;

  for (int iCase = 1; iCase <= T; ++iCase) {
    cout << "Case #" << iCase << ":";

    cin >> dHealth0 >> dAttack0 >> kHealth0 >> kAttack0 >> buff >> debuff;
    
    //===== SMALL
    int i, j, k, fastest = -1;
    for (int nBuffs = 0; nBuffs < 100; ++nBuffs) {
      for (int nDebuffs = 0; nDebuffs < 100; ++nDebuffs) {
	int moves = 0;
	int dH = dHealth0, dA = dAttack0, kH = kHealth0, kA = kAttack0;

	// Debuff (nDebuff) times
	for (i = 0; i < nDebuffs; ++i) {
	  int kANew = kA - debuff; if (kANew < 0) kANew = 0;
	  if (dH <= kANew) { ++moves; dH = dHealth0 - kA; }
	  if (dH <= 0) break;
	  ++moves; kA = kANew; dH -= kA;
	  if (dH <= 0) break;
	}
	if (dH <= 0) continue;

	// Buff (nBuffs) times
	for (i = 0; i < nBuffs; ++i) {
	  if (dH <= kA) { ++moves; dH = dHealth0 - kA; }
	  if (dH <= 0) break;
	  ++moves; dA += buff; dH -= kA;
	  if (dH <= 0) break;
	  
	}
	if (dH <= 0) continue;
	
	// Attack until knight is dead
	while (kH > 0) {
	  if (kH <= dA) { ++moves; kH -= dA; break; }
	  if (dH <= kA) { ++moves; dH = dHealth0 - kA; }
	  ++moves; kH -= dA; dH -= kA;
	  if (dH <= 0) break;
	}
	
	if (dH > 0)
	  if (fastest==-1 || moves < fastest) fastest = moves;
      }
    }
  

    if (fastest==-1)
      cout << " IMPOSSIBLE";
    else
      cout << " " << fastest;

    cout << "\n";
  }

  return 0;
}
