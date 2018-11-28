#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;


int main(){
#ifndef DOMJUDGE
	//_CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF_CRTDBG_LEAK_CHECK_DF);
	ifstream in("C:/Users/Alejandro/Desktop/Google Code Jam/2017/B/prueba.txt");
	auto cinbuf = cin.rdbuf(in.rdbuf());
	ofstream out("C:/Users/Alejandro/Desktop/Google Code Jam/2017/B/small.txt");
	auto coutbuf = cout.rdbuf(out.rdbuf());
#endif
	int numcasos;
	cin >> numcasos; 
	for (int h = 0; h < numcasos; ++h){
		string lim;
		cin >> lim;
		bool mod = false;
		size_t tam = lim.size() - 1;
		for (int i = 0; i < tam; ++i){
			if (lim[i] > lim[i + 1]){
				--lim[i];
				for (int j = i + 1; j < lim.size(); ++j) lim[j] = '9';
				if (i > 0) i -= 2;
			}
		}
		cout << "Case #" << h + 1 << ": ";
		int t = 0;
		while (lim[t] == '0') ++t;
		for (; t < lim.size(); ++t) cout << lim[t];
		cout << '\n';
	}
#ifndef DOMJUDGE
	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);
#endif

	return 0;
}