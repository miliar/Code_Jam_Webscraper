#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<vector<bool> > VVB;

bool findMatch(int i, const VVB &w, VI &mr, VI &mc, VI &seen) {
    for (int j = 0; j < w[i].size(); j++) {
		if (w[i][j] && !seen[j]) {
			seen[j] = true;
			if (mc[j] < 0 || findMatch(mc[j], w, mr, mc, seen)) {
				mr[i] = j, mc[j] = i;
				return true;
			}
		}
	}
	return false;
}

void maxBipartiteMatching(const VVB &w, VI& mr, VI& mc ) {
	mr.assign(w.size(),-1);
	mc.assign(w[0].size(), -1);
	for (int i = 0; i < int(w.size()); i++) {
		VI seen(w[0].size());
		findMatch(i, w, mr, mc, seen);
	}
}

string chars = "0+xo";
#define PLUS 		1
#define CROSS		2

bool isValid ( const VVI& M ) {
	const int n = M.size();
	VI cntRow(n,0), cntCol(n,0), cntDiag1(2*n,0), cntDiag2(2*n,0);
	for ( int i = 0; i < M.size(); ++i )
		for ( int j = 0; j < M.size(); ++j ) {
			if ( M[i][j]&1 )
				cntDiag1[i+j]++, cntDiag2[i+n-j]++;
			if ( M[i][j]&2 )
				cntRow[i]++, cntCol[j]++;
		}
	bool ok = *max_element(cntRow.begin(), cntRow.end()) <= 1;
	ok &= *max_element(cntCol.begin(), cntCol.end()) <= 1;
	ok &= *max_element(cntDiag1.begin(), cntDiag1.end()) <= 1;
	ok &= *max_element(cntDiag2.begin(), cntDiag2.end()) <= 1;
	if ( !ok ) {
		cout << "Illegal matrix:\n";
		for ( VI row : M ) {
			for ( int x : row ) cout << chars[x];
			cout << "\n";
		}
	}
	return ok;
}

void solve ( int test ) {
	int n, placed;
	cin >> n >> placed;
	
	VVI M ( n, VI ( n, 0 ) );
	VVB Bcross ( n, vector<bool> ( n, 0 ) );
	VVB Bplus ( 2*n, vector<bool> ( 2*n, 0 ) );
	vector<bool> usedRow(n, false), usedCol(n, false);
	vector<bool> usedDiag1(2*n, false), usedDiag2(2*n, false);
	
	//cout << "n = " << n << ", placed = " << placed << endl;
	
	while ( placed-- ) {
		char c;
		int i, j;
		cin >> c >> i >> j;
		M[--i][--j] = chars.find(c);
		if ( M[i][j]&1 ) usedDiag1[i+j] = usedDiag2[n+i-j] = true;
		if ( M[i][j]&2 ) usedRow[i] = usedCol[j] = true;
	}

	for ( int i = 0; i < n; ++i )
		for ( int j = 0; j < n; ++j ) {
			if ( !usedDiag1[i+j] && !usedDiag2[n+i-j] )
				Bplus[i+j][n+i-j] = 1;
			if ( !usedRow[i] && !usedCol[j] )
				Bcross[i][j] = 1;
		}
	
	int stylePoints = 0;
	VVI Mf = M;
	vector<int> mr, mc;
	maxBipartiteMatching(Bplus, mr, mc);
	for ( int d1 = 0; d1 < mr.size(); ++d1 ) {
		if ( mr[d1] != -1 ) {
			const int d2 = mr[d1];
			const int i = (d1+d2-n)/2;
			const int j = d1 - i;
			//cout << "add + " << i << " " << mr[i] << " to ans" << endl;
			Mf[i][j] |= 1;
		}
	}

	maxBipartiteMatching(Bcross, mr, mc);
	for ( int i = 0; i < mr.size(); ++i )
		if ( mr[i] != -1 ) {
			//cout << "add * " << i << " " << mr[i] << " to ans" << endl;
			Mf[i][mr[i]] |= 2;
		}
	
	vector<int> ans;
	for ( int i = 0; i < n; ++i )
		for ( int j = 0; j < n; ++j ) {
			if ( Mf[i][j] != M[i][j] ) {
				ans.push_back(i);
				ans.push_back(j);
			}
			stylePoints += __builtin_popcount(Mf[i][j]);
		}
	cout << "Case #" << test << ": " << stylePoints << " " << ans.size()/2 << endl;
	
	for ( int i = 0; i < ans.size(); i += 2 )
		cout << chars[Mf[ans[i]][ans[i+1]]] << " " << ans[i]+1 << " " << ans[i+1]+1 << endl;

	assert ( isValid(M) );
}

int main ( )
{
	freopen ( "D-large.in", "r", stdin );
	freopen ( "D.out", "w", stdout );
	int ntc;
	cin >> ntc;
	for ( int test = 1; test <= ntc; ++test )
		solve(test);
	return 0;
}
