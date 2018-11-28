#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int D, N;
		cin >> D >> N;
		int horses[N][2];
		double time[N];
		double maintime;
		for (int i = 0; i< N; i++){
			cin >> horses[i][0] >> horses[i][1];
			time[i] = (D-horses[i][0])/((double)horses[i][1]);
		}
		sort(time, time+N);
		maintime = time[N-1];
		cout << "Case #" << t+1 << ": " << setprecision(6) << fixed << D/maintime << endl;
	}
	return 0;
}
