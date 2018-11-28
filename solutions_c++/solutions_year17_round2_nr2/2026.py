#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, R, O, Y, G, B, V;
typedef pair<int, char> cPair;

/*
4
8 4 0 2 0 2 0
4 1 0 1 0 2 0
4 0 0 2 0 2 0
5 1 0 1 0 3 0

*/

string solve() {
	string result = "";
	priority_queue<cPair> pq;
	if(R > 0) pq.push(make_pair(R, 'R'));
	if(Y > 0) pq.push(make_pair(Y, 'Y'));
	if(B > 0) pq.push(make_pair(B, 'B'));

	int* tempVal;
	char* tempChar;
	bool tempSwitch = false;
	for(int i = 0; i < N; i++) {
		//cout << "fin: " << pq.size() << endl;
		//cout << result << endl;
		//cout << pq.top().first << ":" << pq.top().second << endl;
		if(i > 0) {
			if(pq.top().second == result[i-1] || (i == N-2 && pq.top().second != result[0])) {
				tempVal = new int;
				tempChar = new char;
				*tempVal = pq.top().first;
				*tempChar = pq.top().second;
				pq.pop();
				tempSwitch = true;
				//cout << "Switch" << endl;
			}
		}
		if(pq.size() == 0) { return "IMPOSSIBLE"; }

		result += pq.top().second;
		if(pq.top().first-1 > 0) { pq.push(make_pair(pq.top().first-1, pq.top().second)); }
		pq.pop();

		if(tempSwitch) {
			pq.push(make_pair(*tempVal, *tempChar));
			tempSwitch = false;
		}
	}

	//cout << "fin: " << pq.size() << endl;

	if(pq.size() > 0 || O > 0 || G > 0 || V > 0) { return "IMPOSSIBLE"; }
	if(result[0] == result[result.length()-1] ||
			result[result.length()-3] == result[result.length()-2]) { return "IMPOSSIBLE"; }
	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> N >> R >> O >> Y >> G >> B >> V;

		string result = solve();
		cout << "Case #" << (i+1) << ": " << result << endl;
	}
	return 0;
}
