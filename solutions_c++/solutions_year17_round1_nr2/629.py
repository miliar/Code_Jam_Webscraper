#include <stdio.h>
#include <algorithm>
#include <set>
#include <cmath>
using namespace std;
#define MAX 50
typedef pair<int,int> pii;

int n, p;
int r[MAX], q[MAX][MAX], lk[MAX][MAX], rk[MAX][MAX];
multiset<pii> s[MAX];

int main () {
  int test;
  scanf ("%d", &test);
  for (int t = 0; t < test; t++) {
	scanf ("%d %d", &n, &p);
	for (int i = 0; i < n; i++)
	  scanf ("%d", &r[i]);
	for (int i = 0; i < n; i++) {
	  for (int j = 0; j < p; j++)
		scanf ("%d", &q[i][j]);
	}
	for (int i = 0; i < n; i++)
	  s[i].clear();
	for (int i = 0; i < n; i++)
	  for (int j = 0; j < p; j++) {
		rk[i][j] = (10*q[i][j])/(r[i]*9);
		lk[i][j] = (int)ceil((10.0*q[i][j])/(r[i]*11));
		if (lk[i][j] <= rk[i][j])
		  s[i].insert(pii(lk[i][j], rk[i][j]));
	  }
	/*
	for (int i = 0; i < n; i++) {
	  for (int j = 0; j < p; j++)
		printf ("(%d,%d) ", lk[i][j], rk[i][j]);
	  printf ("\n");
	}
	*/
	int ret = 0;
	while (1) {
	  int lim = -1;
	  int empty_set = 0;
	  for (int i = 0; i < n; i++) {
		if (s[i].size() == 0) {
		  empty_set = 1;
		  break;
		}
		lim = max (lim, s[i].begin()->first);
	  }
	  if (empty_set)
		break;
	  //printf ("lim = %d\n", lim);
	  for (int i = 0; i < n; i++) {
		while ((s[i].size() > 0) &&
			   (s[i].begin()->second < lim)) {
		  //printf ("lim erase %d -> %d %d\n", i, s[i].begin()->first, s[i].begin()->second);
		  s[i].erase(s[i].begin());
		}
	  }
	  int valid = 1;
	  for (int i = 0; i < n; i++) {
		if (s[i].size() == 0) {
		  valid = 0;
		  break;
		}
		//printf ("i = %d -> %d %d\n", i, s[i].begin()->first, s[i].begin()->second);
		s[i].erase(s[i].begin());
	  }
	  if (valid)
		ret++;
	  else
		break;
	}
	printf ("Case #%d: %d\n", t + 1, ret);
  }
  return 0;
}
