#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include<list>
#include <algorithm>
#include<string>
#include<stdlib.h>
#pragma warning(disable:4996)
using namespace std;
typedef struct {
	int val, high, low;
}aa;
aa a[3000000];
int compare(const void * a, const void * b)
{
	aa *A = (aa *)a;
	aa *B = (aa *)b;
	int mi, ma;
	mi = min(A->high - A->val, A->val - A->low);
	ma= max(A->high - A->val, A->val - A->low);
	int mi1, ma2;
	mi1 = min(B->high - B->val, B->val - B->low);
	ma2 = max(B->high - B->val, B->val - B->low);
	if (mi != mi1)
		return mi1 - mi;
	else if (ma2 != ma)
		return ma2 - ma;
	else
		return A->val - B->val;
}

int main() {
	int  t,i1=0;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A.txt", "w", stdout);
	cin >> t;
	while (t--) {
		i1++;
		int n, k, m, i;
		cin >> n >> k;
		m = 1;
		int nn = 1;
		i = 1;
		/*while (nn < n)
			nn = pow(2, i++);
		if (k > nn / 2){
			cout << "Case #" << i1 << ": " << 0 << " " << 0 << endl;
			continue; }
		if (k>nn/4) {
				cout << "Case #" << i1 << ": " << 1 << " " << 0 << endl;
				continue;
			}*/
		a[0].val = (n - 1) / 2;
		a[0].low = 0;
		a[0].high = n - 1;
		int o1 = 0;
		int o0 = 0;
		for (i = 0; i < m; i++)
		{
			if (a[i].val - a[i].low == 2)
				o1++,o0++;
			else if (a[i].val - a[i].low == 1)
				o0++;
			else if (a[i].val != a[i].low) {
				a[m].high = a[i].val - 1;
				a[m].low = a[i].low;
				a[m].val = (a[m].low + a[m].high) / 2;
				m++;
			}
			if (a[i].high - a[i].val == 2) 
				o1++,o0++;
			else if (a[i].high - a[i].val == 1)
				o0++;
			else if (a[i].val != a[i].high)
			{
				a[m].low = a[i].val + 1;
				a[m].high = a[i].high;
				a[m].val = (a[m].low + a[m].high) / 2;
				m++;
			}
		}
	if (k > m + o1){
			cout << "Case #" << i1 << ": " << 0 << " " << 0 << endl;
		continue;
	}
		else if (k > m) {
			cout << "Case #" << i1 << ": " << 1 << " " << 0 << endl;
			continue;
		}
		qsort(a, m, sizeof(aa), compare);
		int p=a[k-1].high-a[k-1].val;
		int q = a[k-1].val - a[k-1].low;
		cout << "Case #" << i1 << ": " << max(p,q) << " "<<min(p,q)<<endl;
	}
	return 0;
}
