/*input
3
---+-++- 3
+++++ 4
-+-+- 4
*/
#include<bits/stdc++.h>

using namespace std;

int flips(string a, int k) {
  	int M = a.size();
  	int s[M];
	for(int i = 0; i < M; ++i) 
		s[i] = 0;
  	int sum = 0, ans = 0;
  	for(int i = 0; i < M; ++i){
    		s[i] = ((a[i] + sum) % 2 != 1);
    		sum += s[i] - (i >= k-1 ? s[i-k+1] : 0);
    		ans += s[i];
    		if(i > M-k and s[i] != 0) 
			return -1;
  	}
  	return ans;
}

int main(){
	// freopen("source.in", "rt", stdin);
	// freopen("output.out", "wt", stdout);
	int t;
	cin >> t;
	for(int q = 1; q <= t; q++){
		string a, a1="";
		int k;
		cin >> a >> k;
		for(int i = 0; i < a.size(); ++i){
			if(a[i] == '+')
				a1+='1';
			else
				a1+='0';
		}
		int w = flips(a1, k); 
		if(w == -1)
			cout << "Case #" << q << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << q << ": " << w << endl; 
	}
return 0;
}
