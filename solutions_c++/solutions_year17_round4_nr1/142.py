#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

int N,P;

map<vector<int>, int> chk[4];

int go(vector<int> l, int x)
{
	x %= P;
	if (chk[x].count(l)) return chk[x][l];
	int &r = chk[x][l];

	for (int i=0;i<l.size();i++) if (l[i]){
		l[i]--;
		int u = go(l,x+i+1);
		if (x == 0) u++;
		if (r < u) r = u;
		l[i]++;
	}

	return r;
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		scanf ("%d %d",&N,&P);
		int C[4] = {0,};
		int ans = 0;
		for (int i=0;i<N;i++){
			int x; scanf ("%d",&x);
			C[x%P]++;
		}

		vector<int> can;
		for (int i=1;i<P;i++) can.push_back(C[i]);
		for (int i=0;i<P;i++) chk[i].clear();
		printf ("%d\n",go(can,0)+C[0]);
	}

	return 0;
}