#include <cstdio>
#include <string.h>
#include <algorithm>
#include <math.h>
using namespace std;
// typedef long long ll;

int main(int argc, char const *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);

	int t;
	char num[25];
	scanf("%d",&t);

	for (int i = 1; i <= t; ++i)
	{
		printf("Case #%d: ", i);
		scanf("%s", &num);
		int len = strlen(num);

		for (int i = len-1; i > 0; --i){
			if(num[i-1]>num[i]){
				num[i-1] = num[i-1] - 1;
				num[i] = '9';
			}
		}

		for(int i = 0; i < len-1; ++i)
			if(num[i]>num[i+1])num[i+1] = '9';

		bool flag = false;
		for (int i = 0; i < len; ++i)
		{
			if(num[i] > '0')flag=true;
			if(flag)printf("%d", num[i]-'0');
		}
		printf("\n");
	}
	return 0;
}