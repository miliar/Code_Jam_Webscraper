#include <cstdio>
bool invalid;
int T, digit[20], pos;
long long N;
int main (){
	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		invalid = true;
		scanf("%I64d", &N);
		while (invalid){
			invalid = false;
			pos = 0;
			while (N){
				digit[pos] = N % 10;
				N /= 10;
				pos++;
			}
			if (pos == 1)
				N = digit[0];
			else {
				for (int i = pos - 1; i >= 1; i--){
					if (digit[i - 1] < digit[i]){
						for (int j = i - 1; j >= 0; j--)
							digit[j] = 0;
						invalid = true;
					}
				}
				for (int i = pos - 1; i >= 0; i--){
					N *= 10;
					N += digit[i];
				}
				if (invalid)
					N--;
			}
		}
		printf("Case #%d: %I64d\n", i, N);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
