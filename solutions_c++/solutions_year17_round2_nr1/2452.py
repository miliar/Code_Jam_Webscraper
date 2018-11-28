#include <bits/stdc++.h>

using namespace std;
typedef long long int lli;

class horse{
	public:
	int k, s;
};

struct co {
	bool operator() (const horse& a, const horse& b) {
		return (a.k > b.k);
	}
} compare;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	
	int T;
	cin >> T;
	int D, N, si, ki;
	for(int aa=1;aa<=T;++aa)
	{
		cin >> D >> N;
		vector<horse> horses(N);
		for(int i =0;i<N;++i)
		{
			//cerr << i << endl;
			cin >> ki >> si;
			horses[i].k = ki;
			horses[i].s = si;
		}
		sort(horses.begin(), horses.end(), compare);
		double minTime = 0, tv;
		for(int i=0;i<N;++i)
		{
			tv = ((double) (D-horses[i].k))/horses[i].s;
			//cerr << " " << tv << " -> " << (double) D / tv << endl;
			if(minTime < tv)
				minTime = tv;
		}
		double res = (double) D/minTime;

		cout << "Case #" << aa << ": " << fixed << setprecision(9) << res << endl;
	}
	
	return 0;
}
