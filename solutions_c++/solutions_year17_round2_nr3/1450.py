#include<bits/stdc++.h>
/*
*/

using namespace std;

typedef pair<long double, pair<long long int, pair< pair < long long int, long long int >, vector<bool>>> >pqtype;

int main() {
	long long int casenum;
	cin >> casenum;
	for( size_t index = 0; index < casenum; index++ ) {
		long long int N, T;
		cin >> N >> T;
		vector<pair<long long int, long long int>>uma( N );
		for( size_t i = 0; i < N; i++ ) {
			cin >> uma[i].first >> uma[i].second;
		}
		vector < vector<pair<long long int, long long int> >>len( N );
		for( size_t i = 0; i < N; i++ ) {
			for( size_t j = 0; j < N; j++ ) {
				long double lennum;
				cin >> lennum;
				if( lennum != -1 ) {
					len[i].push_back( make_pair( j, lennum ) );
				}
			}
		}
		vector<long double>ans;
		for( size_t i = 0; i < T; i++ ) {
			long long int S, G;
			cin >> S >> G;
			S--; G--;
			priority_queue<pqtype, vector<pqtype>, greater<pqtype>>que;
			vector<bool>init( 0 );
			//init[S] = true;
			que.push( make_pair( 0, make_pair( S, make_pair( make_pair( 0, 0 ), init ) ) ) );
			while( que.size() ) {
				auto now = que.top(); que.pop();
				//cout << now.second.first <<" "<<now.first<< endl;
				if( now.second.first == G ) {
					ans.push_back( now.first );
					break;
				}

				for( auto x : len[now.second.first] ) {
					//if( !now.second.second.second[x.first] ) {
						auto next = now;
						//next.second.second.second[x.first] = true;
						next.second.first = x.first;
						if( x.second <= next.second.second.first.first ) {
							next.second.second.first.first -= x.second;
							next.first += x.second*1.L / next.second.second.first.second;
							//cout<<x.second<<" "<< next.second.second.first.second<<" !!"<<endl;
							que.push( next );
						}
						next = now;
					//	next.second.second.second[x.first] = true;
						next.second.first = x.first;
						if( x.second <= uma[now.second.first].first ) {
							next.second.second.first = uma[now.second.first];
							next.second.second.first.first -= x.second;
							next.first += x.second*1.L / next.second.second.first.second;
							//cout << x.second << " " << next.second.second.first.second << " !!" << endl;
							que.push( next );
						//}
					}
				}
			}

		}
		cout << "Case #" << index + 1 << ": ";
		for( size_t i = 0; i < ans.size(); i++ ) {
			cout << fixed << setprecision( 20 ) << ans[i];
			if( i != ans.size() - 1 ) {
				cout << " ";
			} else {
				cout << endl;
			}
		}
	}
}
