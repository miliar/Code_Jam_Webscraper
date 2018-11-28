#include <bits/stdc++.h>
using namespace std;

struct dato{
	double ini;
	double fin;
	double v;
	double t;
};

double sacoX(double x1, double v1, double x2, double v2){
	double ret = x1 * v2 - x2 * v1;
	ret /= (v2 - v1);
	return ret;
}

double sacoT(double x, double k, double v){
	return (x - k) / v;
}

int main (){
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("solSmall.out", "w", stdout);
	int t;
	scanf ("%d", &t);
	for (int caso = 1; caso <= t; caso++){
		double d;
		int n;
		scanf ("%lf %d", &d, &n);
		vector <pair<double, double> > h(n);
		for (int i = 0; i < n; i++)
			scanf ("%lf %lf", &h[i].first, &h[i].second);
		sort(h.begin(), h.end());
		vector<vector <dato> >secc (n);
		dato aux = {h[n - 1].first, d, h[n - 1].second, (d - h[n - 1].first) / h[n - 1].second};
		secc[n - 1].push_back(aux);
		for (int i = n - 2; i >= 0; i--){
			int j = secc[i + 1].size() - 1;
			//cout << h[i].second << " " << secc[i + 1][j].v << endl;
			while (j >= 0 && h[i].second < secc[i + 1][j].v)
				j--;
			//cout << j << endl;
			if (j >= 0){
				bool choque = false;
				while (j >= 0 && choque == false){
					double xAct = sacoX(h[i].first, h[i].second, secc[i + 1][j].ini, secc[i + 1][j].v);
					//cout << "X = " << xAct << endl;
					if (secc[i + 1][j].ini <= xAct && xAct <= secc[i + 1][j].fin){
						choque = true;
						double tAct = sacoT(xAct, h[i].first, h[i].second);
						//cout << xAct << " " << tAct << endl;
						aux.ini = h[i].first;
						aux.fin = xAct;
						aux.v = h[i].second;
						aux.t = tAct;
						secc[i].push_back(aux);
						aux.ini = xAct;
						aux.fin = secc[i + 1][j].fin;
						aux.v = secc[i + 1][j].v;
						aux.t = (aux.fin - aux.ini) / aux.v;
						secc[i].push_back(aux);
						j--;
						while(j >= 0){
							secc[i].push_back(secc[i + 1][j]);
							j--;
						}
					}else
						j--;
				}
				if (choque == false){
					aux.ini = h[i].first;
					aux.fin = d;
					aux.v = h[i].second;
					aux.t = (aux.fin - aux.ini) / aux.v;
					secc[i].push_back(aux);
				}
			}else{
				aux.ini = h[i].first;
				aux.fin = d;
				aux.v = h[i].second;
				aux.t = (aux.fin - aux.ini) / aux.v;
				secc[i].push_back(aux);
			}
		}
		double tTotal = 0.0;
		for (int i = 0; i < secc[0].size(); i++)
			tTotal += secc[0][i].t;
		printf ("Case #%d: %.6lf\n", caso, d / tTotal);
	}
	return 0;
}