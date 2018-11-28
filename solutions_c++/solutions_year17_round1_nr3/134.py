#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <map>
using namespace std ;
const int MAXN = 100 ;
int Hd, Ad, Hk, Ak, B, D, iHd ;
vector<int> s ;
typedef vector<int> state ;
map<state, int> dist ;
vector<state> q ;
int res ;
int gd ;
void pack() {
  s[0] = Hd ;
  s[1] = Ad ;
  s[2] = Hk ;
  s[3] = Ak ;
}
void newstate(int Hd, int Ad, int Hk, int Ak) {
  Hd -= Ak ;
  if (Hd <= 0 && Hk > 0)
    return ;
  if (Hd < 0)
    Hd = 0 ;
  if (Hk < 0)
    Hk = 0 ;
  if (Ak < 0)
    Ak = 0 ;
  s[0] = Hd ;
  s[1] = Ad ;
  s[2] = Hk ;
  s[3] = Ak ;
  if (dist.find(s) == dist.end()) {
    //    cout << "New state " << Hd << " " << Ad << " " << Hk << " " << Ak << " at " << gd << endl ;
    dist[s] = gd + 1 ;
    q.push_back(s) ;
  }
}
void unpack() {
  Hd = s[0] ;
  Ad = s[1] ;
  Hk = s[2] ;
  Ak = s[3] ;
}
int allmoves() {
  if (Hk == 0) {
    res = gd - 1 ;
    return 1 ;
  }
  if (Ad > Hk) {
    res = gd ;
    return 1 ;
  }
  newstate(Hd, Ad, Hk-Ad, Ak) ;
  newstate(Hd, Ad+B, Hk, Ak) ;
  newstate(iHd, Ad, Hk, Ak) ;
  newstate(Hd, Ad, Hk, Ak-D) ;
  return 0 ;
}
int main() {
   int T ;
   cin >> T ;
   for (int kase=1; kase<=T; kase++) {
      s = vector<int>(4) ;
      cin >> Hd >> Ad >> Hk >> Ak >> B >> D ;
      iHd = Hd ;
      pack() ;
      q.clear() ;
      dist.clear() ;
      q.push_back(s) ;
      dist[s] = 1 ;
      int qg = 0 ;
      int r ;
      res = -1 ;
      while (qg < q.size()) {
	s = q[qg++] ;
	gd = dist[s] ;
	unpack() ;
	int t = allmoves() ;
	if (t)
	  break ;
      }
      if (res < 0)
	cout << "Case #" << kase << ": IMPOSSIBLE" << endl ;
      else
	cout << "Case #" << kase << ": " << res << endl ;
      //      cout << "Queue size is " << q.size() << endl ;
   }
}
