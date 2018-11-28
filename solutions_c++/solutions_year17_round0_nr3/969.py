#include <cstdio>
#include <iostream>
#include <deque>
using namespace std;

deque< pair<long long,long long> > d;

void add(long long len, long long num)
{
	if (d.back().first == len)
		d.back().second += num;
	else
		d.push_back(make_pair(len, num));
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++)
	{
		long long a, k;
		long long ans1, ans2;
		cin>>a>>k;
		d.clear();
		d.push_back(make_pair(a,1));
		while (1)
		{
			pair<long long,long long> tmp = d.front();
			d.pop_front();
			long long len = tmp.first;
			long long num = tmp.second;
			//cerr<< len << ' '<< num <<endl;
			if (num >= k)
			{
				ans1 = len / 2;
				ans2 = len - len / 2 - 1;
				break;
			}
			k -= num;
			if (len % 2 == 0)
			{
				add(len/2, num);
				add(len/2-1, num);
			}
			else
				add(len/2, num*2);
		}
		cout<<"Case #"<<t<<": "<<ans1<<' '<<ans2<<endl;	
	}
	return 0;
}