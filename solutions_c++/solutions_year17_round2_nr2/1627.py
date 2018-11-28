#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<stdio.h>
#include<string.h>
#include<string>
#include<set>
#include<stdlib.h>
#include<bitset>
#include<algorithm>
using namespace std;
#define ll long long
string reff = "RYB";
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // !ONLINE_JUDGE
	//R, O, Y, G, B, and V.
	//O = G = V = 0. 
	int t,n;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int color[3] = { 0 };
		scanf("%d", &n);
		int sum = 0, mx = 0, idx = -1;
		priority_queue<pair<int, int> >pq;
		for (int i = 0, x; i < 6; ++i) {
			scanf("%d", &x);
			if (i % 2 == 0) {
				color[i / 2] = x;
				if(x>0)
					pq.push(make_pair(x, i / 2));
				if (x > mx) {
					mx = x;
					idx = i / 2;
				}
				sum += x;
			}
		}
		char mxR = reff[idx];
		bool ans = true;
		string st = "";
		int last = -1;
		if (sum - mx < mx) {
			ans = false;
		}
		else {
			while (!pq.empty()) {
				pair<int, int> a = pq.top();
				pq.pop();
				if (!pq.empty()) {
					pair<int, int> b = pq.top();
					pq.pop();
					if (!pq.empty() && a.first == b.first && a.first == pq.top().first) {
						pair<int, int> c = pq.top();
						for (int i = 0; i < a.first; ++i) {
							st += mxR;
							for (int j = 0; j < 3; ++j) {
								if (j != idx)
									st += reff[j];
							}
						}
						break;
					}
					else {
						a.first--;
						b.first--;

						if (a.second == idx) {
							st += reff[idx];
							st += reff[b.second];
							last = b.second;
						}
						else if (b.second == idx) {
							st += reff[idx];
							st += reff[a.second];
							last = a.second;
						}
						else if (a.second == last) {
							st += reff[b.second];
							st += reff[a.second];
						}
						else {
							st += reff[a.second];
							st += reff[b.second];
							last = b.second;
						}

						if (a.first > 0)
							pq.push(a);
						if (b.first > 0)
							pq.push(b);
					}
				}
				else
					st += reff[a.second];
			}
		}
		if (ans) {
			printf("Case #%d: ",i);
			for (int i = 0; i < st.length(); ++i)
				printf("%c", st[i]);
			printf("\n");
		}
		else
			printf("Case #%d: IMPOSSIBLE\n", i);
	}
}