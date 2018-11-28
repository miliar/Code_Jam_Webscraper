#include <iostream>
#include <vector>

using namespace std;

vector<int> do_work(vector<int> vnum, int prev) {
	int top = vnum[0];
	vnum.erase(vnum.begin());
	vector<int> ret;
	ret.push_back(-1);
	if(top < prev) {
		return ret;
	}
	// yay base case
	if(vnum.size() == 0) {
		ret[0] = top;
		return ret;
	}

	// try top
	vector<int> temp = do_work(vnum, top);
	if(temp[0] != -1) {
		ret[0] = top;
		for(int j = 0; j<(int)temp.size(); ++j) {
			ret.push_back(temp[j]);
		}
		return ret;
	}


	// otherwise do 9s for days
	if(top - 1 < prev) {
		return ret;
	}
	ret[0] = top - 1;
	for(int i = 0; i<(int)vnum.size(); ++i) {
		ret.push_back(9);
	}
	return ret;
}

int main() {
	int n; cin >> n;
	for(int cs = 0; cs<n; ++cs) {
		long long num; cin >> num;
		vector<int> vnum;
		while(num) {
			vnum.insert(vnum.begin(), num % 10);
			num /= 10;
		}
		vnum.insert(vnum.begin(), 0);
		long long last_seen = 0;
		vector<int> temp = do_work(vnum, 0);
		for(int i = 0; i<(int)temp.size(); ++i) {
			last_seen *= 10;
			last_seen += temp[i];
		}
		cout << "Case #" << cs+1 << ": " << last_seen << endl;
	}
}
