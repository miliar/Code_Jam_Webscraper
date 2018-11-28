#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <string.h>
using namespace std;

typedef long long LL;
int main(int argc, char const *argv[])
{
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		printf("Case #%d: ",t+1);

		LL llN;
		char strN[50];
		cin>>llN;
		if(llN<10)
		{
			printf("%lld\n",llN);
			continue;
		}
		
		sprintf(strN,"%lld",llN);
		int len=strlen(strN);
		// printf("strN is %s\n", strN);
		// printf("strN[len-1-0] is %s\n", &strN[len-1-0]);
		
		// continue;
		
		for (int i = 0; i < len; ++i)
		{
			LL diff;
			if(strN[len-1-i-1]>strN[len-1-i])
			{
				// printf("str@%d is %s\n",i, &strN[len-1-i]);
				sscanf(&strN[len-1-i],"%lld",&diff);
				// printf("diff is %lld\n",diff );
				llN-=diff;
				--llN;
				sprintf(strN,"%lld",llN);
				len=strlen(strN);	
				// printf("strN is %s\n", strN);
			}
		}
		printf("%lld\n",llN );

	}

	
	
	
	return 0;
}