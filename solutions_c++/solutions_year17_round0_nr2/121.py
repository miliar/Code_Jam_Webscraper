#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;

typedef long long ll;
ll process(ll N){
	string str = to_string(N);
	const int S = str.size();

	int fall = -1;
	for (int i = 1; i < S; i++){
		if (str[i] < str[i - 1]){
			fall = i;
			break;
		}
	}
	if (fall == -1) return N;

	int target = fall - 1;
	while (target > 0 && str[target - 1] == str[fall - 1]) target--;
	str[target]--;
	for (int i = target + 1; i < S; i++) str[i] = '9';
	return stoll(str);
}

int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		ll N; scanf("%lld", &N);
		printf("Case #%d: %lld\n", tc, process(N));
	}
}