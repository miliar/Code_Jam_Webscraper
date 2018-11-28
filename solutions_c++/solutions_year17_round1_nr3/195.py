#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>

#define D(x) 

using namespace std;

struct state {
	int Hd, Hk, Ad, Ak;
	int turn;

	state(int Hd, int Hk, int Ad, int Ak) {
		this->Hd = min(100, max(0, Hd));
		this->Hk = min(100, max(0, Hk));
		this->Ad = min(100, max(0, Ad));
		this->Ak = min(100, max(0, Ak));
	}

	int id() {
		return Hd + 101*(Hk + 101*(Ad + 101*(Ak)));
	}
};

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
	os << "[";
	for (int i = 0; i < vec.size(); i++) {
		if (i > 0) os << ", ";
		os << vec[i];
	}
	os << "]";
	return os;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
    	int Hd, Ad, Hk, Ak, B, D;

    	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

    	vector<state> current;
    	current.push_back(state(Hd, Hk, Ad, Ak));
    	bool done = false;
    	int turn = 0;

    	vector<bool> visited(101*101*101*101);

    	while (!current.empty()) {
    		vector<state> next;
    		D(cerr << "turn " << turn << endl);

    		for (state& st : current) {
    			int id = st.id();
    			D(cerr << "  Hd=" << st.Hd << " Hk=" << st.Hk << " Ad=" << st.Ad << " Ak=" << st.Ak << endl);
    			if (visited[id]) { D(cerr << "    skipping" << endl); continue; }
    			visited[id] = true;

    			if (st.Hk <= 0) {
    				done = true;
    				break;
    			}
    			if (st.Hd <= 0) {
    				continue;
    			}

    			// Attack
    			next.push_back(state(st.Hd - st.Ak, st.Hk - st.Ad, st.Ad, st.Ak));
    			// Buff
    			next.push_back(state(st.Hd - st.Ak, st.Hk, st.Ad + B, st.Ak));
    			// Cure
    			next.push_back(state(Hd - st.Ak, st.Hk, st.Ad, st.Ak));
    			// Debuff
    			next.push_back(state(st.Hd - max(st.Ak-D,0), st.Hk, st.Ad, st.Ak-D));
    		}
    		if (done) break;

    		turn++;
    		swap(current, next);
    	}

        cout << "Case #" << testCase << ": ";
        if (done) {
        	cout << turn << endl;
        } else {
        	cout << "IMPOSSIBLE" << endl;
        }
    }
}
