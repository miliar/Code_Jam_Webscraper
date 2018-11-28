#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int Trova_cambio(int num, string str) {
	int x = 0;
	while (x < (num - 1) ) {
		if (str[x] > str[x + 1])
			return x;
        x++;
	}

    return -1;

}

int main() {
    int t_T;  // input
    string n_N; // input per small e large
	string S;
	bool trovato;
	int i, app;

    cin >> t_T;
    for (int ie = 1; ie <= t_T; ++ie) {
        cin >> n_N;

		S = n_N;
		int n = S.size();


		trovato = false;
		while (!trovato) {
			app = Trova_cambio(n, S);
			if (app	>= 0) {
				S[app] = (char)(S[app] - 1);
				for (int y = app+1; y < n; ++y)
					S[y] = '9';
			}
			else trovato = true;
		}

        cout << "Case #" << ie << ": ";
		if (S[0] == '0')
			i = 1;
		else
			i = 0;

		while (i < n) {
			cout << S[i];
			i++;
		}
		cout << endl;

//        cout << "Case #" << ie << ": " << i << endl;

    }
    return 0;
}

