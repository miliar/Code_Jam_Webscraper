#include <bits/stdc++.h>

using namespace std;

#define D(x) x
#define REP(i,a,b) for (int i = (a); i < (b); ++i)
#define REPR(i,a,b) for (int i = (b) - 1; i >= (a); --i)
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<vector<int> > VII;

ifstream fin ("B-large.in");
ofstream fout ("B-large.out");

int main() {
    ios_base::sync_with_stdio(false);
    cout << setprecision(12) << fixed;

    int T; fin >> T;
    REP(t,1,T+1) {
        string s; fin >> s;
        int dec = 1;
        while (dec < s.length() && s[dec-1] <= s[dec])
            dec++;
        if (dec < s.length()) {
            s[dec-1]--;
            for (int j = dec; j < s.length(); ++j) {
                s[j] = '9';
            }
            while (dec - 2 >= 0 && s[dec-2] > s[dec-1]) {
                s[dec-2]--;
                s[dec-1] = '9';
                dec--;
            }
        }
        fout << "Case #" << t << ": ";
        if (s[0] != '0' || s.length() == 1)
            fout << s[0];
        REP(i,1,s.length())
            fout << s[i];
        fout << endl;
    }

	return 0;
}
