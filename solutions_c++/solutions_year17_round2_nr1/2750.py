#include<bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i=(int)a; i<(int)b; i++)
#define INF 0x3f3f3f3f


int main(){

	int n, d, c, bi=1;
	double t, a, b, tm;
	
	cin>>n;
	
	while(n--){
		cin>>d>>c;
		tm = 0;
		rep(i, 0, c){
			cin>>a>>b;
			t = (d-a)/b;
			tm = max(tm, t);
		}
		cout << fixed<< setprecision(6) << "Case #" << bi++ << ": " << d/tm << endl;
	}
	
	return 0;
}
