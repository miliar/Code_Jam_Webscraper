#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;

int N,C,M;

int go(int n, int *pos)
{
	int rem = 0, pr = 0;
	for (int i=N;i>=1;i--){
		if (pos[i] > n){
			rem += pos[i] - n;
		}
		else{
			int del = min(n-pos[i],rem);
			pr += del;
			rem -= del;
		}
	}

	if (rem > 0) return -1;
	return pr;
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		scanf ("%d %d %d",&N,&C,&M);

		int pos[1010] = {0,}, cus[1010] = {0,};
		int l = 0, r = M, a = M;
		while (M--){
			int a,b; scanf ("%d %d",&a,&b);
			pos[a]++; cus[b]++;
		}

		for (int i=1;i<=C;i++) l = max(l,cus[i]);

		while (l <= r){
			int m = (l + r) / 2;
			if (go(m,pos) != -1){
				a = m;
				r = m - 1;
			}
			else l = m + 1;
		}

		printf ("%d %d\n",a,go(a,pos));
	}

	return 0;
}