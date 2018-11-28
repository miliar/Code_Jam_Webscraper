#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define sd(x) scanf("%lf",&x)
#define sc(x) scanf("%c",&x)
#define ss(x) scanf("%s",x)
#define vl vector<ll>
#define vi vector<int>
#define pb push_back
#define mod 1000000007

	
#define MAXN 200110
#define SQRT 330
#define ls (node<<1)
#define rs ((node<<1)+1)
#define ii pair<int,int>
#define F first
#define S second

ll modpow(ll base, ll exponent,ll modulus){
	if(base==0&&exponent==0)return 0;
	ll result = 1;
	while (exponent > 0){
		if (exponent % 2 == 1)
		    result = (result * base) % modulus;
		exponent = exponent >> 1;
		base = (base * base) % modulus;
	}
	return result;
}


ll N;

string give(string x, int last, bool ok){
	if(ok){
		string y = "";
		for(int i = 0; i < (int)x.size(); i++){
			y += "9";
		}
		return y;
	}
	if((int)x.size() == 0){
		return "";
	}
	for(int i = 9; i >= last; i--){
		string y;
		for(int j = 0; j < (int)x.size(); j++){
			y += to_string(i);
		}
		if(stoll(x) >= stoll(y)){
			y = to_string(i);
			if(i < (x[0] - '0')) ok = true;
			y += give(x.substr(1), i, ok);
			return y;
		}
	}
}

inline void ReadInput(void){
	sl(N);
}

inline void solve(int t){
	string x = to_string(N);
	string y = "";
	for(int i = 0; i < (int)x.size(); i++){
		y += "1";
	}
	if(stoll(x) >= stoll(y)){
		y = give(x, 1, false);
	}else{
		y = "";
		for(int i = 1; i < (int)x.size(); i++){
			y += "9";
		}
	}
	printf("Case #%d: ", t);
	cout << y << endl;
}

inline void Refresh(void){
	
}

int main()
{	
	//ios_base::sync_with_stdio(false);
	int t; si(t);
	for(int i = 1; i <= t; i++){
		ReadInput();
		solve(i);
	}
    return 0;
}

