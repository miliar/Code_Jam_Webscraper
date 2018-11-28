
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 1003

using namespace std;

string s;
int len;
long long memo[20][11][2][2];

long long DP(int pos, int last, bool menor, bool push){
	
	if(pos == len)return 1;
	long long &ret = memo[pos][last][menor][push];
	
	if(ret != -1)return ret;
	long long ans = 0;
	
	if(menor){
		
		if(push){
			
			for(int i = last; i <= 9; i++)ans += DP(pos + 1, i, menor, push);
		}
		else{// solo el reducido el tamaño(string vacio)
			
			ans += DP(pos + 1, last, menor, push);// reduce más
			for(int i = 1; i <= 9; i++)ans += DP(pos + 1, i, menor, 1);
		}
		
	}
	else{
		
		if(push){
		
			for(int i = last; i < s[pos] - '0'; i++)ans += DP(pos + 1, i, 1, push);
			if(s[pos] - '0' >= last)ans += DP(pos + 1, s[pos] - '0', menor, push);
			
		}
		else{// no push no menor -> begin
			
			ans += DP(pos + 1, last, 1, push);// numero de menor tamaño
			for(int i = 1; i < s[pos] - '0'; i++)ans += DP(pos + 1, i, 1, 1);
			ans += DP(pos + 1, s[pos] - '0', menor, 1);
		}
		
	}
	
	return ret = ans;
}

string toString(long long num){
	
	string ans = "";
	if(num == 0)return "0";
	
	while(num > 0)ans += char(num%10 + '0'), num /= 10;
	reverse(all(ans));
	return ans;
}

long long cuenta(long long hi){
	
	if(hi == 0)return 1;
	
	memset(memo, -1, sizeof memo);
	s = toString(hi);
	
	len = s.size();
	return DP(0, 10, 0, 0);
}

int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		long long n;
		scanf("%lld", &n);
		
		s = toString(n);
		len = s.size();
		
		long long total = cuenta(n);
		long long lo = 0, hi = n, me;
		
		while(lo < hi){
			
			me = lo + (hi - lo)/2;
			if(cuenta(me) == total)hi = me;
			else lo = me + 1;
		}
		
		printf("Case #%d: %lld\n", caso++, lo);
	
	}
}

