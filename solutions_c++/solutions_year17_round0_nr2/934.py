#include <stdio.h>
#include <string.h>
#include <assert.h>

template<class data_t> inline data_t str_to_int(const unsigned int* digit,size_t size)
{
	data_t num = 0;
	for(size_t i = size - 1;i != (size_t)(-1);--i)
	{
		num *= 10;
		num += digit[i];
	}
	return num;
} 

template<class data_t> inline size_t int_to_str(data_t num,unsigned int* digit,size_t size)
{
	memset(digit,0,sizeof(unsigned int)*size);
	size_t pos = 0;
	if(0 == num) ++ pos;
	for(;num > 0;num /= 10,++pos) digit[pos] = num%10;  
	return pos;
}

bool is_tidy(const unsigned int* digit,size_t size)
{
	for(size_t i = 0;i + 1 < size;++i)
	{
		if(digit[i] < digit[i+1]) return false;
	}
	return true;
}

int main()
{
	static const size_t buff_size = 100;
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned long long v = 0;scanf("%I64d",&v);

		unsigned int digit[buff_size] = { 0 },output[buff_size] = { 0 };
		size_t pos = int_to_str(v,digit,buff_size);

		unsigned long long ans = 0;
		if(is_tidy(digit,pos)) ans = v;
		else
		{
			for(size_t i = 0;i < pos;++i)
			{
				if(0 == digit[i]) continue;
				output[pos] = 0;
				for(size_t j = pos - 1;j != i;--j) output[j] = digit[j];
				output[i] = digit[i] - 1;
				for(size_t j = i - 1;j != (size_t)(-1);--j) output[j] = 9;
				if(is_tidy(output,pos))
				{
					ans = str_to_int<unsigned long long>(output,pos);
					break;
				}
			}
		}

		printf("Case #%u: %I64u\n",iCases,ans);
	}
	return 0;
}