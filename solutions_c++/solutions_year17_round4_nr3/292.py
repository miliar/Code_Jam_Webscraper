#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;

using namespace std;

int T;
int n, m;
string mas[55];
int was[55][55];
char bl[55][55];

void load () {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> mas[i];
	}
}               

bool checkUp (int i, int j) {
	for (int k = 1; ; k++) {
		if (i - k < 0)
			break;
		if (mas[i - k][j] == '#')
			break;
		if (mas[i - k][j] == '-' || mas[i - k][j] == '|')
			return false; 
	}
	for (int k = 1; ; k++) {
		if (i + k == n)
			break;
		if (mas[i + k][j] == '#')
			break;
		if (mas[i + k][j] == '-' || mas[i + k][j] == '|')
			return false; 
	}
	return true;
}


bool checkLeft (int i, int j) {
	for (int k = 1; ; k++) {
		if (j - k < 0)
			break;
		if (mas[i][j - k] == '#')
			break;
		if (mas[i][j - k] == '-' || mas[i][j - k] == '|')
			return false; 
	}
	for (int k = 1; ; k++) {
		if (j + k == m)
			break;
		if (mas[i][j + k] == '#')
			break;
		if (mas[i][j + k] == '-' || mas[i][j + k] == '|')
			return false; 
	}
	return true;
}

            
bool stupidCheck () {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (was[i][j] || mas[i][j] != '.') continue;
			bool r = false;
			for (int ni = i; ni < n && !r; ni++) {
				if (mas[ni][j] == '#')
					break;
				if (mas[ni][j] == '|' || mas[ni][j] == '-')
					r = true;
			}
			for (int nj = j; nj < m && !r; nj++) {
				if (mas[i][nj] == '#')
					break;
				if (mas[i][nj] == '|' || mas[i][nj] == '-')
					r = true;
			}                                       
			for (int ni = i; ni >= 0 && !r; ni--) {
				if (mas[ni][j] == '#')
					break;
				if (mas[ni][j] == '|')
					r = true;
				if (mas[ni][j] == '-' && !bl[ni][j])
					r = true;
			}

			for (int nj = j; nj >= 0 && !r; nj--) {
				if (mas[i][nj] == '#')
					break;
				if (mas[i][nj] == '-')
					r = true;
				if (mas[i][nj] == '|' && !bl[i][nj])
					r = true;
			}
			
			if (!r) {
				return false;
			}
		}           
	}
	return true;
}


bool addUp (int i, int j, int v) {
	for (int k = 1; ; k++) {
		if (i - k < 0)
			break;
		if (mas[i - k][j] == '#')
			break;
		was[i - k][j] += v;
	}
	for (int k = 1; ; k++) {
		if (i + k == n)
			break;
		if (mas[i + k][j] == '#')
			break;
		was[i + k][j] += v;
	}
	return true;
}


bool addLeft (int i, int j, int v) {
	for (int k = 1; ; k++) {
		if (j - k < 0)
			break;
		if (mas[i][j - k] == '#')
			break;		
		was[i][j - k] += v;
	}
	for (int k = 1; ; k++) {
		if (j + k == m)
			break;
		if (mas[i][j + k] == '#')
			break;
		was[i][j + k] += v; 
	}
	return true;
}


bool check () {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (mas[i][j] == '.' && !was[i][j]) {
				return false;
			}
		}
	}
	return true;
}

mt19937 rnd;

bool go (int i, int j) {
	if (i == n)
		return check ();
	if (j == m) {
		return go (i + 1, 0);
	}
	if (!stupidCheck ())
		return false;
	if (mas[i][j] != '|' && mas[i][j] != '-')
		return go (i, j + 1);
	/*if (rnd () & 1) {
	mas[i][j] = '|';
	if (checkUp (i, j)) {
		addUp (i, j, 1);
		bl[i][j] = 1;
		if (go (i, j + 1))
			return true;
		addUp (i, j, -1);
		bl[i][j] = 0;
	}
	mas[i][j] = '-';
	if (checkLeft (i, j)) {
		addLeft (i, j, 1);
		bl[i][j] = 1;
		if (go (i, j + 1))
			return true;
		addLeft (i, j, -1);
		bl[i][j] = 0;
	}
	}
	else*/ {
	
	mas[i][j] = '-';
	if (checkLeft (i, j)) {
		addLeft (i, j, 1);
		bl[i][j] = 1;
		if (go (i, j + 1))
			return true;
		addLeft (i, j, -1);
		bl[i][j] = 0;
	}
	mas[i][j] = '|';
	if (checkUp (i, j)) {
		addUp (i, j, 1);
		bl[i][j] = 1;
		if (go (i, j + 1))
			return true;
		addUp (i, j, -1);
		bl[i][j] = 0;
	}
	}
	return false;
}

string ans[] = {"IMPOSSIBLE", "POSSIBLE"};

void solve (int tc) {             
	memset (was, 0, sizeof (was));
	memset (bl, 0, sizeof (bl));
	bool r = go (0, 0);
	cout << "Case #" << tc << ": " << ans[(int) r] << endl;
	for (int i = 0; i < n && r; i++) {
		cout << mas[i] << endl;
	}
	clog << tc << endl;
}

void clear () {
}

int main () {
#ifdef LOCAL
    freopen ("file.in", "r", stdin);
    freopen ("file.out", "w", stdout);
#endif 
	
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		load ();
		solve (tc);
		clear ();
	}

    return 0;
}