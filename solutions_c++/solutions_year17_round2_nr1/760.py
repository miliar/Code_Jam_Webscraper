#include <vector>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long  double ld;

int main()
{	
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";

		int D,N;
		cin >> D >> N;

		ld slowest = 0;
		
		vector<ld> pos(N);
		vector<ld> speed(N);
		for(int j = 0; j < N; j++)
		{
			cin >> pos[j] >> speed[j];
			slowest = max(slowest, (D - pos[j]) / speed[j]);
		}
		
		cout << setprecision(20) << D / slowest << endl;
	}
}
