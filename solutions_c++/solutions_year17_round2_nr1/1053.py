#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <unordered_map>
#include <climits>
#include <cassert>
#include <unordered_set>
#include <iostream>
#include <fstream>
#define fo(x) for(int i=0; i<x; i++)
#define ii pair<int,int>
#define ll unsigned long long

using namespace std;

int contacifre(unsigned long long l) {
	int c = 0;
	while(l>0) {
		l/=10;
		c++;
	}
	return c;
}

int main() {
	int t;
	ll d,n,k,s,numeratore,denominatore, ris, parziale, die;
	die = 1000000;
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	fscanf(in,"%d", &t);
	for(int j=0; j<t; j++) {
		fscanf(in,"%lld %lld", &d, &n);
		for(ll i=0; i<n; i++) {
			fscanf(in,"%lld %lld", &k, &s);
			numeratore = d*s*1000000;
			denominatore = d-k;
			parziale = numeratore/denominatore;
			if(i==0 || parziale<ris)
				ris = parziale;
			
		}
		fprintf(out,"Case #%d: %lld.", j+1,ris/die);
		if(ris%1000000 == 0)
			fprintf(out, "000000\n");
		else {
			for(int i=0; i<6-contacifre(ris%die); i++)
				fprintf(out,"0");
			fprintf(out,"%lld\n", ris%die);
		}
	}
	return 0;
}
