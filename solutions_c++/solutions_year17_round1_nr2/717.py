#include <bits/stdc++.h>
using namespace std;

#define IOS std::ios_base::sync_with_stdio(false);std:cin.tie(0);std::cout.tie(0);
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {

	int casos;
	cin >> casos;
	for(int caso = 1; caso <= casos; caso++) {
		cout << "Case #" << caso << ": ";

		ll n, p;
		vector<ll> rat;
		ll vec[100][100];
		bool tom[100][100];
		memset(tom, 0, sizeof tom);
		pair<ll, ll> cant[100][100];
		cin >> n >> p;
		for(int i = 0; i < n; i++) {
			ll a;
			cin >> a;
			rat.push_back(a); 
		}

		for(int i = 0; i < n; i++)
			for(int k = 0; k < p; k++)
				cin >> vec[i][k];

		for(int i = 0; i < n; i++) {
			for(int k = 0; k < p; k++) {
				ll temp = vec[i][k]*100ll/110ll + (vec[i][k]*100ll % 110ll == 0 ? 0 : 1);
				cant[i][k].first = temp/rat[i] + (temp%rat[i] == 0 ? 0 : 1);
				temp = vec[i][k]*100ll/90ll;// + (vec[i][k]*100 % 90 == 0 ? 0 : 1);
				cant[i][k].second = temp/rat[i];// + (temp%rat[i] == 0 ? 0 : 1);
			}
		}

		for(int i = 0; i < n; i++) sort(cant[i], cant[i] + p);


		int ans = 0;


		for(int i = 0; i < p; i++) {
			for(ll k = cant[0][i].first; k <= cant[0][i].second; k++) {
				bool can = true;
				ll q[100];
				q[0] = i;
				for(int m = 1; m < n; m++) {
					bool vuelta = false;
					for(int s = 0; s < p; s++) {
						if(tom[m][s])
							continue;
						if(k >= cant[m][s].first && k <= cant[m][s].second) {
							vuelta = true;
							q[m] = s;
							break;
						}
						//if(k>= cant[m][s].second) break;
					}
					if(!vuelta) {
						can = false;
						break;
					}
				}
				if(can) {
					ans++;
					for(int m = 0; m < n; m++)
						tom[m][q[m]] = true;
					break;
				}
			}
		}
		cout << ans << endl;

	}

	return 0;
}
