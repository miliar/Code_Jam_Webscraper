#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vector<vi> vvi;

int N,P;
int dp[100][100][100][100];
int ct[4];
int cur[4];

int p2[][2] = {{1,0},{0,2}};
int p3[][3] = {{1,0,0},{0,0,3},{0,1,1},{0,3,0}};
int p4[][4] = {{1,0,0,0},{0,4,0,0},{0,2,1,0},{0,1,0,1},{0,0,2,0},{0,0,0,4},{0,0,1,2}};

bool next_cur(int s) {
	if (s >= P) return false;
	cur[s]++;
	if (cur[s] <= ct[s]) return true;
	cur[s] = 0;
	return next_cur(s+1);
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0);
	int T;
	cin >> T;
	for (int Tct=1; Tct<=T; Tct++) {
		cout << "Case #" << Tct << ": ";
		cin >> N >> P;
		
		for (int i=0; i<4; i++)
			ct[i] = 0;

		int g;
		for (int i=0; i<N; i++) {
			cin >> g;
			ct[g%P]++;
		}
	
		dp[0][0][0][0] = 0;
		for (int i=0; i<4; i++)
			cur[i] = 0;
		cur[0] = 1;

		do {
			if (P == 2) {
				dp[cur[0]][cur[1]][cur[2]][cur[3]] = 1;
				for (int i=0; i<2; i++) {
					if (p2[i][0] <= cur[0] && p2[i][1] <= cur[1])
						 dp[cur[0]][cur[1]][cur[2]][cur[3]] = max(dp[cur[0]][cur[1]][cur[2]][cur[3]],1+dp[cur[0]-p2[i][0]][cur[1]-p2[i][1]][cur[2]][cur[3]]);
				}
			} else if (P == 3) {
				dp[cur[0]][cur[1]][cur[2]][cur[3]] = 1;
				for (int i=0; i<4; i++) {
					if (p3[i][0] <= cur[0] && p3[i][1] <= cur[1] && p3[i][2] <= cur[2])
						 dp[cur[0]][cur[1]][cur[2]][cur[3]] = max(dp[cur[0]][cur[1]][cur[2]][cur[3]],1+dp[cur[0]-p3[i][0]][cur[1]-p3[i][1]][cur[2]-p3[i][2]][cur[3]]);
				}
			} else if (P == 4) {
				dp[cur[0]][cur[1]][cur[2]][cur[3]] = 1;
				for (int i=0; i<7; i++) {
					if (p4[i][0] <= cur[0] && p4[i][1] <= cur[1] && p4[i][2] <= cur[2] && p4[i][3] <= cur[3])
						 dp[cur[0]][cur[1]][cur[2]][cur[3]] = max(dp[cur[0]][cur[1]][cur[2]][cur[3]],1+dp[cur[0]-p4[i][0]][cur[1]-p4[i][1]][cur[2]-p4[i][2]][cur[3]-p4[i][3]]);
				}
			}
		} while (next_cur(0));

		cout << dp[ct[0]][ct[1]][ct[2]][ct[3]] << "\n";
	}
}

