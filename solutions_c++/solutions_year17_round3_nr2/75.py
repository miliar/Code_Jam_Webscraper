#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stdio.h>
#include <set>
using namespace std;
int t, ac, aj, a, n, b;
typedef pair<int,int> pi;
vector<pair<pi, int> > act;
priority_queue<int, vector<int>, greater<int> > cpq, apq, fpq;
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("Blargeout.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		while (!cpq.empty()){
			cpq.pop();
		}
		while (!apq.empty()){
			apq.pop();
		}
		while (!fpq.empty()){
			fpq.pop();
		}
		act.clear();
		scanf("%d%d", &ac, &aj);
		int ct = 0, at = 0; //current time that c and a have
		for (int j = 0; j < ac; j++){
			scanf("%d%d", &a, &b);
			ct += b - a;
			act.push_back(make_pair(make_pair(a, b), 0));
		}
		for (int j = 0; j < aj; j++){
			scanf("%d%d", &a, &b);
			at += b - a;
			act.push_back(make_pair(make_pair(a, b), 1));
		}
		sort(act.begin(), act.end());
		int freetime = 0;
		for (int j = 0; j < act.size(); j++){
			if (j == act.size() - 1){
				if (act[j].second == 0 && act[0].second == 0){
					cpq.push(act[0].first.first + 1440 - act[j].first.second);
				} else if (act[j].second == 1 && act[0].second == 1){
					apq.push(act[0].first.first + 1440 - act[j].first.second);
				} else {
					fpq.push(act[0].first.first + 1440 - act[j].first.second);
				}
				continue;
			}
			if (act[j].second == 0 && act[j + 1].second == 0){
				cpq.push(act[j + 1].first.first - act[j].first.second);
			} else if (act[j].second == 1 && act[j + 1].second == 1){
				apq.push(act[j + 1].first.first - act[j].first.second);
			} else {
				fpq.push(act[j + 1].first.first - act[j].first.second);
			}
		}
		int answer = 0;
		while (!cpq.empty() && ct + cpq.top() <= 720){
			ct += cpq.top();
			cpq.pop();
		}
		while (!apq.empty() && at + apq.top() <= 720){
			at += apq.top();
			apq.pop();
		}
		while (!cpq.empty()){
			int v = cpq.top();
			v -= (720 - ct);
			ct += v;
			at += cpq.top() - v;
			cpq.pop();
			answer += 2;
		}
		while (!apq.empty()){
			int v = apq.top();
			v -= (720 - at);
			at += v;
			ct += apq.top() - v;
			apq.pop();
			answer += 2;
		}
		answer += fpq.size();
		printf("Case #%d: %d\n", i + 1, answer);
	}
}
