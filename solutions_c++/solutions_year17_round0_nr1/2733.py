#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

void resolve(int ncas){
	cout << "Case #" << ncas +1 << ": ";
	int cont = 0;
	string str;
	int k;
	cin >> str;
	cin >> k;
	bool possible = true;

	while (!str.empty() && str.front() == '+') str.erase(str.begin());

	while (str.size() > 0 && possible){
		if (str.size() < k)
			possible = false;
		else{
			int i = 0;
			while (i < k){
				if (str[i] == '+') str[i] = '-';
				else str[i] = '+';
				++i;
			}
			++cont;
		}

		while (!str.empty() && str.front() == '+') 
			str.erase(str.begin());
	}
	if (possible) cout << cont << '\n';
	else cout << "IMPOSSIBLE\n";
}

int main(){

	ifstream in("A-large.in");
	auto cinbuf = cin.rdbuf(in.rdbuf());
	ofstream on("out.txt");
	auto coutbuf = cout.rdbuf(on.rdbuf()); //save old buf and redirect std::cin to casos.txt


	int numCasos;
	cin >> numCasos;
	for (int i = 0; i < numCasos; ++i)
		resolve(i);

	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);

	return 0;
}