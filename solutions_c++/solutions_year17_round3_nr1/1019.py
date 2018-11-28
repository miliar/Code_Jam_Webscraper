#include <bits/stdc++.h>

using namespace std;

long long f(pair<int, int> x){
	return 2LL*x.first*x.second;
}
 
bool cmp(pair<int, int> x, pair<int, int> y){
	long long fx = f(x);
	long long fy = f(y);
	return  (fx > fy) || (fx == fy) && (x.first > y.first);
}
const double pi = 3.1415926535897932384626433832795;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    cout.precision(24);
    for (int oo = 1; oo <= T; oo++){
        cout << "Case #" << oo << ": ";
        int n, k;
        cin >> n >> k;
        vector <pair<int, int> > a(n);
        for (int i=0;i<n;i++){
        	int x, y;
        	cin >> x >> y;
        	a.push_back(make_pair(x, y));
        }
        sort(a.begin(), a.end(), cmp);
        long double mans = 0;
        for (int l = 0; l<n; l++){	     
	        long double ans = 0;
	        ans += 1LL*a[l].first*a[l].first + f(a[l]);
	        int s = 1;
	        for (int i = 0; i < n; i++){
	        	if ((i != l) && (a[i].first <= a[l].first) && (s < k)){
	        		ans += 2LL*a[i].first*a[i].second;
	        		s++;
	        	}
	        }
	        if ((ans > mans) && (s == k))
	        	mans = ans;
	    }
        cout << mans * pi << endl;
    }   
    return 0;
}
