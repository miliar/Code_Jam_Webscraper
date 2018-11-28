#include <bits/stdc++.h>

using namespace std;

#define debug(x) cout << "-----" << x << "-----" << endl
#define debugS(S, x) cout << "-" << S << "-" << "-----" << x << "-----" << endl
#define print(x) cout << x << endl
#define NMAX 1222
#define PI 3.141592653589793238462643383279502884197169399

typedef long long int lli;
typedef unsigned long long int llu;
typedef pair < long double, int > par;
typedef vector < vector < par > > grafo;

int main()
{
	int T, N, K, R, H, maior_R, maior_H, indice_do_maior;
	vector < par > P;

	scanf("%d", &T);
	

	int con = 1;
	while(con <= T)
	{
		P.clear();
		scanf("%d %d", &N, &K);

		maior_R = maior_H = indice_do_maior = -1;
		for(int i = 0; i < N; i++)
		{
			scanf("%d %d", &R, &H);
			
			long double area = 2.0 * PI * R * H; 
			//printf("area = %LF   R = %d\n", area, R);
			P.push_back(make_pair(area, R));

			/*if(P.R[i] > maior_R || (P.R[i] == maior_R && P.H[i] > maior_H))
			{
				maior_R = P.R[i];
				maior_H = P.H[i];
				indice_do_maior = i;
			}*/
		}

		sort(P.begin(), P.begin() + N);

		int indice_inicial;
		long double res = 0;
		priority_queue < par, vector < par >, greater < par > > Heap;
		for(int i = N - 1; i > N - K - 1; i--)
		{
			R = P[i].second;
			if(R > maior_R)
			{
				maior_R = R;
			}
			res += P[i].first;
			Heap.push(P[i]);
			//printf("area = %LF\n", P[i].first);
		}

		int ultimo = N - 1;
		long double A;

		for(int i = N - K - 1; i >= 0; i--)
		{
			A = P[i].first;
			R = P[i].second;
			if(R > maior_R && ((PI * R * R) - (PI * maior_R * maior_R) >= Heap.top().first - A))
			{
				//printf("R = %d %LF   %LF\n", R, A, Heap.top().first);
				//printf("%LF  %LF\n", (long double)(PI * R * R) - (PI * maior_R * maior_R),  (long double)Heap.top().first - A);
				maior_R = R;
				res -= Heap.top().first;
				res += A;
				Heap.pop();
				Heap.push(P[i]);
			}
		}

		res += PI * maior_R * maior_R;

		printf("Case #%d: %.9LF\n", con++, res);
	}



	return 0;
}