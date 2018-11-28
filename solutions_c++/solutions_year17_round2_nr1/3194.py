#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

struct horse { int pos; double speed; double time; };


double calc(int D, horse& A) {
	return (D - A.pos) / A.speed;
}

bool position(horse &A, horse &B)
{
	return A.pos < B.pos;
}

bool time(horse &A, horse &B)
{
	return A.time > B.time;
}

int main() {

	ofstream out;
	out.open("results.out");
	out << fixed;
	out.precision(6);
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		vector<horse> horses;

		int D, N; cin >> D >> N;

		for (int k = 0; k < N; k++)
		{
			horse temp;
			cin >> temp.pos >> temp.speed;
			horses.push_back(temp);

		}

		sort(horses.begin(), horses.end(), position);

		horses[N - 1].time = calc(D, horses[N - 1]);
		for (int k = N - 2; k >= 0; k--)
		{
			horses[k].time = max(calc(D, horses[k]), calc(D, horses[k + 1]));
		}

		sort(horses.begin(), horses.end(), time);

		out << "Case #" << i << ": " << D / horses[0].time << "\n";

	}


	out.close();
	return 0;
}