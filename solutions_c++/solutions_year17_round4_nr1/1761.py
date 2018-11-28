#include <bits/stdc++.h>
using namespace std;

int solve(){
    int n,p;
    cin >> n >> p;
    int mod[4] = {0};
    for(int i = 0; i < n; i++){
	int x;
	cin >> x;
	mod[x%p] += 1;
    }

    //cout << mod[0] << " " << mod[1] << " " << mod[2] << "\n";

    int ans = mod[0];
    if(p <= 1) return ans;
    if(p == 2){
	ans += mod[1]/2;
	mod[1] %= 2;
	if(mod[1]) ans++;
	return ans;
    }

    if(p == 3){
	int q = min(mod[1], mod[2]);
	ans += q;
	mod[1] -= q;
	mod[2] -= q;
	ans += (mod[1]/3);
	ans += (mod[2]/3);
	mod[1] %= 3;
	mod[2] %= 3;
	if(mod[1] + mod[2] > 0) ans += 1;
	return ans;
    }

    if(p == 4){
	int q = min(mod[1], mod[3]);
	ans += q;
	ans += mod[2]/2;
	mod[2] %= 1;
	mod[1] -= q;
	mod[3] -= q;
	if(mod[2] > 0){
	    if(mod[1] > 1){
		mod[1] -= 2;
		ans++;
		mod[2] -= 1;
	    }
	    if(mod[3] > 1){
		mod[3] -= 2;
		ans++;
		mod[2] -= 1;
	    }
	}

	ans += mod[1]/4;
	ans += mod[3]/4;
	mod[1] %= 4;
	mod[3] %= 4;

	if(mod[1] + mod[2] + mod[3] > 0) ans += 1;
	return ans;
    }
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
	cout << "Case #" << i << ": " << solve() << "\n";
    }
    return 0;
}
