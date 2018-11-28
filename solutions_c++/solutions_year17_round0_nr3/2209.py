#include <iostream>
#include <string>

using namespace std;

unsigned long long powers[61];

void calculatePowers() {
	unsigned long long power = 1;
	powers[0] = 1;
	for (int i = 1; i < 61; i++) {
		power *= 2;
		powers[i] = power;
		//~ cout << power << endl;
	}
}

void printMaxMinStalls(unsigned long long N, unsigned long long K) {
	int section = 0;
	//~ cout << N << " " << K << endl;
	while (K > powers[section] - 1)
		section++;
	section--;
	unsigned long long power = powers[section];
	unsigned long long power_ = power - 1;
	unsigned long long stalls = (N - power_) / power;
	//~ cout << power << " " << (N - power_) / power << endl;
	//~ cout << K - power << " " << (N - power_) % power << endl;
	if (K - power < (N - power_) % power)
		stalls++;
	//~ cout << stalls << endl;
	cout << stalls / 2 << " " << (stalls - 1) / 2;
}

int main() {
	int T;
	calculatePowers();
	cin >> T;
	for (int iCase = 1; iCase <= T; iCase++) {
		unsigned long long N, K;
		cin >> N >> K;
		cout << "Case #" << iCase << ": ";
		printMaxMinStalls(N, K);
		cout << endl;
	}
}
