#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int z = 1; z <= t; z++){
		int n, k;
		cin >> n >> k;
		int s[n + 2] = {0};
		s[0] = 1; s[n + 1] = 1;
		int mm = 0, mins = 0, maxs = 0, st, maxx = 0;
		for(int p = 0; p < k; p++){
			int ls, rs;
			maxs = 0;
			maxx = 0;
			mins = 0;
			mm = 0;
			if(n == k) break;
			for(int i = 1; i < n+1; i++){
				ls = -1; rs = -1;
				for(int j = i; j< n+2; j++){
					if(s[j] == 1) break;
					rs++;
				}
				for(int j = i; j >= 0; j--){
					if(s[j] == 1) break;
					ls++;
				}
			mins = min(rs, ls);
			if(mins > mm){
				st = i;
				maxx = max(rs,ls);
				mm = mins;
			}
			else if(mins == mm){
				maxs = max(ls, rs);
				if(maxs > maxx){
					st = i;
					maxx = maxs;
					mm = min(ls, rs);
				}
			}
		}
		s[st] = 1;
		}
		cout << "Case #" << z << ": " << maxx << " " << mm << endl;
	}
	return 0;
}