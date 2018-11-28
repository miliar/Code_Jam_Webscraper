#include <bits/stdc++.h>

using namespace std;

vector<double> p;
double u;

long double f(long double x){
	long double res = 0.0;
	long double s = 0;
	for (int i = 0; i < p.size(); i++){
		if (p[i] < x){
			s += x - p[i];
			res += log(x);
		}else
			res += log(p[i]);
	}
	if (s > u)
		return -1;
	else
		return exp(res);
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    cout.precision(20);
    for (int oo = 1; oo <= T; oo++){
        cout << "Case #" << oo << ": ";
        int n, k;
        cin >> n >> k;
        cin >> u;
        p.assign(n, 0);
        for (int i = 0; i < n; i++)
        	cin >> p[i];
 		sort(p.begin(), p.end());
 		long double l = 0, r = 1;
 		for (int i = 0; i < 100; i++){
 			long double m = (l+r)/2.0;
 			if (f(m) != -1)
 				l = m;
 			else
 				r = m; 
 		}    
 		long double ans = f(l); 
 		cout << ans << endl;
    }   
    return 0;
}
