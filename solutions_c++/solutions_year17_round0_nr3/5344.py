#include <iostream> 
#include <map>
#include <math.h>


using namespace std;

#define REP(i, n) for (int i = 0; i < n; ++i)
#define FOR(i, a, b) for (int i = a; i <= b; ++i)
#define FORD(i, a, b) for (int i = a; i >= b; --i)
#define MAX(a, b) (a > b ? a : b)
#define MIN(a, b) (a < b ? a : b)

int main()
{
	int T;

	cin >> T;

	REP(t, T)
	{
		int l, r;
		long long int N, K;
		long long int count;
		map<long long int, long long int> powcount;
		int queue[100];
		int qp, crntp;


		cin >> N >> K;

		count = 0;
		qp = 0;
		crntp = 1;

		queue[0] = N;

		powcount[N] = 1;
		
		REP(qp, crntp)
		{
			if (queue[qp] == 0)
				break;

			r = (queue[qp]) / 2;
			l = queue[qp] - 1 - r;


			if (powcount.find(r) == powcount.end())
			{
				powcount[r] = powcount[queue[qp]];
				queue[crntp++] = r;
			}
			else
				powcount[r] += powcount[queue[qp]];

			if (powcount.find(l) == powcount.end())
			{
				powcount[l] = powcount[queue[qp]];
				queue[crntp++] = l;
			}
			else
				powcount[l] += powcount[queue[qp]];
		}

		FOR(i, 0, crntp)
		{
			count += powcount[queue[i]];
			if (count >= K)
			{
				r = queue[i] / 2;
				l = queue[i] - 1 - r;
				cout << "Case #" << t + 1 << ": " << MAX(r, l) << " " << MIN(r, l) << endl;
				break;
			}
		}
	}

	return 0;
}