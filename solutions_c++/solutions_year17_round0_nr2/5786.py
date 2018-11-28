#include <cstdio>
#include <stdlib.h> 
#include <string.h>


char str[101010];

int main(){

	int n=0;

	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		long long number = 0;

		scanf("%lld", &number);

		sprintf(str, "%lld", number);

		for (int j = 0; j < strlen(str); ++j)
		{
			if ((j + 1) == strlen(str))			
				break;
			
			if ((str[j]) > (str[j+1]))
			{		

				str[j]--;		

				for (int k = j; k > 0; --k)
				{
					if (str[k] < str[k- 1])
					{
						str[k] = '9';
						str[k-1]--;
					} else
						break;
				}

				for (int k = j+1; k < strlen(str); ++k)				
					str[k] = '9';
				
				break;
			}
		}
		
		number = strtoll(str,NULL,10);

		printf("Case #%d: %lld\n", i+1,  number);
	}
}