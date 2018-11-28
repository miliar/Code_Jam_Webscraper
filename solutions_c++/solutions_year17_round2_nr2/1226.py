#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>

using namespace std;

struct Node {
	int index;
	int num;
};

char colors[] = "ROYGBV";


void solve()
{

    string ans;
	string impossible = "IMPOSSIBLE";
	vector<vector<Node> > node(6, vector<Node>());
	int b[6];
	int n = 0;
	cin >> n;
	for (int i = 0; i < 6; i++) {
		cin >> b[i];
	}

	for (int i = 0; i < 3; i++) {
		int u = i * 2;
		int v = (u + 3) % 6;
		if (b[v] > b[u]) {
			cout << impossible;
			return;
		}
		if (b[v] == b[u]) {
            if (b[v] == 0) {
                continue;
            }
			if (b[v] + b[u] != n) {
				cout << impossible;
				return;
			} else {
				for (int i = 0; i < n / 2; i ++) {
					cout << colors[u] << colors[v];
				}
				return;
			}
		} else {
            if (b[u] + b[v] == n) {
                cout << impossible;
                return;
            }
			Node tmp;
			tmp.index = u;
			tmp.num = b[v];
			node[i].push_back(tmp);
			int left = b[u] - b[v] - 1;
			while (left--) {
				Node t;
				t.index= u;
				t.num = 0;
				node[i].push_back(t);
			}
		}
	}

	int pre = -1;

    for (int i = 0; i < 3; i++) {
        if (2 * node[i].size() > n) {
            cout <<impossible;
            return;
        }

    }



    vector<Node> aa;

    int k = 0;
    int ss = 1;
    int n1 = 0;
    for (int i = 0; i < 3; i++) {
    	for (int j = 0; j < 3; j++) {
    		if (node[j].size() > node[k].size()) {
    			k = j;
    		}
    	}
    	if (aa.size() == 0) {
    		aa = node[k];
    		n1 = aa.size();
    	} else {
    		for (int j = 0; j < node[k].size(); j++) {
    			aa.insert(aa.begin() + (ss-1)*2 + 1, node[k][j]);
    			ss++;
    			if (ss == n1+1) {
    				ss = 1;
    			}
    		}
    	}
    	node[k].clear();
    }
    for (int i = 0; i < aa.size(); i++) {
    	for (int j = 0; j < aa[i].num; j++) {
    		ans = ans + colors[aa[i].index];
    		ans = ans + colors[(aa[i].index + 3)%6];
    	}
    	ans = ans + colors[aa[i].index];
    }
    cout << ans;
}

int main()
{
	ios::sync_with_stdio(false);
	int cases;
	cin >> cases;
	for (int i = 1; i <= cases; i++) {
		cout <<"Case #" << i <<": ";
		solve();
		cout << endl;
	}
    return 0;
}
