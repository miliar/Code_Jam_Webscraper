#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int tc=1;tc<=T;++tc) {
		string N;
		cin >> N;
		int firstdec=-1;
		for (int i=0;i<N.length()-1;++i) if (N[i]>N[i+1]) {
			firstdec = i;
			break;
		}
		cout << "Case #" << tc << ": ";
		if (firstdec == -1) cout << N << endl;
		else {
			while (firstdec > 0 && N[firstdec-1]==N[firstdec]) --firstdec;
			--N[firstdec];
			for (int i=firstdec+1;i<N.length();++i) N[i]='9';
			cout << stoll(N) << endl; //Conversion to remove any leading zero :p
		}
	}
	return 0;
}