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

	
#define MAXN 2010
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


string str;

int K;

bool what[MAXN];

inline void ReadInput(void){
	cin >> str >> K;
}

inline void solve(int t){
	string ans;
	int c = 0;
	int len = str.size();
	for(int i = 0; i < len; i++){
		if(str[i] == '+'){
			what[i] = true;
		}else{
			what[i] = false;
		}
	}
	for(int i = 0; i <= len - K; i++){
		if(what[i] == false){
			for(int j = i; j < i + K; j++){
				what[j] = !what[j];
			}
			c++;
		}
	}
	bool flag = false;
	for(int i = 0; i < len; i++){
		if(what[i] == false) flag = true;
	} 
	if(flag) ans = "IMPOSSIBLE";
	else ans = to_string(c);
	printf("Case #%d: ", t);
	cout << ans << endl;
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

