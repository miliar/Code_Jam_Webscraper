#include<cstdio>
#include<vector>

namespace {
	using std::vector;
	typedef long long int ll;

	ll tidy(ll n) {
		vector<ll> digits;
		while (n > 0) {
			digits.push_back(n%10);
			n /= 10;
		}
		int q = digits.size() - 1;
		int r = digits.size() - 1;
		while (q > 0 && digits[q-1] >= digits[q]) {
			q--;
			if (digits[q] > digits[q+1]) r = q;
		}
		if (q > 0) {
			digits[r]--;
			for (int i = r-1;i >= 0;--i) digits[i] = 9;
		}
		ll ans = 0;
		ll fact = 1;
		for (int i = 0;i < digits.size();++i) {
			ans += fact*digits[i];
			fact *= 10;
		}
		return ans;
	}
}

int main() {
	FILE* input;
	FILE* output;
	input = fopen("B-large.in","r");
	output = fopen("tidy_output_large.txt","w");
	int num;
	fscanf(input,"%d",&num);
	for (int i = 0;i < num;++i) {
		ll val;
		fscanf(input,"%lld",&val);
		fprintf(output,"Case #%d: %lld\n",i+1,tidy(val));
	}
}	

