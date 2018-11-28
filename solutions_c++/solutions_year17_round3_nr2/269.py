#include <algorithm>
#include <cstdio>
using namespace std;

struct gap{
	int start, end;
	int len;
};

bool compare(gap A, gap B){
	return A.len < B.len;
}
bool check;
int T, AC, AJ;
int X, Y;
int time[1440];
int remainC, remainJ, numC, numJ, temp, last, ans;
gap gapC[1440], gapJ[1440];
int main (){
	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d", &AC, &AJ);
		if (AC + AJ == 0){
			printf("Case #%d: 2\n", i);
		} else {
			remainC = 720;
			remainJ = 720;
			for (int j = 0; j < 1440; j++)
				time[j] = 0;
			for (int j = 0; j < AC; j++){
				scanf("%d %d", &X, &Y);
				for (int k = X; k < Y; k++)
					time[k] = 2;
				remainJ -= Y - X;
			}
			for (int j = 0; j < AJ; j++){
				scanf("%d %d", &X, &Y);
				for (int k = X; k < Y; k++)
					time[k] = 1;
				remainC -= Y - X;
			}
			
			temp = 0;
			while (time[temp] == 0)
				temp++;
			for (int j = 0; j < 1440 - temp; j++)
				time[j] = time[j + temp];
			for (int j = 1440 - temp; j < 1440; j++)
				time[j] = 0;
			
			last = 1439;
			while (time[last] == 0)
				last--;
			
			check = false;
			numC = 0;
			numJ = 0;
			for (int j = 0; j < 1440; j++){
				if (time[j] == 2){
					check = false;
				} else if (time[j] == 1){
					if (check){
						if (j - temp - 1 > 0){
							gapC[numC].start = temp + 1;
							gapC[numC].end = j - 1;
							gapC[numC].len = j - temp - 1;
							numC++;
						}
					}
					check = true;
					temp = j;
				}
			}
			if (time[0] == 1 && time[last] == 1 && last != 1439){
				gapC[numC].start = last + 1;
				gapC[numC].end = 1439;
				gapC[numC].len = 1439 - last;
				numC++;
			}
			
			for (int j = 0; j < 1440; j++){
				if (time[j] == 1){
					check = false;
				} else if (time[j] == 2){
					if (check){
						if (j - temp - 1 > 0){
							gapJ[numJ].start = temp + 1;
							gapJ[numJ].end = j - 1;
							gapJ[numJ].len = j - temp - 1;
							numJ++;
						}
					}
					check = true;
					temp = j;
				}
			}
			if (time[0] == 2 && time[last] == 2 && last != 1439){
				gapJ[numJ].start = last + 1;
				gapJ[numJ].end = 1439;
				gapJ[numJ].len = 1439 - last;
				numJ++;
			}
			
			sort(gapC, gapC + numC, compare);
			sort(gapJ, gapJ + numJ, compare);
			
			temp = 0;
			while (remainC >= gapC[temp].len && temp < numC){
				for (int j = gapC[temp].start; j <= gapC[temp].end; j++)
					time[j] = 1;
				remainC -= gapC[temp].len;
				temp++;
			}
			
			temp = 0;
			while (remainJ >= gapJ[temp].len && temp < numJ){
				for (int j = gapJ[temp].start; j <= gapJ[temp].end; j++)
					time[j] = 2;
				remainJ -= gapJ[temp].len;
				temp++;
			}
			
			for (int j = 1; j < 1440; j++){
				if (time[j] == 0 && time[j - 1] == 1){
					if (remainC > 0){
						time[j] = 1;
						remainC--;
					} else {
						time[j] = 2;
						remainJ--;
					}
				}
				if (time[j] == 0 && time[j - 1] == 2){
					if (remainJ > 0){
						time[j] = 2;
						remainJ--;
					} else {
						time[j] = 1;
						remainC--;
					}
				}
			}
			
			ans = 0;
			for (int j = 1; j < 1440; j++){
				if (time[j - 1] != time[j])
					ans++;
			}
			if (time[0] != time[1439])
				ans++;
			printf("Case #%d: %d\n", i, ans);
		}
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
