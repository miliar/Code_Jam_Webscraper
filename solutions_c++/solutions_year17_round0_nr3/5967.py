//Wrong
#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int T,N,K;
int len;
int arr[10000];

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	cin >> T;
	for (int now_case = 1;now_case <= T;++now_case) {
		cin >> N >> K;
		memset(arr, 0, sizeof(int)*2*K);
		len = 1, arr[1] = N;
		int k=1;
		while ((k <<= 1) < K);
		int num = 0;
		int i, j;
		for (i = 1;i <= k;++i) {
			for (j = (1 << i);j < (1 << (i + 1));j+=2) {
				int fa=arr[j >> 1]-1;
				arr[j] = fa / 2;
				arr[j + 1] = fa - arr[j];
				if (++num == K) break;
			}
			sort(arr + (1 << i), arr + (1 << (i + 1)), [](int &a, int &b) {return a > b;});
			if (num == K) break;
		}
		int ans=0;
		if (j < (1 << (i + 1))) {
			ans = arr[j >> 1];
		}
		else {
			ans = arr[(1 << i)];
		}
		cout << "Case #" << now_case << ": " << (ans / 2) << ' ' << (ans - ans / 2 - 1) << '\n';
	}
	return 0;
}