#include <iostream>
#include <map>

using namespace std;

typedef map<long long, long long> t_llmap;
typedef t_llmap::reverse_iterator t_rit;

int main()
{
	int T, test;
	long long N, K, count;
	t_llmap m;
	t_rit rit;

	cin>>T;
	for (test = 1; test <= T; test++)
	{
		cin>>N>>K;

		count = 0LL;
		m[N] = 1LL;

		while (1)
		{
			rit = m.rbegin();

			if ((rit->first-1) % 2 != 0)
			{
				m[((rit->first-1)/2)+1] += rit->second;
				m[(rit->first-1)/2] += rit->second;
			}
			else
			{
				m[(rit->first-1)/2] += (rit->second * 2);
			}

			count += rit->second;

			if (count < K)
			{
				m.erase(rit->first);
			}
			else
			{
				break;
			}
		}

		cout<<"Case #"<<test<<": "<<(rit->first / 2)<<" "<<((rit->first % 2 == 0) ? ((rit->first / 2)-1) : (rit->first / 2))<<endl;

		m.clear();
	}

	return 0;
}
//Case #1: 1 0
