#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;


void solve(int _case) {
	cout << "Case #" << _case << ": ";
	// Regola: il colore col massimo numero deve essere inferiore alla somma degli altri

	// Quindi poi li assegnamo in ordine!
    auto cmp = [](pair<char, int> left, pair<char, int> right) { return left.second > right.second; };
    
    pair<char, int> letters[] = { { 'R', 0 }, {'O', 0}, {'Y', 0}, {'G', 0}, {'B', 0}, {'V', 0} };

    int tot;
    cin >> tot;
    for(auto &c : letters)
		cin >> c.second;
	
	sort(letters, letters + 6, cmp);
	
	if((tot - letters[0].second) < letters[0].second) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	// Uso un po' di memoria.
	int size = letters[0].second;
	char out[size][6] = {};
	
	for(int i = 0, j = 0; j < 6; ++j) {
		while(letters[j].second) {
			out[i % size][j] = letters[j].first;
			--letters[j].second;
			++i;
		}
	}
	
	for(char * c = out[0]; c != out[size]; ++c)
		if(*c)
			cout << *c;
	cout << endl;
}

int main() {
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i)
		solve(i);
}
