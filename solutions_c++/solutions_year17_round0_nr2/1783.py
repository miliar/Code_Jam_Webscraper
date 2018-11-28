#include <bits/stdc++.h>

#define cin fin
#define cout fout


using namespace std;

typedef long long ll;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int T, N;
string S;
ll answer;

string togglex(int x) {
    string retval = "";
    for (int i=0; i<x; i++)
        retval = retval + S[i];
    if (x < N) retval = retval+ (char)(S[x]-1);
    for (int i=x+1; i<N; i++)
        retval = retval + '9';

    for (int i=1; i<N; i++)
        if (retval[i] < retval[i-1]) retval = "0";
    return retval;
}

ll stringtonum(string snum) {
    ll retval = 0LL;
    for (int i=0; i<snum.size(); i++) {
        retval = retval*(10LL) + (ll)(snum[i]-'0');
    }
    return retval;
}

int main()
{
    cin >> T;

    for (int caseno=1; caseno<=T; caseno ++) {
        cin >> S;
        N = S.size();
        answer = 0LL;
        cout << "Case #" << caseno << ": ";
        for (int i=0; i<=N; i++) if (i == N || S[i] != '0') {
            ll candidate = stringtonum(togglex(i));
            answer = max(answer, candidate);
        }
        cout << answer << endl;
    }

    return 0;
}
