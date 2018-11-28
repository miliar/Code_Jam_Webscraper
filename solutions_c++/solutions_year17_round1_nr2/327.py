#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> Seg;

ostream& operator << ( ostream& out, Seg s ) { return out << "(" << s.first << "," << s.second << ")"; }

Seg intersection ( Seg a, Seg b ) {
	return Seg( max(a.first,b.first), min(a.second,b.second) );
}

inline ll ceilDiv( ll num, ll den ) { return (num+den-ll(1))/den; }

Seg getSegment ( ll amt, ll needed ) {
	// 9/10*x*needed <= amt
	// x <= amt*10/(needed*9)

	// 11/10*x*needed >= amt
	// x >= amt*10/(needed*11)

	amt *= ll(10);
	Seg ans = Seg( ceilDiv(amt,needed*ll(11)), amt/(needed*ll(9)) );
	Seg ans2 ( ans.first-1, ans.second+1 );
	
	if ( !( ll(9)*ans.second*needed <= amt
			&& ll(9)*ans2.second*needed > amt
			&& ll(11)*ans.first*needed >= amt
			&& ll(11)*ans2.first*needed < amt ) ) {
		cout << "Fail for amt=" << amt << ", needed=" << needed << ", returned " << ans << endl;
	}
	
	return ans;
}

bool cmp ( const Seg& a, const Seg& b ) {
	if ( a.first != b.first ) return a.first < b.first;
	return a.second < b.second;
}

int solve() {
	int nIngredients, nPackages;
	cin >> nIngredients >> nPackages;
	
	vector<ll> needed ( nIngredients );
	vector<deque<Seg> > amt ( nIngredients );
	
	for ( auto& x : needed ) cin >> x;
	for ( int i = 0; i < nIngredients; ++i ) {
		for ( int j = 0, x; j < nPackages; ++j ) {
			cin >> x;
			amt[i].push_back( getSegment(x, needed[i]) ); 
		}
		sort ( amt[i].begin(), amt[i].end(), cmp );
	}
	
	int ans = 0;
	
	while ( true ) {

		Seg total;
		for ( int i = 0; i < nIngredients; ++i ) {
			while ( true ) {
				if ( amt[i][0].first <= amt[i][0].second ) break;
				amt[i].pop_front();
				if ( amt[i].empty() ) return ans;
			}
			if ( i == 0 ) total = amt[i][0];
			else total = intersection(total, amt[i][0]);
		}

		if ( total.first <= total.second )
		{
			ans++;
			for ( int i = 0; i < nIngredients; ++i ) {
				amt[i].pop_front();
				if ( amt[i].empty() ) return ans;
			}
		}
		else
		{
			int remIndex = 0;
			Seg remSeg = amt[0][0];
			for ( int i = 1; i < nIngredients; ++i ) {
				if ( amt[i][0].second < remSeg.second ) {
					remIndex = i;
					remSeg = amt[i][0];
				}
			}
		
			amt[remIndex].pop_front();
			if ( amt[remIndex].empty() )
				return ans;
		}
	}
}

int main() {
	freopen ( "B-large.in", "r", stdin );
	freopen ( "B.out", "w", stdout );
	
	int ntc;
	scanf ( "%d", &ntc );
	for ( int test = 1; test <= ntc; ++test ) {
		int ans = solve();
		cout << "Case #" << test << ": " << ans << endl;
	}
	
	return 0;
}
