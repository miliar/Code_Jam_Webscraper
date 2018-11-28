#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, cas, D, N, in, i, spd;
	long double m;
	cin >> T;
	for(cas=1;cas<=T;cas++){
	    cout << "Case #" << cas << ": ";
        cin >> D >> N;
        cin >> in >> spd;
        m = ((long double)(D-in))/spd;
        for(i=1;i<N;i++){
            cin >> in >> spd;
            m = max(m, ((long double)(D-in))/spd);
        }
        cout << fixed << setprecision(6) << D/m << '\n';
	}
	return 0;
}
