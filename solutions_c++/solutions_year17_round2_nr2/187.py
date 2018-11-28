#include"stdio.h"
#include"algorithm"
#include"string"
#include"iostream"
using namespace std;
int t, T, N, C[6], Count;
vector<int> Err, Log;
string Answer;
char S[] = "ROYGBV";
bool check[6][6] = {	{ 0, 0, 1, 1, 1, 0 },
						{ 0, 0, 0, 0, 1, 0 },
						{ 1, 0, 0, 0, 1, 1 },
						{ 1, 0, 0, 0, 0, 0 },
						{ 1, 1, 1, 0, 0, 0 },
						{ 0, 0, 1, 0, 0, 0 }
						};
void mixed(int i) {
	int j = (i + 3) % 6;
	while (C[j] > 0) {
		//printf("%c%c", S[j], S[i]);
		Answer += S[j];
		Answer += S[i];
		Log.push_back(j);
		Log.push_back(i);
		C[j]--;
		Count++;
	}
}
void handle(int i) {
	//printf("%c", S[i]);
	Answer += S[i];
	Log.push_back(i);
	mixed(i);
	C[i]--;
	Count++;
}

int main() {
	//freopen("B-small-attempt1.in", "r", stdin);
	//freopen("B-small-attempt1.txt", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		Count = 0;
		Answer = "";
		Log.clear();
		scanf("%d", &N);
		for (int i = 0; i < 6; i++)
			scanf("%d", &C[i]);
		int Ans = 1;
		for (int i = 1; i < 6; i+=2) {
			if (C[i] == 0) continue;
			int j = (i + 3) % 6;
			if (C[i] > C[j] || (C[i] == C[j] && C[i] + C[j] != N)) {
				Ans = 0;
				break;
			}
			C[j] -= C[i];
		}
		if (Ans == 0) {
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}
		
		int maxC = 0, Max = 0;
		for (int i = 0; i < 6; i+=2)
			if (C[i] >= C[maxC]) {
				Max = C[i];
				maxC = i;
			}
		int Tot = C[0] + C[2] + C[4];
		if (Max * 2 > Tot) {
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}
		//printf("%d...%d\n", maxC, Max);
		printf("Case #%d: ", t);
		
		for (int x = 0; x < Max; x++) {
			handle(maxC);
			int first = 1;
			for (int i = 0; i < 6; i+=2) {
				if (i == maxC)
					continue;
				else if (x < Tot - Max - Max)
					handle(i);
				else if (first) {
					if (C[i] > 0) {
						handle(i);
						first = 0;
					}
				}
			}
		}
		for (int i = 1; i < 6; i+=2)
			if (C[i] > 0) mixed((i + 3) % 6);
		//printf("\n");
		cout << Answer << endl;
		if (Count != N) Err.push_back(t);
		for (int i = 0; i < Log.size(); i++) {
			int j = (i + 1) % Log.size();
			if (!check[Log[i]][Log[j]])
				Err.push_back(t);
		}
	}
	//for (int i = 0; i < Err.size(); i++)
	//	printf("%d ", Err[i]);
}
