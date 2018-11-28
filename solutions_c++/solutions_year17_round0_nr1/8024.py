#include <bits/stdc++.h>
using namespace std;

// types
typedef long long int ll;

int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int tt = 0; tt < T; tt++){

		string s;
		cin >> s;
		int n = s.size();
		int k;
		cin >> k;
		int flips =0;
		for(int i=0;i<n-k+1;i++){
			// flip
			if(s[i] == '-'){
				flips++;
				for(int j=i;j<i+k;j++){
					if(s[j] == '-'){s[j]='+';}
					else{s[j]='-';}
				}
			}
		}
		for(int i=0;i<n;i++){
			if(s[i] == '-'){flips = -1;}
		}
		cout << "Case #" <<tt+1 << ": ";
		if(flips == -1){cout << "IMPOSSIBLE";}
		else{cout << flips;}
		cout << "\n";
	}
	return 0;
}
