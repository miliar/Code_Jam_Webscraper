#include <iostream>
#include <string>
#include <set>
#include <queue>
using namespace std;
typedef long long ll;
#define f0(i,N) for (int i=0; i< N; i++) 
#define f1(i,N) for (int i=1; i<=N; i++) 
string S, R; int K;
struct E {
	string str; int steps;
	E() : str(""), steps(0) {};
	E(string S, int i) : str(S), steps(i) {};
};

string flip(string S, int pos, int K)
{
	f0(j, K)
	{
		if (S[pos+j] == '+') S[pos + j] = '-';
		else S[pos + j] = '+';
	}
	return S;
}

int main()
{
	ios::sync_with_stdio(false);
	int T; cin >> T;
	f1(t, T) {
		cin >> S >> K; R = string(S.length(), '+'); int f = 0;
		cout << "Case #" << t << ": "; 
		queue<E> q; set<string> st;
		q.push(E(S, 0)); st.insert(S);
		while (!q.empty()) {
			E temp = q.front(); q.pop();
			if (temp.str == R) {
				f = 1;
				cout << temp.steps << endl; break;
			}
			f0(i, S.length() - K + 1) {
				string strn = flip(temp.str, i, K);
				if (st.count(strn) == 0)
				{
					q.push(E(strn, temp.steps + 1));
					st.insert(strn);
				}
			}
		}
		if (f == 0) cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
