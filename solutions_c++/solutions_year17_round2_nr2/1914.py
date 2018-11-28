#include <bits/stdc++.h>
using namespace std;


int c[10];
int vs[10];
int ind[10];

typedef long long ll;

bool cmp(int a,int b){
	return vs[a] > vs[b];
}

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w+",stdout);
	int T; cin >> T;
	int ca = 0;

	while (T--){
		ca ++;

		int n; cin >> n;
		
		for (int i = 0;i < 6;i++){
			cin >> c[i];
			//cout << c[i] << '\n';
		}
		//if (ca != 49) continue;
		bool imp = 0;

		vs[0] = c[0];
		vs[1] = c[2];
		vs[2] = c[4];

		//-cout << vs[0] << ' ' << vs[1] <<' ' << vs[2] << '\n';

		if (vs[0] > vs[1] + vs[2]){
			imp = 1;
		}else if(vs[1] > vs[0] + vs[2]){
			imp = 1;
		}else if(vs[2] > vs[0] + vs[1]){
			imp = 1;
		}


		if (imp){
			cout << "Case #" << ca<<": IMPOSSIBLE\n"; 
			continue;
		}

		ind[0] = 0;
		ind[1] = 1;
		ind[2] = 2;

		sort( ind , ind + 3, cmp);

		int ans[2000];
		for (int i = 0;i < 2000;i++){
			ans[i] = -1;
		}
		int j = 0;
		for (int i = 0;i < 3;i++){
			int cnt = vs[ ind[i] ];
			//cout << i << ' ' << cnt << '\n';
			
			while (cnt -- ){
				while (ans[j] != -1) j=(j+1)%n;

				//cout << " put " << ind[i] << " on " << j << '\n';
				ans[j] = ind[i];
				j = (j+2)%n;
			}
			j = (j-1+n)%n;
		}
		cout << "Case #"<<ca<<": ";
		for (int i = 0;i < n;i++){
			if (ans[i] == 0){
				cout << "R";
			}else if(ans[i] == 1){
				cout << "Y";
			}else if(ans[i] == 2){
				cout << "B";
			}else if(ans[i] == -1){
				cout << "Fatal error!!!!!!" << '\n';
				return 0;
			}
		}
		cout << '\n';

	}
}