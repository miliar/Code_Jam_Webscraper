#include <cstdio>
#include <algorithm>
#include <string.h>
using namespace std;
#define inf 0x3f3f3f3f
char str[1005];

void flip(int start, int end, int &flipped){
	for (int i = start; i < end; ++i)
	{
		if(str[i] == '-'){
			++flipped;
			str[i] = '+';
		}else{
			--flipped;
			str[i] = '-';

		}
	}
}

int main(int argc, char const *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int size, k;
	int t;
	scanf("%d", &t);
	int tc = t;
	while(t--){
		printf("Case #%d: ", tc-t);
		scanf("%s %d", str, &k);
		size = 0;
		int q = 0;
		while(str[size] != '\0'){
			if(str[size] == '+')
				++q;

			++size;
		}

		int f=0;

		for (int i = 0; i <= size-k; ++i)
		{
			if(str[i] == '-'){
				flip(i,i+k,q);
				++f;
			}
		}

		q == size?printf("%d\n", f):puts("IMPOSSIBLE");
	}
	return 0;
}