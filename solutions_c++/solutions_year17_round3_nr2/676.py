#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, cas, C, J, tmp, tc, tj, ans;
	int time[1500][3];
	int interval[1500][2];

	cin >> t;
	cas = 1;
	while (t) {
		cin >> C >> J;
		
		tc = 720;
		tj = 720;
		for (int i = 0; i < C+J; ++i)
		{
			cin >> time[i][0] >> time[i][1];
			if (i<C) {
				tc -= time[i][1] - time[i][0];
				time[i][2] = 0;
			}
			else {
				tj -= time[i][1] - time[i][0];
				time[i][2] = 1;
			}
		}

		for (int i = 0; i < C+J; ++i)
			for (int j = i+1; j < C+J; j++)
				if (time[i][0] > time[j][0])
				{
					tmp = time[i][0];
					time[i][0] = time[j][0];
					time[j][0] = tmp;
					tmp = time[i][1];
					time[i][1] = time[j][1];
					time[j][1] = tmp;
					tmp = time[i][2];
					time[i][2] = time[j][2];
					time[j][2] = tmp;
				}

		for (int i = 1; i < C+J; ++i) {
			interval[i][0] = time[i][0]-time[i-1][1];
			if (time[i][2] == time[i-1][2])
				interval[i][1] = time[i][2];
			else
				interval[i][1] = 2;
		}

		interval[0][0] = time[0][0] + 1440 - time[C+J-1][1];
		if (time[0][2] == time[C+J-1][2])
			interval[0][1] = time[0][2];
		else
			interval[0][1] = 2;

		for (int i = 0; i < C+J; ++i)
			for (int j = i+1; j < C+J; j++)
				if (interval[i][0] > interval[j][0])
				{
					tmp = interval[i][0];
					interval[i][0] = interval[j][0];
					interval[j][0] = tmp;
					tmp = interval[i][1];
					interval[i][1] = interval[j][1];
					interval[j][1] = tmp;
				}

		/*for (int i = 0; i < C+J; ++i)
			cout << interval[i][0] << " " << interval[i][1] << endl;
		cout << tc << endl;
		cout << tj << endl;*/

		int check = 0;
		ans = 0;
		for (int i = 0; i < C+J; ++i)
			if (interval[i][1]==0) {
				if (interval[i][0]==0)
					continue;
				if (tc >= interval[i][0])
					tc -= interval[i][0];
				else {
					ans+=2;
					check += interval[i][0];
				}
			} else if (interval[i][1]==1) {
				if (interval[i][0]==0)
					continue;
				if (tj >= interval[i][0])
					tj -= interval[i][0];
				else {
					ans+=2;
					check += interval[i][0];
				}
			}
			else {
					ans++;
					check += interval[i][0];
			}
		
				

		cout << "Case #" << cas++ << ": " << ans << endl;;
		t--;
		/*cout << "--------------" << endl;*/
	}

	return 0;
}