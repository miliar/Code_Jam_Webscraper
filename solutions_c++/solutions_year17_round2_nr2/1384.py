#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

/*
bool dp[1001][10][10][10];
int n;

bool solve(int at, int cor_ant, int cor_at int cor_p){
	if( at == n-1 ) return pode(cor_p, cor_at);

	bool &ans = dp[at][cor_ant][cor_at][cor_p];
	int &us = used[at][cor_ant][cor_at][cor_p];

	if( us == vis ) return ans;
	us = vis;
	ans = false;

	for(int i = 0; i < 7; i++){

	}
}*/

int main(){
	ios::sync_with_stdio(false);
	int t, n;
	
	cin >> t;

	for(int w = 1; w <= t; w++){
		cin >> n;
		int cor[] = {0, 0, 0, 0, 0, 0};
		for(int i = 0; i < 6; i++) cin >> cor[i];
		vector < pair < int, int > > qt;
		char id[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
		for(int i = 0; i <= 4; i += 2){
			qt.push_back(make_pair(-cor[i], i));
		}

		sort(qt.begin(), qt.end());
		string ans = "";
		for(int i = 0; i < -qt[0].first; i++) ans += id[qt[0].second];
		for(int i = 0, k = 1; i < -qt[1].first; i++, k+= 2) ans.insert(ans.begin()+k, id[qt[1].second]);
		reverse(ans.begin(), ans.end());
		for(int i = 0, k = 0; i < -qt[2].first; i++, k+= 2) ans.insert(ans.begin()+k, id[qt[2].second]);

		bool ok = ans.size() == n;
		for(int i = 0; i < n; i++){
			if( ans[i] == ans[(i+1)%n] ){
				ok = false;
				break;
			}
		}
		cout << "Case #" << w << ": ";
		if( ok == false ){
			cout << "IMPOSSIBLE\n";
		}
		else cout << ans << '\n';
		
	}

	return 0;
}