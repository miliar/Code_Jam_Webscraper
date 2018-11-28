#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int t;
int a[101][101];
int n, q, x, y;
vector < int > e, s;
vector < pair < int, int > > query;
int u, v;
double d[101], len[101][101];
bool fl[101];
//~ vector < int > topsort;
vector < double > ans;


//~ void topsort_run(int u)
//~ {
	//~ fl[u] = 1;	
	//~ for (int i = 0; i < n; i++) {
		//~ if (a[u][i] > -1 && fl[i] == 0)
			//~ topsort_run(i);
	//~ }	
	//~ topsort.push_back(u);
//~ }


int main()
{
	freopen("c.in", "r", stdin);
	freopen("c_large.out", "w", stdout);
	
	cin >> t;
	
	for (int l = 0; l < t; l++) {
		cin >> n >> q;
		e.clear();
		s.clear();
		query.clear();
		
		for (int i = 0; i < n; i++) {
			cin >> x >> y;
			e.push_back(x);
			s.push_back(y);
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> x;
				a[i][j] = x;
			}
		}		
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				len[i][j] = a[i][j];
				if (a[i][j] == -1)
					len[i][j] = 1e14;
			}
		}
		
		for (int k = 0; k < n; k++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					len[i][j] = min(len[i][j], len[i][k] + len[k][j]);
					
					
		//~ for (int i = 0; i < n; i++) {
			//~ for (int j = 0; j < n; j++) {
				//~ cout << len[i][j] << ' ';
			//~ }
			//~ cout << endl;
		//~ }
			
		///////////////////////////
		
		//////////////////////////
		
		ans.clear();
		
		for (int i = 0; i < q; i++) {
			cin >> u >> v;
			u--;
			v--;
			
			//~ for (int i = 0; i < n; i++)
				//~ fl[i] = 0;
				//~ 
			//~ topsort.clear();
			//~ topsort_run(u);
			//~ reverse(topsort.begin(), topsort.end());
			//~ 
			//~ for (int i = 0; i < n; i++)
				//~ cout << topsort[i] + 1 << ' ';
			//~ cout << endl;
			
			////////////////
			
			//~ int ui = 0;
			//~ while (ui < n && topsort[ui] != u)
				//~ ui++;
				//~ 
			//~ int vi = 0;
			//~ while (vi < n && topsort[vi] != v)
				//~ vi++;
				
			//~ cout << ui << ' ' << vi << endl;
				
			for (int j = 0; j < n; j++)
				d[j] = 1e14;
			d[u] = 0;
			
			for (int k = 0; k < n; k++)
				for (int j = 0; j < n; j++) {
					for (int z = 0; z < n; z++) {
						if (e[z] >= len[z][j])
							d[j] = min(d[j], d[z] + len[z][j] * 1.0 / s[z]);
					}
				}
			
			ans.push_back(d[v]);
		}
		
		cout << "Case #" << l + 1 << ": ";
		for (int i = 0; i < q - 1; i++)
			printf("%.6lf ", ans[i]);
		printf("%.6lf", ans[q - 1]);
		cout << endl;		
	}
	
	
	return 0;
}
