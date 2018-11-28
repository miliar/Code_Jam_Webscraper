#include <bits/stdc++.h>
#include <unordered_set>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;

typedef long long ll;

int T;
ll N;


string solve(ll n) {
	string num = to_string(n);
	int length = num.size();
	ll aux=1;
	int i=0;
	ll r=0;
	while(i<length) {
		r+=aux;
		aux*=10;
		i++;
	}
	assert('0'<'1');
	if(n<r) {
		string ans;
		for(int i=0;i<length-1;i++) {
			ans.pb('9');
		}
		return ans;
	} else {
		int pos=length;
		for(int i=0;i<length-1;i++) {
			if(num[i]>num[i+1]) {
				int j=i-1;
				while(j>=0&& num[j]==num[i]) {
					j--;
				}
				j++;
				num[j]--;
				pos=j+1;
				break;
			} 
		}
		for(int i=pos;i<length;i++) {
			num[i]='9';
		}
		for(int i=0;i<length-1;i++) {
			assert(num[i]<=num[i+1]);
		}
		return num;
	}
	
}
int main() {
	scanf("%d",&T);
	int i=1;
	while(T--) {
		scanf("%lld",&N);
		printf("Case #%d: ",i);
		cout << solve(N);
		puts("");
		i++;
	}
	return 0;
}