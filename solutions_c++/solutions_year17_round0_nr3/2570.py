#include<cstdio>

namespace {
	typedef long long int ll;
	typedef struct {
		ll min;
		ll max;
	} llpair;

	llpair calculate(ll n, ll k) {
		ll level_min = n - 1; 
		ll max_num = 1;
		ll level_num = 1;
		ll total_num = 1;
		while (total_num < k) {
			level_num *= 2;
			total_num += level_num;
			if (level_min%2 == 0) {
				level_min = (level_min - 1)/2;
				max_num += level_num/2;
			} else {
				level_min = (level_min - 1)/2;
			}
		}
		llpair ans;
		if (k - total_num + level_num <= max_num) {
			ans.min = level_min/2;
			ans.max = level_min - ans.min;
		} else {
			ans.min = (level_min - 1)/2;
			ans.max = level_min - 1 - ans.min;
		}
		return ans;
	}
}

int main(int argc, char** argv) {
	if (argc != 3) return 0;
	FILE* input;
	FILE* output;
	input = fopen(argv[1],"r");
	output = fopen(argv[2],"w");
	int t;
	fscanf(input,"%d",&t);
	for (int i = 0;i < t;++i) {
		ll a;
		ll b;
		fscanf(input,"%lld",&a);
		fscanf(input,"%lld",&b);
		llpair ans = calculate(a,b);
		fprintf(output,"Case #%d: %lld %lld\n",i+1,ans.max,ans.min);
	}
}
