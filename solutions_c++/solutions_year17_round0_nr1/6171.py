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
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		bool flag = 1;
		for(int i = 0; i < s.length() - k + 1; i++)
		{
			if(s[i] == '-')
			{
				ans++;
				for(int j = i; j < i + k; j++)
					if(s[j] == '+') s[j] = '-';
					else s[j] = '+';
			}
		}

		for(int i = 0; i < s.length(); i++)
			if(s[i] == '-')
				flag = 0;

		cout << "Case #" << tt << ": ";
		if(!flag) cout << "IMPOSSIBLE\n";
		else cout << ans << endl;
	}
	return 0;
}