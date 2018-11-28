#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pll pair < ll, ll >
enum {R, O , Y, G, B, V};
int N, color[6];
int sol[1005];

bool bad(int col, int enemy1, int enemy2, int prev, int next)
{
	if(sol[next] == col || sol[prev] == col || sol[next] == enemy1 || sol[next] == enemy2
		|| sol[prev] == enemy1 || sol[prev] == enemy2) return true;

	return false;
}

int main()
{
	int T;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small.out", "w", stdout);
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out", "w", stdout);
	scanf("%d",&T);
	for(int tc = 1; tc <= T; tc++)
	{
		cin >> N; 
		memset(sol, -1, sizeof(sol));
		for(int i = 0; i < 6; i++)
			scanf("%d",&color[i]);
		bool imp = false;
		for(int i = 0; i < 6; i++)
			if(color[i] > N / 2) {imp = true; break;}

		if(color[R] + color[O] > N / 2) imp = true;
		if(color[R] + color[V] > N / 2) imp = true;
		if(color[Y] + color[G] > N / 2) imp = true;
		if(color[Y] + color[O] > N / 2) imp = true;
		if(color[B] + color[V] > N / 2) imp = true;
		if(color[B] + color[G] > N / 2) imp = true;

		printf("Case #%d: ",tc);
		if(imp) { printf("IMPOSSIBLE\n"); continue;}
		
		int k = 0;
		vector < pair < int, int > > arr;
		for(int i = 0; i < 6; i++) arr.push_back(make_pair(color[i], i));

		sort(arr.begin(), arr.end());
		reverse(arr.begin(), arr.end());
		for(int i = 0; i < 6; i++)
		{
			int col = arr[i].second;
			while(color[col] > 0)
			{
				//Finding a free space
				//cout << k << endl;
				while(sol[k] != -1) {k = (k + 1)%N;}
				//cout << col << "-----" << k << endl;
				//check my adj cells
				int prev = (k == 0) ? N - 1 : k - 1;
				int next = (k + 1)%N;

				if( col == R )
				{
					if(bad(col, O, V, prev, next)) k = (k + 1 ) % N;
					else { sol[k] = col; k = (k + 2) % N; color[col]--; }
				}
				else if( col == O)
				{
					if(bad(col, Y, R, prev, next)) k = (k + 1 ) % N;
					else {sol[k] = col; k = (k + 2)%N; color[col]--; }
				}
				else if( col == Y)
				{
					if(bad(col, O, G, prev, next)) k = (k + 1 ) % N;
					else {sol[k] = col; k = (k + 2)%N; color[col]--; }
				}
				else if( col == G)
				{
					if(bad(col, Y, B, prev, next)) k = (k + 1 ) % N;
					else {sol[k] = col; k = (k + 2)%N; color[col]--; }
				}
				else if( col == B)
				{
					if(bad(col, G, V, prev, next)) k = (k + 1 ) % N;
					else {sol[k] = col; k = (k + 2)%N; color[col]--; }
				}
				else
				{
					if(bad(col, R, B, prev, next)) k = (k + 1 ) % N;
					else {sol[k] = col; k = (k + 2)%N; color[col]--; }
				}
				if(color[col] == 0) k = (k == 0) ? N - 1 : k - 1;
			}
		}
		for(int i = 0; i < N; i++)
		{
			if(sol[i] == R) cout << "R";
			if(sol[i] == G) cout << "G";
			if(sol[i] == B) cout << "B";
			if(sol[i] == V) cout << "V";
			if(sol[i] == O) cout << "O";
			if(sol[i] == Y) cout << "Y";
		}
		printf("\n");
		//break;
	}
}