#include <iostream>
#include <cstring>
using namespace std;
int main(){
	int tc;
	cin >> tc;
	for (int t=1;t<=tc;t++){
		int k, n, ans; string s;
		cin >> s >> k;
		ans =0; n=s.size();
		for (int i=0;i<=n-k;i++) if (s[i]== '-'){
			ans++;
			for (int j=i;j<i+k;j++){
				s[j] = (s[j]=='-'? '+': '-');
			}
		}

		bool lose = false;
		for (int i=n-k;i<n;i++){
			if (s[i]=='-') lose = true;
		}
		if (!lose)
			cout << "Case #" << t << ": "<< ans << endl;
		else
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
