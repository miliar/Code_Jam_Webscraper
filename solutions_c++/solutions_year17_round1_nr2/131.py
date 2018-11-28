#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std ;
typedef long long ll ;
// minimum servings if we have have, and require req per.
// must be within [0.9..1.1].   So:
//   have <= 1.1 * req * serv
//   serv >= hav / 1.1 / req
//   serv >= hav * 10 / (11 * req)
ll smallserv(ll have, ll req) {
  return (have * 10 + req * 11 - 1) / (11 * req) ;
}
// same as above, but floor this time and with 9 instead of 11.
ll largeserv(ll have, ll req) {
  return (have * 10) / (9 * req) ;
}
int main() {
   ll T, N, P ;
   cin >> T ;
   for (int kase=1; kase<=T; kase++) {
      cin >> N >> P ;
      vector<ll> R(N) ;
      for (int i=0; i<N; i++)
	cin >> R[i] ;
      vector<vector<ll> > A ;
      for (int i=0; i<N; i++) {
	vector<ll> Q(P) ;
	for (int j=0; j<P; j++)
	  cin >> Q[j] ;
	sort(Q.begin(), Q.end()) ;
	A.push_back(Q) ;
      }
      int r = 0 ;
      vector<int> at(N) ;
      bool done = false ;
      while (!done) {
	// what's the smallest serv we can make with where we are at?
	for (int i=0; i<N; i++)
	  if (at[i] >= P)
	    done = true ;
	if (done)
	  break ;
	ll loserv = INT_MAX ;
	for (int i=0; i<N; i++)
	  loserv = min(loserv, smallserv(A[i][at[i]], R[i])) ;
	// can we make a serving at this point using the ingredients
	// we have at the locations we are at?
	ll hiserv = 2 * loserv ;
	for (int i=0; i<N; i++) {
	   ll ss = smallserv(A[i][at[i]], R[i]) ;
	   ll bs = largeserv(A[i][at[i]], R[i]) ;
	   loserv = max(loserv, ss) ;
	   hiserv = min(hiserv, bs) ;
	}
	if (hiserv >= loserv) {// still good!
	  r++ ;
	  for (int i=0; i<N; i++)
	    at[i]++ ;
	} else {
	  ll lo = INT_MAX ;
	  int loi = 0 ;
	  for (int i=0; i<N; i++) {
	    ll ss = smallserv(A[i][at[i]], R[i]) ;
	    ll bs = largeserv(A[i][at[i]], R[i]) ;
	    if (ss + bs < lo) {
	      lo = ss + bs ;
	      loi = i ;
	    }
	  }
	  at[loi]++ ;
	}
      }
      cout << "Case #" << kase << ": " << r << endl ;
   }
}
