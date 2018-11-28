#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef vector<int> VI;
typedef vector<VI> VVI;

bool find_match(int i, const VVI& w, VI& mr, VI& mc, VI& seen) {
    for (int j = 0; j < w[i].size(); j++) {
        if (w[i][j] && !seen[j]) {
            seen[j] = true;
            if (mc[j] < 0 || find_match(mc[j], w, mr, mc, seen)) {
                mr[i] = j;
                mc[j] = i;
                return true;
            }
        }
    }
    return false;
}

int max_bipartite_matching(const VVI& w, VI& mr, VI& mc) {
    const int n = w.size(), m = w[0].size();
    mr = VI(n, -1);
    mc = VI(m, -1);
    int count = 0;
    for (int i = 0; i < n; i++) {
        VI seen(m, false);
        if (find_match(i, w, mr, mc, seen)) ++count;
    }
    return count;
}


void solve()
{
	int N, C, M;
	cin >> N >> C >> M;
	if(C != 2)
	{
		for(int i = 0; i < M; ++i)
		{
			int p, b;
			cin >> p >> b;
		}
		cout << "\n"; 
		return;
	}

	vector<vector<int>> wanted(2, vector<int>(N));
	vector<vector<int>> tickets(2);
	vector<int> total(2);
	for(int i = 0; i < M; ++i)
	{
		int p, b;
		cin >> p >> b;

		wanted[b-1][p-1]++;
		total[b-1]++;
		tickets[b-1].push_back(p-1);
	}
	
	int rounds = max(wanted[0][0] + wanted[1][0], max(total[0], total[1]));
	VVI cost(rounds, VI(rounds, 1));

	for(int i = 0; i < tickets[0].size(); ++i)
	for(int j = 0; j < tickets[1].size(); ++j)
		if(tickets[0][i] == tickets[1][j])
			cost[i][j] = 0;

	VI l, r;
	int proms = rounds - max_bipartite_matching(cost, l, r);

	/*cerr << endl;
	for(int i = 0; i < tickets[0].size(); ++i)
		cerr << i << " " << r[i] << endl;
	cerr << endl;*/

	cout << rounds << " " << proms << "\n";
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}
