/*
Anik Dasgupta
username : willhunting
email : anikd96@gmail.com
Jadavpur University, Kolkata
*/

#include <bits/stdc++.h>
using namespace std;

#define fi  	first
#define se  	second
#define pb  	push_back
#define mp  	make_pair
#define ll  	long long
#define inf 	INT_MAX/3
#define mod 	1000000007ll
#define PI  	acos(-1.0)
#define linf	(1ll<<60)-1
#define sc(t)	scanf("%d", &t)

template <class T> inline T bigmod(T p,T e,T M){
    ll ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++)
	{
		double d, n;
		cin >> d >> n;
		double time[(int)n + 9];
		for(int i = 0; i < n; i++)
		{
			double start, speed;
			cin >> start >> speed;
			time[i] = (d - start)/speed;
		}

		double ans = d/time[0];
		for(int i = 1; i < n; i++)
			ans = min(ans, d/time[i]);

		cout << "Case #"<< tt << ": ";
		printf("%.6lf\n", ans);

	}
	return 0;
}