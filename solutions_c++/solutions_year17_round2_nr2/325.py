#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define mp make_pair
#define pub push_back
#define x first
#define y second
#define all(a) a.begin(), a.end()
#define y1 dsfgsdfgsdfgsdfgsdfgsdfg
#define y0 asdfasdf3rcdt234d5c23xd234dx43
const int INF = (int)1e9 + 7;
const ll LINF = (ll)4e18 + 7;
const double pi = acos(-1.0);

const int p1 = 353251;
const int p2 = 239017;
const int mod = 1e9 + 7;
const int mod1 = 1e9 + 7;
const int mod2 = 1e9 + 9;

/*
const int MAX_MEM = 1e8;
int mpos = 0;
char mem[MAX_MEM];
void * operator new ( size_t n ) {
    char *res = mem + mpos;
    mpos += n;
    return (void *)res;
}

void operator delete ( void * ) { }
*/

int tt, n;
int r, o, y, g, b, v;
vector<pair<int, char> > t;
char a[1007];
bool was[1007];


const bool is_testing = 0;
int main() {
	srand('D' + 'E' + 'N' + 'I' + 'S' + 'S' + 'O' + 'N' + time(NULL));
	//mt19937 rnd(time(NULL));
	//ios_base::sync_with_stdio(0); cin.tie(0);
	if (is_testing) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	} else {
		//freopen("beads.in", "r", stdin);
		//freopen("beads.out", "w", stdout);
	}
	cin >> tt;
	for (int st = 1; st <= tt; st++){
		memset(was, 0, sizeof(was));
		cin >> n >> r >> o >> y >> g >> b >> v;
		t.clear();
		t.pub(mp(r, 'R'));
		t.pub(mp(y, 'Y'));
		t.pub(mp(b, 'B'));
		sort(all(t));
		reverse(all(t));
		int last = -1;
		for (int i = 0; i < n; i += 2){
			if (i == n - 1 || t[0].x == 0) break;
			last = i;
			was[i] = 1;
			a[i] = t[0].y;
			t[0].x--;
		}
		if (t[0].x != 0){
			cout << "Case #" << st << ": IMPOSSIBLE\n";
			continue;
		}
		last++;
		int f = 0;
		bool stop = 0;
		for (int i = last; i < n; i++){
			if (t[1 + f].x == 0) stop = 1;
			was[i] = 1;
			a[i] = t[1 + f].y;
			t[1 + f].x--;
			f = (f + 1) % 2;
		}
		if (stop){
			cout << "Case #" << st << ": IMPOSSIBLE\n";
			continue;
		}
		for (int i = 0; i < n; i++){
			if (!was[i]){
				if (t[1].x > 0){
					t[1].x--;
					a[i] = t[1].y;
				} else {
					t[2].x--;
					a[i] = t[2].y;
				}
			}
		}
		cout << "Case #" << st << ": ";
		for (int i = 0; i < n; i++) cout << a[i];
		cout << "\n";
	}
}
