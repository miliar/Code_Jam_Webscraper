#include <bits/stdc++.h>
using namespace std;

int cnt, n, p, peep[10];

int main() {
	int nq;
	cin >> nq;
	for(int q=0; q<nq; q++) {
		cin >> n >> p;
		for(int i=0; i<p; i++)
			peep[i] = 0;
		for(int i=0; i<n; i++) {
			int a; cin >> a;
			peep[a%p]++;
		}
		cnt = peep[0];
		if(p == 2) {
			if(peep[1]>0) cnt += (peep[1]-1)/2+1;
		}
		else if(p==3) {
			int mi = min(peep[1], peep[2]);
			cnt += mi;
			peep[1]-=mi;
			peep[2]-=mi;

			int mx = max(peep[1], peep[2]);
			if(mx>0) cnt += (mx-1)/3+1;
		}
		else if(p==4) {
			int mi = min(peep[1], peep[3]);
			cnt += mi;
			peep[1]-=mi;
			peep[3]-=mi;

			mi = peep[2]/2;
			cnt += mi;
			peep[2] -= 2*mi;

			int mx = max(peep[1], peep[3]);
			if(peep[2] == 1 && mx >= 2) {
				cnt += 1;
				mx-=2;
			}
			if(mx>0) cnt += (mx-1)/4+1;
		}
		printf("Case #%d: %d\n", q+1, cnt);
	}
	return 0;
}