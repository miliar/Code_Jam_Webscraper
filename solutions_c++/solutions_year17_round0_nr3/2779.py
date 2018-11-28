#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <queue>

using namespace std;

using lli = long long int;

void resolve(int ncas){
	cout << "Case #" << ncas + 1 << ": ";
	lli n, k;
	cin >> n >> k;
	if (n == k)
		cout << 0 << ' ' << 0 << '\n';
	else{

		int j = 0;
		lli pot = 1;
		while (j < 64 && pot <= k){
			++j;
			pot = pot * 2;
		}
		pot /= 2;
		--j;

		lli num1, num2, cont1, cont2;
		num1 = (n - (pot - 1)) / pot + 1;
		num2 = num1 - 1;
		cont1 = (n - (pot - 1)) % pot;
		cont2 = pot - cont1;

		k -= (pot - 1);

		lli num;
		if (k <= cont1)
			num = num1;
		else num = num2;
		if (num % 2 == 0){
			cout << num / 2 << ' ' << (num - 1) / 2 << '\n';
		}
		else{
			cout << (num - 1) / 2 << ' ' << (num - 1) / 2 << '\n';
		}
	}

}

int main(){

	ifstream in("C-large.in");
	auto cinbuf = cin.rdbuf(in.rdbuf());
	ofstream on("C-large.txt");
	auto coutbuf = cout.rdbuf(on.rdbuf()); //save old buf and redirect std::cin to casos.txt


	int numCasos;
	cin >> numCasos;
	for (int i = 0; i < numCasos; ++i)
		resolve(i);

	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);

	return 0;
}