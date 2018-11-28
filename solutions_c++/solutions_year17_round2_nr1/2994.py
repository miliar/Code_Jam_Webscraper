#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		int D, N;
		cin >> D >> N;

		double last_time_to_dest = 0;
		for(int i = 0; i < N; ++i)
		{
			int K, S;
			cin >> K >> S;
			double time = static_cast<double>(D - K) / static_cast<double>(S);
			if(time > last_time_to_dest)
				last_time_to_dest = time;
		}

		double speed = static_cast<double>(D) / last_time_to_dest;
		printf("Case #%d: %.06lf\n", t, speed);
	}
}