#include<stdio.h>
#include<assert.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;

const double EPS = 1e-8;
const double PI = acos(-1);

int solve();

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		solve();
	}
}

const int MX = 105;

int solve()
{
	int N, P;
	scanf("%d%d", &N, &P);

	int cnt[4] = {}, a, tot = 0;
	for(int i = 1; i <= N; i++){
		scanf("%d", &a);
		cnt[a%P]++;
		tot = (tot+a) % P;
	}
	int mx = 0;
	if(P == 4){
		for(int i = 0; i <= min(cnt[1]/2, cnt[2]); i++){
			for(int j = 0; j <= min(cnt[1], cnt[3]); j++){
				for(int k =0 ; k <= min(cnt[2], cnt[3]/2); k++){
					int tmp[4] = {};
					tmp[0] = cnt[0];
					tmp[1] = cnt[1] - i*2 - j;
					tmp[2] = cnt[2] - i - k;
					tmp[3] = cnt[3] - j - k*2;
					int ch = 1;
					for(int l = 1; l <= 3; l++){
						if( tmp[l] < 0 ) ch = 0;
					}
					if( ch ) mx = max(mx, tmp[0] + i+j+k + tmp[1]/4 + tmp[2]/2 + tmp[3]/4);
				}
			}
		}
	}
	else if( P == 3){
		for(int i = 0; i <= min(cnt[1], cnt[2]); i++){
			mx = max(mx, cnt[0] + i + (cnt[1]-i)/3 + (cnt[2]-i)/3);
		}
	}
	else mx = cnt[0] + cnt[1]/2;
	if( tot%P != 0 ) mx++;
	printf("%d\n", mx);
}
