#include <bits/stdc++.h>
using namespace std;

const int EPS = 1e-15;

typedef long long ll;

ll k[10000] , s[10000] , st[10000];

bool cmp(int a,int b){
	return k[a] < k[b];
}

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w+",stdout);
	int T; cin >> T;
	int ca = 0;
	while (T--){
		ll d,n; cin >> d >> n;
		for (int i = 0;i < n;i++){
			cin >> k[i] >> s[i];
			st[i] = i;
		}

		sort( st , st + n, cmp);


		ca++;
		//if (ca != 3) continue;


		double sol = 0;
		for (int ir = 0;ir < n;ir++){
			//cout << "it " << st[ir] << '\n';


			int f = 0;
			int i = st[ir];
			for (int jr = ir + 1;jr < n;jr++){
				int j = st[jr];

				if (s[i] == s[j]) continue;
				double t = double(k[i] - k[j]) / double(s[j] - s[i]);
				double x = k[i] + t * s[i];

				if (t > 0 && x < d){
					//cout << "colision " << t << ' ' << i << ' ' << j << '\n';
					f = 1;
					break;
				}
			}
			if (f == 0){


				//cout << st[ir] << '\n';

				//cout << "sol selected " << ir << "\n";



				//cout << k[i] << ' ' << s[i] << '\n'; 
				//cout << d - k[i] << '\n';
				sol = double(d - k[i]) / double(s[i]);
				break;
			}
		}

		double final = double(d) / double(sol);
		cout << "Case #" << ca<<": " << fixed << setprecision(10) << final << '\n';
	}

}