#include <bits/stdc++.h>
using namespace std;

long long k, n;
vector<long long> gt[100], sl[100];

bool cmp(int x, int y) {
	return x>y;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);;
	int test;
	scanf("%d\n", &test);
	for(int dem = 1; dem <= test; dem++) {
		for(int i=0; i<100; i++) {
			gt[i].clear();
			sl[i].clear();
		}
		cin >> n >> k;
		gt[0].push_back(n);
		sl[0].push_back(1);
		bool found = false;
		for(int i=0; !found; i++) {
			long long sum = 0;
			for(int j=0; j<gt[i].size(); j++)
				sum += sl[i][j];
			if (sum < k) {
				k -= sum;
				for(int j=0; j<gt[i].size(); j++) {
					gt[i+1].push_back((gt[i][j]-1)/2);
					gt[i+1].push_back(gt[i][j]/2);
				}
				sort(gt[i+1].begin(), gt[i+1].end(), cmp);
				gt[i+1].resize(unique(gt[i+1].begin(), gt[i+1].end(), cmp) - gt[i+1].begin()+1);
				sl[i+1].resize(gt[i+1].size());
				for(int j=0; j<gt[i].size(); j++) {
					int pos = lower_bound(gt[i+1].begin(), gt[i+1].end(), gt[i][j]/2, cmp) - gt[i+1].begin();
					sl[i+1][pos] += sl[i][j];
					pos = lower_bound(gt[i+1].begin(), gt[i+1].end(), (gt[i][j]-1)/2, cmp) - gt[i+1].begin();
					sl[i+1][pos] += sl[i][j];
				}
			} else {				
				for(int j=0; j<gt[i].size() && !found; j++) {
					k -= min(k, sl[i][j]);
					if (k==0) {
						printf("Case #%d: %lld %lld\n", dem, gt[i][j]/2, (gt[i][j]-1)/2);
						found = true;
					}
				}
			}
		}
		// for(int i=0; i<3; i++) {
		// 	for(int j=0; j<gt[i].size(); j++)
		// 		printf("(%lld %lld) ", gt[i][j], sl[i][j]);
		// 	printf("\n");
		// }
	}
	fclose(stdin);
	fclose(stdout);
}