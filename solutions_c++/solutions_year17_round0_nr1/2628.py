#include <iostream>
#include <string>

using namespace std;

int main()
{
	int TM;
	cin >> TM;
	for (int T=1; T<=TM; T++) {
		string s;
		cin >> s;
		int K;
		cin >> K;
		int ct=0;
		for (int i=0; i<=s.size()-K; i++) {
			if (s[i] == '-') {
				ct++;
				for (int j=0; j<K; j++)
					s[i+j] ^= 6;
			}

			//cout << s << endl;
		}

		bool ok=true;
		for (int i=s.size()-K+1; i < s.size(); i++) {
			if (s[i] == '-')
				ok = false;
		}

		if (ok)
			cout << "Case #" << T << ": " << ct << "\n";
		else
			cout << "Case #" << T << ": IMPOSSIBLE\n";
	}
}
