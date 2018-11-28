#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

bool check (pair <int, int> a, pair <int, int> b) {
    if (a.first > b.first)
        swap (a, b);
    if (a.first == -1 || b.first == -1)
        return false;
    return b.first <= a.second;
}

int rec (vector < vector <int> >& g, set <int>& s, vector <int>& v) {
    if (v.size () == g.size())
        return v.size();

    int cur = v.size();
    int mx = cur;
    for (int i = 0; i < g[cur].size(); ++i)
        if (s.find(g[cur][i]) == s.end()) {
            s.insert(g[cur][i]);
            v.push_back(g[cur][i]);
            mx = max (mx, rec(g, s, v));
            s.erase(g[cur][i]);
            v.pop_back();
        }
    return mx;
}


 
bool try_kuhn (int v, int n, int k, vector < vector <int> > &g, vector <int>& mt, vector <char>& used) {
	if (used[v])  return false;
	used[v] = true;
	for (size_t i=0; i<g[v].size(); ++i) {
		int to = g[v][i];
		if (mt[to] == -1 || try_kuhn (mt[to], n, k, g, mt, used)) {
			mt[to] = v;
			return true;
		}
	}
	return false;
}

int main () {
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int t1 = 0; t1 < t; ++t1) {
        cout << "Case #" << t1 + 1 << ": ";

        int n, p;
        cin >> n >> p;
        vector <int> eng (n);
        for (int i = 0; i < n; ++i)
            cin >> eng[i];

        vector < vector < pair <int, int> > > amo (n, vector < pair <int, int> > (p));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < p; ++j) {
                int a;
                cin >> a;
                int l = -1;
                int r = -1;
                int x = 0;
                while (9 * x * eng[i] <= 10 * a) {
                    if (9 * x * eng[i] <= 10 * a && 10 * a <= 11 * x * eng[i]) {
                        if (l == -1)
                            l = x;
                        r = x;
                    }
                    ++x;
                }
                amo[i][j] = make_pair(l, r);
            }
        }
        if (n == 1) {
            int ans = 0;
            for (int i = 0; i < p; ++i)
                if (amo[0][i].first != -1)
                    ++ans;
            cout << ans;
        } else {
            /*vector < pair <int, int> > v;
            for (int i = 0; i < p; ++i)
                for (int j = 0; j < p; ++j)
                    v.push_back(make_pair (i, j));
            int mx = 0;
            for (int i = 0; i < (1 << v.size()); ++i) {
                bool good = true;
                vector < vector <bool> > used(n, vector <bool> (p, false));
                for (int j = 0; j < v.size(); ++j) {
                    if (i & (1 << j)) {
                        bool flag = check(amo[0][v[j].first], amo[1][v[j].second]);
                        if (!flag || used[0][v[j].first] || used[1][v[j].second]) {
                            good = false;
                            break;
                        } else {
                            used[0][v[j].first] = true;
                            used[1][v[j].second] = true;
                        }
                    }
                }
                if (!good)
                    continue;
                int count = 0;
                for (int j = 0; j < p; ++j)
                    if (used[0][j])
                        ++count;
                mx = max(mx, count);*/
                               vector < vector <int> > g(p, vector <int> ());
                for (int i = 0; i < p; ++i)
                    for (int j = 0; j < p; ++j)
                        if (check(amo[0][i], amo[1][j])) {
                           g[i].push_back(j);
                        }
		vector<int> mt;
		vector<char> used;
		mt.assign (p, -1);
		for (int v=0; v<p; ++v) {
			used.assign (p, false);
			try_kuhn (v, p, p, g, mt, used);
		}
		int ans = 0;
		for (int i=0; i<p; ++i)
			if (mt[i] != -1)
				++ans;
		cout << ans;
                /*set <int> s;
                vector <int> v;
                cout << rec(g, s, v);*/
        }
        cout << endl;
    }
}
