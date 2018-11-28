#include <iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

int testy,n,k,r,h,parz;
vector < pair <int, int> > nal;
double tab[2010][2];
double maxpref[2010];

void policzmaxpref(int n) {
	maxpref[0] = tab[0][parz];
	for (int i=1; i<n; ++i) {
		maxpref[i] = max(tab[i][parz], maxpref[i-1]);
	}
}

double calosc(int i) {
	double r = -nal[i].first, h = -nal[i].second;
	return M_PI*r*r + 2.0*M_PI*r*h;
}

double bok(int i) {
	double r = -nal[i].first, h = -nal[i].second;
	return 2.0*M_PI*r*h;
}

void doloz(int n){
	for (int i=1; i<n; ++i) {
		if (maxpref[i-1] == 0.0) { tab[i][(parz+1)%2] = 0.0; continue; }
		tab[i][(parz+1)%2] = maxpref[i-1] + bok(i);
	}
	++parz;
	parz = parz%2;
}

int main() {
	
	cin>>testy;
	
	for (int l=1; l<=testy; ++l) {
		cin>>n>>k;
		nal.clear();
		for (int i=0; i<n; ++i) {
			cin>>r>>h;
			nal.push_back(make_pair(-r,-h));
		}
		sort(nal.begin(), nal.end());
		for (int i=0; i<2010; ++i) {
			tab[i][0] = 0.0;
			tab[i][1] = 0.0;
			maxpref[i] = 0.0;
		}
		
		parz =0;
		
		for (int i=0; i<n; ++i) tab[i][0] = calosc(i);
		
		//for (int j=0; j<n; ++j) printf("%lf ", tab[j][parz]);
		//	printf("\n");
		
		for (int i=1; i<k; ++i) {
			policzmaxpref(n);
			doloz(n);
			//for (int j=0; j<n; ++j) printf("%lf ", tab[j][parz]);
			//printf("\n");
		}
		double odp = 0.0;
		for (int i=0; i<n; ++i) odp = max(odp, tab[i][parz]);
		printf("Case #%d: %.7lf\n", l, odp);
	}	

	return 0;
}
