#include <stdio.h>
#include <string.h>

int main()
{
	static const size_t buff_size = 1000;
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		char buff[buff_size+1] = { 0 };
		unsigned int k = 0,ans = 0;
		scanf("%s%d",buff,&k);
		for(size_t i = 0,len = strlen(buff);i + k <= len;++i)
		{
			if(buff[i] == '+') continue;
			++ ans;
			for(size_t j = 0;j < k;++j) buff[i+j] = '+' + '-' - buff[i+j];
		}
		for(size_t i = 0,len = strlen(buff);i < len;++i)
		{
			if(buff[i] == '-')
			{
				ans = (unsigned int)(-1);
				break;
			}
		}

		printf("Case #%d: ",iCases);
		if((unsigned int)(-1) == ans) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}