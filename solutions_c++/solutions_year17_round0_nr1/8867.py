#include "bits/stdc++.h"
#define MOD 1000000007
#define INF 11234567890
#define in std::cin
#define out std::cout
#define rep(i,N) for(LL i=0;i<N;++i)
typedef long long int LL;

int T, K;
std::string S;
int ans;

int main()
{
	in >> T;
	rep(loop, T)
	{
		ans = 0;
		in >> S >> K;
		rep(i, S.length() - K + 1)
		{
			if (S[i] == '-')
			{
				++ans;
				rep(j, K) { S[i + j] = ((S[i + j] == '-') ? ('+') : ('-')); }
			}
		}
		for (auto c : S)
		{
			if (c == '-') { ans = -1; break; }
		}
		if (ans == -1) { out << "Case #" << loop + 1 << ": " << "IMPOSSIBLE" << std::endl; }
		else { out << "Case #" << loop + 1 << ": " << ans << std::endl; }
	}
	return 0;
}