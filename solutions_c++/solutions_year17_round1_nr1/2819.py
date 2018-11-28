#include <bits/stdc++.h>
#define MAX_N 100100
using namespace std;

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define iii pair<ii, int>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ep emplace_back
#define sz(a) (int) a.size()
#define cl(a) a.clear()

#define vi vector<int>
#define vii vector<ii>

#define LOWBIT(x) ( (x) & -(x) )

#define FOR(x,a,b) for (int x=a;x<=b;x++)
#define FOD(x,a,b) for (int x=a;x>=b;x--)
#define REP(x,a,b) for (int x=a;x<b;x++)
#define RED(x,a,b) for (int x=a;x>b;x--)

const int MAX = 1e5 + 10;
const int MAXN = 1e4 + 10;
const int MOD = 1e9 + 7;
const int inf = 1e9;
const double pi = acos(-1.0);
const double eps = 1e-6;

int dx[] = {0 , -1 , 0 , 1};
int dy[] = {1 , 0 , -1 , 0};

int test;
char a[30][30];
int R , C;
bool mark[30];

int main() {
	ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    cin >> test; int t = test;

    while (test--) {
        cout << "Case #" << t - test << ": ";
        memset(mark , false , sizeof(mark));

        cin >> R >> C;

        FOR(i , 1 , R) {
            string s;
            cin >> s;

            FOR(j , 1 , C) a[i][j] = s[j - 1];
        }

        FOR(i , 1 , R)
            FOR(j , 1 , C)
                if (a[i][j] != '?' && !mark[a[i][j] - 'A']) {
                    int S = 0;
                    mark[a[i][j] - 'A'] = true;
                    int UL , UR , DL , DR;
                    FOR(ul , i , R)
                        FOR(ur , j , C)
                            FOR(dl , 1 , i)
                                FOR(dr , 1 , j) {
                                    bool check = true;
                                    FOR(x , dl , ul)
                                        FOR(y , dr , ur)
                                            if (a[x][y] != a[i][j] && a[x][y] != '?') check = false;

                                    if (check) {
                                        if (S < (ul - dl + 1) * (ur - dr + 1)) {
                                            S = (ul - dl + 1) * (ur - dr + 1);
                                            UL = ul;
                                            UR = ur;
                                            DL = dl;
                                            DR = dr;
                                        }
                                    }
                                }

                    //cout << DL << ' ' << UL << ' ' << DR << ' ' << UR << endl;

                    FOR(x , DL , UL)
                        FOR(y , DR , UR) a[x][y] = a[i][j];
                }

        cout << endl;

        FOR(i , 1 , R) {
            FOR(j , 1 , C) cout << a[i][j];
            cout << endl;
        }
    }

	return 0;
}
