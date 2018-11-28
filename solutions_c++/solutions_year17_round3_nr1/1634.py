#include<iostream>
#include<cstdio>
#include<set>
#include<cmath>

using namespace std;
class MyPair
{
public:
	const long long R, H;
	MyPair(long long r, long long h):R(r),H(h) {}
	bool operator<(const MyPair &o) const
	{
		if(R*H != o.R*o.H)
			return (R*H<o.R*o.H);
		return (R<o.R);
	}
};

int main()
{
	int T;
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		cout << "Case #" << t << ": ";
		long long N, K, R, H;
		multiset<MyPair> a;
		scanf("%lld %lld ", &N, &K);
		while(N--)
		{
			scanf("%lld %lld ", &R, &H);
			a.insert(MyPair(R,H));
		}
		multiset<MyPair>::reverse_iterator it = a.rbegin();
		double result = 0;
		long long maxR = 0;
		while(K-- >1)
		{
			result += 2* it->R* it->H;
			if(maxR<it->R)
				maxR = it->R;
			it++;
		}
		long long max = 0;
		for(;it!=a.rend();it++)
		{
			long long c = 2* it->R* it->H;
			if(it->R > maxR)
				c += (it->R)*(it->R);
			else
				c += maxR * maxR;
			if(max < c)
				max = c;
		}
		result += max;
		result *= 3.1415926535897;
		printf("%.7f\n", result);
	}
	return 0;
}

