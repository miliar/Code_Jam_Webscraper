#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <memory.h>
#define P pair< int, int >
using namespace std;


int dr[4][2] = { {0, -1}, {0, 1}, {1, 0}, {-1, 0} };
int A[2][4] = { {2, 3, 0, 1}, {3, 2, 1, 0} };
char b[60][60];
int R, C;

bool isin( int x, int y ){
	return x >= 0 && y >= 0 && x < R && y < C;
}

bool dfs( int x, int y, int dir, int lev, set< P >& st ){
	if( !isin( x, y ) )
		return true;
	char ch = b[x][y];
	if( ch == '#' )
		return true;
	if( ch == '.' || lev == 0 )
		st.insert( P( x, y ) );
	if( ch == '-' || ch == '|' ){
		if( lev )
			return false;
	}
	if( ch == '/' ){
		int revDir = A[0][dir];
		return dfs( x + dr[revDir][0], y + dr[revDir][1], revDir, lev + 1, st );
	}
	if( ch == '\\' ){
		int revDir = A[1][dir];
		return dfs( x + dr[revDir][0], y + dr[revDir][1], revDir, lev + 1, st );
	}
	return dfs( x + dr[dir][0], y + dr[dir][1], dir, lev + 1, st );
}

vector< P > ep;
vector< P > beams;
set< P > cover[60][60][2];
bool val[60][60][2];

void join( set< P >& s1, set< P >& s2 ){
	for( set< P >::iterator i = s2.begin(); i != s2.end(); i++ )
		s1.insert( *i );
}

void print( set< P >& st ){
	for( set< P >::iterator i = st.begin(); i != st.end(); i++ )
		cout << (*i).first << ' ' << (*i).second << endl;
}

//fill the v array
//e.g. to push (p v !q) use the following code:
//	v[VAR(p)].push_back( NOT( VAR(q) ) )
//	v[NOT( VAR(q) )].push_back( VAR(p) )
//the result will be in color array

#define VAR(X) (X << 1)
#define NOT(X) (X ^ 1)
#define CVAR(X,Y) (VAR(X) | (Y))
#define COL(X) (X & 1)
#define NVAR 3000

int n;
vector<int> v[2 * NVAR];
int color[2 * NVAR];
int bc[2 * NVAR];

bool dfs( int a, int col ) {
	color[a] = col;
	int num = CVAR( a, col );
	for( int i = 0; i < v[num].size(); i++ ) {
		int adj = v[num][i] >> 1;
		int ncol = NOT( COL( v[num][i] ) );
		if( ( color[adj] == -1 && !dfs( adj, ncol ) ) || 
			( color[adj] != -1 && color[adj] != ncol ) ) {
			color[a] = -1;
			return false;
		}
	}
	return true;
}

bool twosat() {
	memset( color, -1, sizeof color );
	for( int i = 0; i < n; i++ ){
		if( color[i] == -1 ){
			memcpy(bc, color, sizeof color);
			if( !dfs( i, 0 )){
				memcpy(color, bc, sizeof color);
				if(!dfs( i, 1 ))
					return false;
			}
		}
	}
	return true;
}

map< P , int > mp;


int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> R >> C;
		for( int i = 0; i < 2 * NVAR; i++ )
			v[i].clear();
		ep.clear();
		mp.clear();
		beams.clear();
		memset( val, false, sizeof val );
		for( int i = 0; i < R; i++ )
			for( int j = 0; j < C; j++ ){
				cin >> b[i][j];
				cover[i][j][0].clear();
				cover[i][j][1].clear();
			}
		bool imp = false;
		for( int i = 0; i < R; i++ )
			for( int j = 0; j < C; j++ ){
				char ch = b[i][j];
				if( ch == '-' || ch == '|' ){
					int sz = mp.size();
					mp[P( i, j )] = sz;
					beams.push_back( P( i, j ) );
					{
						bool d1 = dfs( i, j, 0, 0, cover[i][j][0] );
						bool d2 = dfs( i, j, 1, 0, cover[i][j][0] );
						if( d1 == false || d2 == false )
							cover[i][j][0].clear();
					}
					{
						bool d1 = dfs( i, j, 2, 0, cover[i][j][1] );
						bool d2 = dfs( i, j, 3, 0, cover[i][j][1] );
						if( d1 == false || d2 == false )
							cover[i][j][1].clear();
					}
					/*//cout << "CUr = " << i << ' ' << j << endl;
					if( cover[i][j][0].size() ){
						cout << "chp\n";
						print( cover[i][j][0] );
					}
					//cout << endl;
					if( cover[i][j][1].size() ){
						cout << "bala\n";
						print( cover[i][j][1] );
					}
					//cout << endl;
					*/
					if( cover[i][j][0].size() == 0 && cover[i][j][1].size() == 0 )
						imp = true;
				}
				if( ch == '.' )
					ep.push_back( P( i, j ) );
			}
		n = mp.size();
		for( int i = 0; i < R; i++ )
			for( int j = 0; j < C; j++ ){
				char ch = b[i][j];
				if( ch == '.' || ch == '-' || ch == '|' ){
					vector< int > vv;
					//cout << i << ' ' << j << endl;
					for( int k = 0; k < beams.size(); k++ ){
						if( cover[beams[k].first][beams[k].second][0].count( P( i, j ) ) ){
							//cout << beams[k].first << ' ' << beams[k].second << endl;
							vv.push_back( VAR(k) );
						}
						if( cover[beams[k].first][beams[k].second][1].count( P( i, j ) ) ){
							//cout << beams[k].first << ' ' << beams[k].second << endl;
							vv.push_back( NOT( VAR( k ) ) );
						}
					}
					//cout << endl;
					if( vv.size() == 0 ){
						imp = true;
						break;
					}
					if( vv.size() == 1 ){
						v[vv[0]].push_back( vv[0] );
					}
					else{
						v[vv[0]].push_back( vv[1] );
						v[vv[1]].push_back( vv[0] );
					}
				}
			}
		cout << "Case #" << T << ": ";
		bool ts = twosat();
		if( imp || ts == false )
			cout << "IMPOSSIBLE" << endl;
		else{
			cout << "POSSIBLE" << endl;
			for( int i = 0; i < beams.size(); i++ ){
				if( color[i] == 0 )
					b[beams[i].first][beams[i].second] = '|';
				else b[beams[i].first][beams[i].second] = '-';
			}
			for( int i = 0; i < R; i++ ){
				for( int j = 0; j < C; j++ )
					cout << b[i][j];
				cout << endl;
			}
		}
	}
	return 0;
}