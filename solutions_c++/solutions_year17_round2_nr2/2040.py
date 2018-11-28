//Irvin Gonzalez


#include <iostream>
#include <string>
#include <vector>
using namespace std;
void solve() {
	int n;
	cin >> n;
	int pony[6];
	for(int i = 0; i < 6; ++i) {
		cin >> pony[i]; }
	int range[6][6];
	for(int i = 0; i < 6; ++i) for(int j = 0; j < 6; ++j) range[i][j] = 0;
	range[0][2] = 1;
	range[0][3] = 1;
	range[0][4] = 1;
	range[1][5] = 1;
	range[2][4] = 1;
	range[2][5] = 1;
	range[2][0] = 1;
	range[3][0] = 1;
	range[4][0] = 1;
	range[4][1] = 1;
	range[4][2] = 1;
	range[5][2] = 1;

	vector<int> order;
	int cur = -1;
	int grtval = 0;
	for(int i = 0; i < 6; ++i) {
		if(pony[i] > grtval) {
			cur = i;
			grtval = pony[i]; } }
	pony[cur]--;
	n--;
	order.push_back(cur);
	while(n != 0) {
		int grt = -1;
		grtval = 0;
		for(int i = 0; i < 6; ++i) {
			if(range[cur][i] == 1 && pony[i] > 0) {
				if((i%2 == 1) && (grt%2 == 0)) {
					//cout << i << " " << grt << endl;
					grt = i;
					grtval = pony[i]; 
				}
				else if(pony[i] > grtval) {
					if(i%2 == 0 && grt%2 == 1) {}
					else{
						grt = i;
						grtval = pony[i]; } }
			        else if(pony[i] == grtval) {
					if((range[order[0]][i] == 0) && (range[order[0]][grt] == 1)) {
						if(i%2 == 0 && grt%2 == 1) {}
						else{
							grt = i; 
							grtval = pony[i]; } }
					else if((range[order[0]][i] == 1) && (range[order[0]][grt] == 1)) {
						if((i%2 == 1) && (grt%2 == 0)) {
							grt = i;
							grtval = pony[i]; } } }			
			}
		}
		if(grt == -1) {
			cout << "IMPOSSIBLE";
			return; }
		cur = grt;
		pony[cur]--;
		n--;
		order.push_back(cur); }
	if(range[order[0]][order[order.size() - 1]] == 0) {
		cout << "IMPOSSIBLE";
		return; }
	for(int i = 0; i < order.size(); ++i) {
		if(order[i] == 0)
			cout << "R";
		if(order[i] == 1)
			cout << "O";
		if(order[i] == 2)
			cout << "Y";
		if(order[i] == 3)
			cout << "G";
		if(order[i] == 4)
			cout << "B";
		if(order[i] == 5)
			cout << "V";
	}


		


}
int main() {

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl; }
	return 0;
}
