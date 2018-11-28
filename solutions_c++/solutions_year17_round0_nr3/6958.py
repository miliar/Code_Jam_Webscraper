#include <stdio.h>
#include <algorithm>
#include <queue>
#include <functional>
#include <vector>
using namespace std;

int T;//Test case;
int N, K;
int stall[1000003];
vector<pair<int, int>> ans;
vector <int> V;


int restroom(void) {
	vector<pair<int, int>>dat;
	sort(V.begin(), V.end());
	for (int j = 0; j < V.size() - 1; j++)
		dat.push_back(make_pair(V[j + 1] - V[j], V[j]));

	int x = 0;
	sort(dat.begin(), dat.end());
	int iden;
	int size = dat.size();
	iden = dat[size - 1].first;
	while (dat[size- 1-x].first == iden) {
		if (size == 1 + x)
			break;
		x++;	
	}
	if(dat[size-1-x].first!=iden)
	x = x - 1;
	if (size == 1)
		x = 0;

	int left, dif, mid;
	left = dat[dat.size() - 1 - x].second;
	dif = dat[dat.size() - 1 - x].first;
	mid = (left + left + dif) / 2;

	V.push_back(mid);
	stall[mid] = 1;


	return mid;

}

int main(void) {
	FILE *fp;
	fp = fopen("C-small-1-attempt1.in", "r");
	fscanf(fp, "%d", &T);
	
	for (int i = 0; i < T; i++) {
		//printf("!\n");
		int m = 0;
		int mxi = 0, min = 0;
		int ls = 0, rs = 0;
		fscanf(fp,"%d %d", &N, &K);
		stall[0] = 1;
		stall[N + 1] = 1;

		V.push_back(0);
		V.push_back(N + 1);
		for (int i = 0; i < K; i++) {
			m=restroom();

		}
		stall[m] = 0;
		while (stall[m - ls] == 0)
			ls++;
		while (stall[m + rs] == 0)
			rs++;
		if (ls <= rs) {
			mxi = rs;
			min = ls;
		}
		else {
			mxi = ls;
			min = rs;
		}
		ans.push_back(make_pair(mxi-1, min-1));
		
		for (int i = 0; i <= N+1; i++)
			stall[i] = 0;

		V.clear();
	}

	for (int i = 0; i < ans.size(); i++) {

		printf("Case #%d: %d %d\n", i + 1, ans[i].first, ans[i].second);
	}



	return 0;
}