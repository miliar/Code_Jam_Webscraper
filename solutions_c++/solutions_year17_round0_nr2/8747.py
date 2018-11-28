#include <bits/stdc++.h>
using namespace std;


int main() {
	//freopen("in.in","rt",stdin);
	//freopen("newfile.txt","wt",stdout);

	int z;
	cin >> z;
	for (int t = 1; t <= z; t++) {
		int x;
		cin>>x;
		int ans=0;
		for(int i=x;i>=1;i--){
			int v=i,l=10;
			while(v){
				if(v%10<=l){
					l=v%10;
					v/=10;
				}
				else break;
			}
			if(v==0){
				ans=i;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if (ans != -1)
			cout << ans << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}

	return 0;
}

