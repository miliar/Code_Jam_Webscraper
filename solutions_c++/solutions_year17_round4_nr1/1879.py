#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main(){

	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++){
		int n, p;
		cin >> n >> p;
		int res = 0;
		cout << "Case #" << tt << ": ";

		int niza[n];

		for(int i=0; i<n; i++){
			cin >> niza[i];
		}

		int qq[p];
		memset(qq, 0, sizeof(qq));

		for(int i=0; i<n; i++){
			int id = niza[i]%p;
			qq[id]++;
		}

		res += qq[0];
		for(int i=1; i<=p/2; i++){
			if(i == p-i){
				res += qq[i]/2;
				qq[i] %= 2;
			} else {
				int z = min(qq[i], qq[p-i]);
				res += z;
				qq[i] -= z;
				qq[p-i] -= z;
			}
		}


		if(p == 2 && qq[1]){
			res ++;
		} else if(p == 3){
			if(qq[1]){
				res += (qq[1] + 2)/3;
			} else if(qq[2]){
				res += (qq[2] + 2)/3;
			}
		} else if(p == 4){
			if(qq[1]){
				res += (qq[1] + 3) / 4;
				int onel = (qq[1] + 3) % 4;
				if(onel >= 2 && qq[2]){
					res += 2;
				} else if(onel > 0 || qq[2]){
					res ++;
				}
			} else if(qq[3]){
				res += (qq[3] + 3) / 4;
				int onel = (qq[3] + 3) % 4;
				if(onel >= 2 && qq[2]){
					res += 2;
				} else if(onel > 0 || qq[2]){
					res ++;
				}
			} else if(qq[2]){
				res ++;
			}
		}
		cout << res << endl;
	}
	return 0;
}

