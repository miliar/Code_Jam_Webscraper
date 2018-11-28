#include "bits/stdc++.h"
#define MOD 1000000007
#define INF 11234567890
#define in std::cin
#define out std::cout
#define rep(i,N) for(LL i=0;i<N;++i)
typedef long long int LL;

LL T, N;

int main()
{
	in >> T;
	rep(loop, T)
	{
		in >> N;
		for (LL i = N; i >= 1; --i)
		{
			std::string S = std::to_string(i);
			char prev = '0';
			bool flag = true;
			rep(j, S.length())
			{
				if (S[j] == '0' || (S[j] - '0') < (prev - '0'))
				{
					flag = false;
					break;
				}
				prev = S[j];
			}
			if (flag)
			{
				out << "Case #" << loop + 1 << ": " << i << std::endl;
				break;
			}
		}
	}
	return 0;
}