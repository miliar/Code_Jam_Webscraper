#include <cstdio>

int val[20];
int result[20];
int m;

bool dfs(int p, bool any){
	if (p == -1){
		bool skipZero = true;
		for (int i = m - 1; i >= 0; i--){
			if (skipZero && result[i] == 0)
				continue;
			skipZero = false;
			printf("%d", result[i]);
		}
		puts("");
		return true;
	}
	if (any) {
		result[p] = 9;
		return dfs(p - 1, any);
	} else {
		if (val[p] >= val[p + 1]){
			result[p] = val[p];
			bool r = dfs(p - 1, any);
			if (r==false){
				if ((result[p] = val[p] - 1) >= 0) {
					if (result[p] >= val[p + 1])
						return dfs(p - 1, true);
					else
						return false;
				} else return false;
			} else return true;
		} else {
			return false;
		}
	}
}

int main(){
	freopen("B.in", "r", stdin);
	int T; scanf("%d", &T);
	for (int Tcase = 0; Tcase < T; Tcase++){
		
		printf("Case #%d: ", Tcase+1);
		long long n; scanf("%lld", &n); m = 0;
		while (n){
			val[m++] = n % 10;
			n /= 10;
		}
		val[m] = 0;
		result[m] = 0;
		dfs(m - 1, false);
	}

}