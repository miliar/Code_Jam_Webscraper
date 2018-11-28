#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
	int T;
	cin >> T;
	int cnt = 0;
	while(T--){
		++cnt;
		ll dest_pos;
		ll n;
		ll init_pos;
		ll max_speed;
		double max_time = DBL_MIN;

		cin >> dest_pos >> n;
		for(int i = 0; i < n; ++i){
			cin >> init_pos >> max_speed;
			int dist_rem = dest_pos - init_pos;
			double time_req = 1.0 * dist_rem / max_speed;
			max_time = max(max_time, time_req);
		}
		printf("Case #%d: %.6f\n", cnt, dest_pos / max_time);
	}
	return 0;
}