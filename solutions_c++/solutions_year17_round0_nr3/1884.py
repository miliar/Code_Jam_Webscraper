#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;
#define LL long long

void generate(LL dis[2], LL num[2]){
	if (dis[0] & 1){
		LL t1 = num[0] * 2 + num[1];
		LL t2 = num[1];
		num[0] = t1, num[1] = t2;
	}else{
		LL t1 = num[0];
		LL t2 = num[0] + num[1] * 2;
		num[0] = t1, num[1] = t2;
	}
	dis[1] = dis[0] / 2 - 1;
	dis[0] = dis[0] / 2;
}

void show(LL x){
//	printf("show (%d)\n", x);
	if (x & 1){
		cout << x / 2 << " " << x / 2 << endl;
	}else{
		cout << x / 2 << " " << x / 2 - 1 << endl;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	LL dis[2], num[2];
	int T;
	LL n, k;
	cin >> T;
	for (int tt = 1; tt <= T;tt++){
		printf("Case #%d: ", tt);
		cin >> n >> k;
		num[0] = 1; num[1] = 0;
		dis[0] = n; dis[1] = n - 1;
		if (k == 1){
			show(n);
			continue;
		}
		for (LL i = 2;i <= k;i <<= 1){
			generate(dis, num);
//			printf("I : %d  dis = [%d, %d], num = [%d, %d]\n", i, dis[0], dis[1], num[0], num[1]);
			if (i * 2 > k){
				if (k - i + 1 > num[0]){
					show(dis[1]);
				}else{
					show(dis[0]);
				}
				break;
			}
		}
	}
	return 0;
}
