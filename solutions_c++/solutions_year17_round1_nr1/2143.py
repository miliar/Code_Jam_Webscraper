#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define For(i,a,b)  for(int i=(a);i<(b);++i)
#define rep(i,n)    For(i,0,(n))

vector<string> solve()
{
	int R, C;
	cin >> R >> C;

	vector<string> cake(R);
	rep(i, R)
		cin >> cake[i];
	int cr;
	rep(i, R) {
		rep(j, C) {
			if(cake[i][j] != '?') {
				cr = i;
				goto cp;
			}
		}
	}
cp:
	cake[0] = cake[cr];

	char first;
	rep(i, R) {
		rep(j, C) {
			if(cake[i][j] != '?') {
				first = cake[i][j];
				goto next;
			}
		}
	}
next:

	vector<string> result(R, string(C, first));
	rep(i, R) {
		int before = 0;
		rep(j, C) {
			if(cake[i][j] != '?') {
				For(k, i, R) {
					For(l, before, C) {
						result[k][l] = cake[i][j];
					}
				}
				before = j + 1;
			}
		}
	}

	return result;
}

int main()
{
	int T;
	cin >> T;

	rep(i, T) {
		cout << "Case #" << (i + 1) << ":" << endl;
		for(const string &s : solve())
			cout << s << endl;
	}
}
