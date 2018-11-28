#include <algorithm>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>

typedef unsigned long long ulong;
typedef unsigned uint;
using namespace std;
static const char nl = '\n';

pair<ulong,ulong> go2(ulong N,ulong K)
{
	vector<bool> S(N+2);
	S[0] = true;
	S[N+1] = true;
	auto l = make_pair(N,N);
	while(K > 0)
	{
		uint bestIndex = 0;
		auto bestVal = make_pair(0ULL,0ULL);
		for(uint i = 1;i <= N;++i)
		{
			if(S[i]) continue;
			ulong Ls = 0;
			while(!S[i-(Ls+1)]) ++Ls;
			ulong Rs = 0;
			while(!S[i+(Rs+1)]) ++Rs;
			ulong f = max(Ls,Rs);
			ulong s = min(Ls,Rs);
			if(s > bestVal.second || bestIndex == 0)
			{
				bestVal = make_pair(f,s);
				bestIndex = i;
			}
			else if(s == bestVal.second && f > bestVal.first)
			{
				bestVal = make_pair(f,s);
				bestIndex = i;
			}
		}
		S[bestIndex] = true;
		l = bestVal;
		--K;
	}
	return l;
}


pair<ulong,ulong> go(ulong N,ulong K)
{
	if(K == 0) return make_pair(N,N);
	if(N == K) return make_pair(0,0);

	ulong chosen = N/2;
	if(N % 2 == 0) chosen -= 1;
	ulong left = K-1;
	ulong split = left / 2;
	ulong rem = left % 2;
	
	pair<ulong,ulong> v;
	ulong Ls = chosen;
	ulong Rs = N - (chosen + 1);
		
	if(left == 0)
	{
		ulong f = max(Ls,Rs);
		ulong s = min(Ls,Rs);
		v = make_pair(f,s);
	}
	else 
	{
		ulong Kn = split+rem;
		if(Ls == Rs)
		{
			v = go(Ls,Kn);
		}
		else if(left % 2 == 1)
		{
			v = go(Rs,Kn);
		}
		else
		{
			v = go(Ls,Kn);
		}
	}
	return v;
}

pair<ulong,ulong> go()
{
	ulong N, K;
	cin >> N >> K;
	return go(N,K);
}

int main(int argc,char* argv[])
{
	ios_base::sync_with_stdio(false);
#if 1
	uint T;
	cin >> T;
	for(uint i = 0;i < T;++i)
	{
		auto p = go();
		cout << "Case #" << (i+1) << ": " << p.first << ' ' << p.second << nl;
	}
#else
	for(uint i = 1;i <= 1000;++i)
	{
		for(uint j = 0;j <= i;++j)
		{
			auto p1 = go2(i,j);
			auto p2 = go(i,j);
			if(p1 != p2)
			{
				cout << "Doh!\n";
			}
		}
	}
#endif
	return 0;
}
