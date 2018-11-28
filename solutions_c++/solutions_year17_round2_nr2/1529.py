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
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;
	vector<pair<int,char>> colors;
	colors.push_back({ r,'R'});
	colors.push_back({ y, 'Y' });
	colors.push_back({ b, 'B'});
	sort(colors.begin(), colors.end(), greater<pair<int,char>>());
	if (colors[0].first - colors[1].first - colors[2].first > 0)
		cout << "IMPOSSIBLE\n";	
	else{
		bool iniFin = false;
		char ini = colors[0].second, ant = '0';
		while (colors[0].first > 0){
			if (colors[0].second == ant)
				swap(colors[0], colors[1]);
				
			else{
				if (ini != ant && !iniFin && colors[0].first == 1){
					int i = 0;
					while (i < colors.size() && colors[i].second != ini) ++i;
					if (i != 0)
						swap(colors[0], colors[i]);
				}
			}
			ant = colors[0].second;
			cout << ant;
			--colors[0].first;
			if (colors[0].second == ini && colors[0].first == 0) iniFin = true;
			
			sort(colors.begin(), colors.end(), greater<pair<int, char>>());
		}
		cout << '\n';
	}
}

int main(){

	ifstream in("B-small-attempt1.in");
	auto cinbuf = cin.rdbuf(in.rdbuf());
	ofstream on("B-small-attempt1.txt");
	auto coutbuf = cout.rdbuf(on.rdbuf());


	int numCasos;
	cin >> numCasos;
	for (int i = 0; i < numCasos; ++i)
		resolve(i);

	cin.rdbuf(cinbuf);
	cout.rdbuf(coutbuf);

	return 0;
}