#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#define LL long long
#define eps 1e-8
#define mem(a,b) memset(a,b,sizeof(a))
#define zero(x) ((x > +eps) - (x < -eps))
#define MAX 110
#define INF 100000000
#define MAXEDGE 50010
using namespace std;
//freopen("", "r", stdin);
//freopen("", "w", stdout);
//printf("Case #%d: ", ii);

int n, p;
int num[MAX];
int cnt[4];

int main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int ii = 1; ii <= T; ii++){
		mem(cnt, 0);
		scanf("%d%d", &n, &p);
		int sum = 0;
		for (int i = 0; i < n; i++){
			scanf("%d", &num[i]);
			if (num[i] % p == 0){
				sum++;
				i--;
				n--;
			}
		}
		for (int i = 0; i < n; i++){
			cnt[num[i] % p] ++;
		}
		if (p == 2){
			sum += cnt[1] / 2;
			cnt[1] %= 2;
			sum += cnt[1];
		}
		else if (p == 3){
			int re = min(cnt[1], cnt[2]);
			sum += re;
			cnt[1] -= re;
			cnt[2] -= re;
			if (cnt[1]){
				sum += cnt[1] / 3;
				cnt[1] %= 3;
				sum += cnt[1] != 0 ? 1 : 0;
			}
			else{
				sum += cnt[2] / 3;
				cnt[2] %= 3;
				sum += cnt[2] != 0 ? 1 : 0;
			}
		}
		else if (p == 4){
			sum += cnt[2] / 2;
			cnt[2] %= 2;
			int re = min(cnt[1], cnt[3]);
			sum += re;
			cnt[1] -= re;
			cnt[3] -= re;
			if (cnt[1]){
				re = min(cnt[2], cnt[1] / 2);
				sum += re;
				cnt[2] -= re;
				cnt[1] -= 2 * re;
				sum += cnt[1] / 4;
				if (cnt[1] || cnt[2]){
					sum++;
				}
			}
			else if(cnt[3]){
				re = min(cnt[2], cnt[3] / 2);
				sum += re;
				cnt[2] -= re;
				cnt[3] -= 2 * re;
				sum += cnt[3] / 4;
				if (cnt[3] || cnt[2]){
					sum++;
				}
			}
		}
		printf("Case #%d: %d\n", ii,sum);
	}
	return 0;
}