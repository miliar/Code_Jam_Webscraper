#include <bits/stdc++.h>
using namespace std;

struct interval{
	int L, R, color;
};
bool operator <(interval a, interval b){
	return a.R < b.R;
}

int T, R, B, Ci[2];
interval L[205];

int dist(int x, int y){
	return (y - x + 1440) % 1440;
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d %d", &R, &B);
		int N = R + B;

		for(int i = 0; i < R; i++){
			scanf("%d %d", &L[i].L, &L[i].R);
			L[i].color = 0;
		}
		for(int i = 0; i < B; i++){
			scanf("%d %d", &L[R + i].L, &L[R + i].R);
			L[R + i].color = 1;
		}
		sort(L, L + N);

		/*for(int i = 0; i < N; i++)
			cout << L[i].L << ',' << L[i].R << ',' << L[i].color << ' ';
		cout << endl;*/

		Ci[0] = 0;
		Ci[1] = 0;

		int res = 0;
		for(int i = 0; i < N; i++){
			Ci[L[i].color] += L[i].R - L[i].L;

			if(L[(i + 1) % N].color == L[i].color)Ci[L[i].color] += dist(L[i].R, L[(i + 1) % N].L);
			else res++;
		}

		if((Ci[0] > 720) || (Ci[1] > 720)){
			int residue_color;
			if(Ci[0] > 720)residue_color = 0;
			else residue_color = 1;

			vector <int> v;
			for(int i = 0; i < N; i++){
				if((L[i].color == residue_color) && (L[(i + 1) % N].color == residue_color))
					v.push_back(dist(L[i].R, L[(i + 1) % N].L));
			}
			sort(v.rbegin(), v.rend());

			for(int x : v){
				Ci[residue_color] -= x;
				res += 2;

				if(Ci[residue_color] <= 720)break;
			}
		}

		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
