#include <fstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <unordered_map>
using namespace std;

long long p[1000];
unordered_set<long long> st;
unordered_map<long long, long long> mp;

void build_sum()
{
	const long long p_max = 1000000000000000000LL;
	p[0] = 1;
	int i = 0;
	
	while(p[i] < p_max)
	{
		p[i + 1] = 2 * p[i];
		++i;
	}	
}

long long get_count(long long nr, long long N)
{
	if(nr == N)
	{
		return 1;
	}
	if(nr > N)
	{
		return 0;
	}
	if(st.find(nr) == st.end())
	{
		return 0;
	}
	if(mp.find(nr) != mp.end())
	{
		return mp[nr];
	}
	
	long long ans = get_count(2 * nr, N) + 2 * get_count(2 * nr + 1, N) + get_count(2 * nr + 2, N);
	return mp[nr] = ans;
}

pair<long long, long long> solve(long long N, long long K)
{
	int i = 0;
	
	while(K > p[i])
	{
		K -= p[i];
		++i;
	}
	
	long long N1 = N;
	long long prevN1;
	long long a = N;
	long long b = N;
	for(int j = 0;j <= i;++j)
	{
		prevN1 = N1;
		N1 /= 2;
		
		st.insert(a / 2);
		st.insert(b / 2);
		if(a % 2 == 0)
		{
			st.insert(a / 2 - 1);
			b = a / 2;
			a = a / 2 - 1;
		}
		else if(b % 2 == 0)
		{
			st.insert(b / 2 - 1);
			a = b / 2 - 1;
			b = b / 2;
		}
		else
		{
			a = a / 2;
			b = b / 2;
		}
	}
	
	long long left = 0;
	long long right = 0;
	long long cnt = get_count(prevN1, N);
	
	if(prevN1 % 2 == 0)
	{
		left = N1 - 1;
		right = N1;
		if(K > cnt)
		{
			--right;
		}
	}
	else
	{
		left = N1;
		right = N1;
		if(K > cnt)
		{
			--left;
		}
	}
	
	return make_pair(right, left);
}

int main()
{
	ifstream in("C.in");
	ofstream out("C.out");
	
	int t;
	in >> t;
	
	build_sum();
	for(int i = 0;i < t;++i)
	{
		long long N, K;
		
		in >> N >> K;
		st.clear();
		mp.clear();
		pair<long long, long long> ans = solve(N, K);
		
		out<<"Case #"<<i + 1<<": "<<ans.first<<" "<<ans.second<<"\n";
	}
	
	in.close();
	out.close();
}
