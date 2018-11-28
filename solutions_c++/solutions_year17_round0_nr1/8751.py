#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <queue>
using namespace std;

int T, K;
string target;
unordered_map <string, int> mapa;

void busca( string& cad ){
	int lim = cad.size() - K + 1;
	string tmp;
	queue < string > q;
	q.push(cad);
	mapa[cad] = 0;

	while( !q.empty() ){
		string u = q.front(); q.pop();
		if( u == target ) break;

		for( int i = 0; i < lim; i++ ){
			tmp = u;
			for( int j = 0; j < K; j++ ){
				if( tmp[j+i] == '+' ) tmp[j+i] = '-';
				else tmp[j+i] = '+';
			}
			if( mapa.count( tmp ) == 0 || mapa[u]+1 < mapa[tmp]  ){
				mapa[tmp] = mapa[u]+1;
				q.push(tmp);
			}
		}
	}
}

int main(){
	string cad;
	cin >> T;
	for( int casos = 1; casos <= T; casos++ ){
		mapa.clear();
		cin >> cad >> K;

		target = "";
		for( int i = 0; i < cad.size(); i++ )
			target += '+';
		busca( cad );
		
		cout << "Case #" << casos << ": ";
		if( mapa.count( target ) )
			cout << mapa[target] << '\n';
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}