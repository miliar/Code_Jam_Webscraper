#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int N,P;
int need[50];
int have[50][50];
int ptr[50];
int ct;

int main()
{
	int TM;
	cin >> TM;
	for (int T=1; T<=TM; T++) {
		cin >> N >> P;
		for (int i=0; i<N; i++) {
			cin >> need[i];
			ptr[i] = 0;
		}

		for (int i=0; i<N; i++) {
			for (int j=0; j<P; j++)
				cin >> have[i][j];
		
			sort(have[i],have[i]+P);
		}

		ct=0;
		while (true) {
			int mins=0,maxs=10000000;
			for (int i=0; i<N; i++) {
				while (ptr[i] < P && ceil(have[i][ptr[i]]/1.1/need[i]) > floor(have[i][ptr[i]]/0.9/need[i]))
					ptr[i]++;

				int a = ceil(have[i][ptr[i]]/1.1/need[i]);
				int b = floor(have[i][ptr[i]]/0.9/need[i]);				

				if (ptr[i] >= P) goto end;
				mins = max(a,mins);
				maxs = min(b,maxs);
			}

			if (maxs >= mins && maxs > 0) {
				ct++;
				for (int i=0; i<N; i++)
					ptr[i]++;
			} else {
				int mins=10000000,mini=0;
				for (int i=0; i<N; i++) {
					int x = ceil(have[i][ptr[i]]/1.1/need[i]);
					if (x < mins) {
						mins = x;
						mini = i;
					}
				}
				ptr[mini]++;
			}
		}

		end:;
		cout << "Case #" << T << ": " << ct << "\n";
	}
}
