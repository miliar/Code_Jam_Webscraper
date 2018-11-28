#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cctype>
#include <functional>
#include <iomanip>

using namespace std;

using lli = long long int;

void resolve(int ncas){
	cout << "Case #" << ncas + 1 << ": ";
	lli destiny;
	int n;
	cin >> destiny >> n;
	vector<float> time;
	lli start;
	float v;
	while (n--){
		cin >> start >> v;
		time.push_back((float)((destiny-start )/ v));
	}

	sort(time.begin(), time.end(), greater<float>());
	cout << fixed << setprecision(6) << (float)destiny / time[0] << '\n';
}

int main(){

	ifstream in("A-large.in");
	auto cinbuf = cin.rdbuf(in.rdbuf());
	ofstream on("A-large.txt");
	auto coutbuf = cout.rdbuf(on.rdbuf());


	int numCasos;
	cin >> numCasos;
	for (int i = 0; i < numCasos; ++i)
		resolve(i);

	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);

	return 0;
}