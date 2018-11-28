#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cstring>
#include <vector>
using namespace std;
#define ll long long
typedef pair<ll,ll> pi;
ll t, n, c, m, p, b;
vector<ll> v[1005];
ll arr[1005];
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("blargeout.txt", "w", stdout);
	scanf("%lld", &t);
	for (int i = 0; i < t; i++){
		scanf("%lld%lld%lld", &n, &c, &m);
		memset(arr, 0, sizeof(arr));
		for (int j = 0; j < n; j++){
			v[j].clear();
		}
		ll answer = 0;
		for (int j = 0; j < m; j++){
			scanf("%lld%lld", &p, &b);
			v[p - 1].push_back(b - 1);
			arr[b - 1] += 1;
			answer = max(answer, arr[b - 1]);
		}
		ll cursum = 0;
		ll promoted = 0;
		for (int j = 0; j < n; j++){
			cursum += (long long)v[j].size();
			if (cursum > answer*(j + 1)){
				if (cursum % (j + 1) == 0){
					answer = max(answer, cursum/(j + 1));
				} else {
					answer = max(answer, (cursum + j + 1)/(j + 1));
				}
			}
		}
		for (int j = 0; j < n; j++){
			if ((long long)v[j].size() > answer){
				promoted += (long long)v[j].size() - answer;
			}
		}
		printf("Case #%d: %lld %lld\n", i + 1, answer, promoted);
		
	}
}
