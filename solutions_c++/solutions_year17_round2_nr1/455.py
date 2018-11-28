#include <stdio.h>
#include <algorithm>

using namespace std;

class p {
public:
	double x, v;
};

bool cmp(const p &i, const p &j) {
	return i.x<j.x;
}

p list[1001];
double d[1001];
int n;
double D;

int main() {
	FILE* in=fopen("A-Large.in","rt");
	FILE* out=fopen("Aout.txt","wt");
	int t;
	fscanf(in,"%d",&t);
	for(int tc=1;tc<=t;tc++) {
		fprintf(out,"Case #%d: ",tc);
		fscanf(in,"%lf %d",&D,&n);
		for(int i=0;i<n;i++)
			fscanf(in,"%lf %lf",&list[i].x,&list[i].v);
		sort(list,list+n,cmp);
		d[n-1]=(D-list[n-1].x)/list[n-1].v;
		for(int i=n-2;i>=0;i--)
			d[i]=max(d[i+1],(D-list[i].x)/list[i].v);
		fprintf(out,"%.10f\n",D/d[0]);
	}
	return 0;
}
