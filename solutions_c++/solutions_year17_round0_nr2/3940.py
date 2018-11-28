#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for (int c = 0; c < T; ++c) {
		string N;
		cin >> N;
		int last = N.size() - 1;
		int change_from = 0;
		while (change_from < last && N[change_from+1] >= N[change_from])
			++change_from;
		//cout << "Change from: " << change_from << endl;
		if (change_from != last)	
			while (change_from > 0 && N[change_from-1] == N[change_from])
				--change_from;
		//cout << "Change from: " << change_from << endl;
		/*if (last && N[change_from] == '1') {
			string out(last, '9');
			cout << "Case #" << (c+1) << ": " << out << "\n";
			continue;
		}*/
		if (last && change_from < last)
			--N[change_from];
		for (int i = change_from+1; i <= last; ++i) {
			N[i] = '9';
		}
		if (N[0] == '0')
			N.erase(0, 1);
		cout << "Case #" << (c+1) << ": " << N << "\n";
	}
	return 0;
}
