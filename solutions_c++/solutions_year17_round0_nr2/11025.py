 #include <iostream>
#include <string>

long long int power(int i) {
	long long pow = 1;
	while (i > 0) {
		pow *= 10;
		i--;
	}
	return pow;
}

using std::cin;
using std::cout;

void nofinder(long long int &N) {
	std::string s = std::to_string(N);
	int i = s.size(), ins=-1;
	int no1 = 0, no2 = 0;
	i--;
	while (i > 0) {
		if (s[i - 1] > s[i]) {
			ins = i - 1;
		}
		i--;
	}
	if (ins != -1) {
		//ins--;
		long long int M=0;
		int j = ins,k=-1;
		while (1) {
			M = N - (N%power(j+1)) + (s[s.size()-1-j]-'0')*power(j) - 1 ;
			std::string t = std::to_string(M);
			i = t.size();
			i--;
			while (i > 0) {
				if (t[i - 1] > t[i]) {
					k = 0;
					break;
				}
				i--;
			}
			if (k == -1) {
				N = M;
				return;
			}
			k = -1;
			j++;
		}
	}
}



int main() {
	int T,j;
	long long int N;
	cin >> T;
	j = 1;
	while (j <= T) {
		cin >> N;
		nofinder(N);
		cout << "Case #"<< j << ": " << N <<'\n';
		j++;
	}
}