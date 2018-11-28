	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int X = 6;
const int N = 2002;

int mp[N];
char ch[X] = {'R', 'V', 'Y', 'O', 'B', 'G'};
int g[X][X];
string res;

void add(int u, int v, int w) { g[u][v] = g[v][u] = w; }

void dfs(int v)
{
	for(int i = 0; i < X; i++)
		if(g[v][i])
		{
			g[v][i]--;
			g[i][v]--;
			dfs(i);
			res += ch[v];
		}
}

int main()
{
	int _t = in();
	mp['G'] = 5;
	mp['R'] = 0;
	mp['V'] = 1;
	mp['Y'] = 2;
	mp['O'] = 3;
	mp['B'] = 4;
	for(int _i = 1; _i <= _t; _i++)
	{
		printf("Case #%d: ", _i);
		for(int i = 0; i < X; i++)
			for(int j = 0; j < X; j++)
				g[i][j] = 0;
		res.clear();
		int R, O, Y, G, B, V, n;
		scanf("%d%d%d%d%d%d%d", &n, &R, &O, &Y, &G, &B, &V);

		add(0, 5, 2 * G);
		add(1, 2, 2 * V);
		add(3, 4, 2 * O);

		R -= G;
		Y -= V;
		B -= O;
		bool ok = true;
//		cerr << R << " " << Y << " " << B << endl;
		if(R < 0 || Y < 0 || B < 0)
		{
			ok = false;
//			cerr << "1!! ";
		}

		add(0, 2, Y + R - B);
		add(2, 4, Y + B - R);
		add(4, 0, B + R - Y);

		int st = 0;
		for(int i = 0; i < X; i++)
		{
			int d = 0;
			for(int j = 0; j < X; j++)
			{
				d += g[i][j];
				if(g[i][j] < 0)
					ok = false;
			}
			if(d % 2)
			{
				ok = false;
//				cerr << "2!!! ";
			}
			if(d)
				st = i;
		}

		if(!ok)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}

/*		for(int i = 0; i < X; i++, cerr << endl)
			for(int j = 0; j < X; j++)
				cerr << g[i][j] << " ";
*/
		dfs(st);
		
//		cerr << " => " << res << endl;
		if(res.size() == n)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE\n";
	}
}

/*
 * if(concat.size() == 0)
		{
			if(check(R + 1, B, Y, 0, 0))
			{
				res = tmp;
				ok = true;
			}
			if(check(R, B + 1, Y, 1, 1))
			{
				res = tmp;
				ok = true;
			}
			if(check(R, B, Y + 1, 2, 2))
			{
				res = tmp;
				ok = true;
			}
		}
		else
		{
			
		}
		int grs = gr.size();
		int vys = vy.size();
		int obs = ob.size();
		if(grs && !(vys + obs))
		{
			if(check(R + 2, B, Y, 0, 0))
			{
				tmp.pop_back();
				res = tmp + gr;
				ok = true;
			}
		}
		if(obs && !(vys + grs))
		{
			if(check(R, B + 2, Y, 1, 1))
			{
				tmp.pop_back();
				res = tmp + ob;
				ok = true;
			}
		}
		if(vys && !(obs + grs))
		{
			if(check(R, B, Y + 2, 2, 2))
			{
				tmp.pop_back();
				res = tmp + concat;
				ok = true;
			}
		}
		*/
