#include<iostream>
#include<vector>
#include<algorithm>
#include<functional>
#include<cmath>
#include<iomanip>
using namespace std;



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	const long double PI = acos(-1.0L);
	
	int T;
	cin >> T;
	
	for(int TCASE = 0; TCASE < T; TCASE++) {
		int n, k;
		cin >> n >> k;
		
		struct Cake {
			int h, r;
		};
		vector<Cake> cakes(n);
		
		for(int i=0;i<n;i++)
			cin >> cakes[i].r >> cakes[i].h;
		
		sort(cakes.begin(), cakes.end(), [&PI](Cake l, Cake r) {
			return 2 * PI * l.r * l.h > 2*PI * r.r * r.h;
		});
		
		long double result = 0;
		
		for(int pick = 0; pick < n; pick++) {
			long double ret;
			{
				Cake &cur = cakes[pick];
				ret = PI * cur.r * cur.r + 2 * PI * cur.r * cur.h;
			}
			for(int i=0, cnt = 1; cnt < k; i++)
				if(i != pick) {
					cnt++;
					ret += 2 * PI * cakes[i].r * cakes[i].h;
				}
			
			result = max(result, ret);
		}
		
		cout << "Case #" << TCASE+1 << ": " << fixed << setprecision(7) << result << '\n';
	}
	
	return 0;
}