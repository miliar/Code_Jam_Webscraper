#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>
#include <assert.h>

using std::vector;
using std::string;

char get_first_valid(const string& s)
{
	char firstc = '?';
	for(size_t k = 0;k < s.size();++k)
	{
		if(s[k] != '?')
		{
			firstc = s[k];
			break;
		}
	}
	return firstc;
}

void fill_line(string& s,char firstc)
{
	for(size_t k = 0;k < s.size();++k)
	{
		if(s[k] == '?')
		{
			s[k] = firstc;
		}
		else
		{
			firstc = s[k];
		}
	}
}

int main()
{
	static const size_t buff_size = 100;
	char buff[buff_size+1] = { 0 };
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int r = 0,c = 0;scanf("%d%d",&r,&c);
		vector<string> data(r);
		for(unsigned int i = 0;i < r;++i)
		{
			scanf("%s",buff);
			data[i] = buff;
		}
		for(unsigned int i = 0;i < r;++i)
		{
			char firstc = get_first_valid(data[i]);
			if(firstc != '?')
			{
				fill_line(data[i],firstc);
			}
			else if(0 != i)
			{
				for(unsigned int k = 0;k < c;++k)
				{
					data[i][k] = data[i-1][k];
				}
			}
		}
		for(unsigned int i = r - 1;i != (unsigned int)(-1);--i)
		{
			char firstc = get_first_valid(data[i]);
			if(firstc == '?')
			{
				assert(i != (r-1));
				for(unsigned int k = 0;k < c;++k)
				{
					data[i][k] = data[i+1][k];
				}
			}
		}

		printf("Case #%u:\n",iCases);
		for(unsigned int i = 0;i < r;++i) printf("%s\n",data[i].c_str());
	}
	return 0;
}