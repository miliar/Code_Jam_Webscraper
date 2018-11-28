#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <queue>
#define rep(i,a,b) for (int i = (a); i <= (b); ++i) 
#define rep2(i,a,b) for (int i = (a); i >= (b); --i)
const int maxn = 110;
typedef long long ll;
ll last, tot, t, n, x, a[maxn];
using namespace std;
void work(ll k){
	while (k != 0){
		a[++tot] = k  % 10;
		k /= 10;
	}
}
int main()
{
	//freopen("111.txt","w",stdout);
	int i, j;
	cin >> t;
	bool flag;
	rep (s,1,t){
		cin >> x;
		tot = 0;
		memset(a,0,sizeof(a));
		work(x);
		
		flag = true;
		rep (k,1,tot-1){
			if (a[k]<a[k+1]){
				flag = false;
				break;
			}
		}
		if (flag){
			//cout << x << endl;
			printf("Case #%d: %d\n",s,x);//Case #1: 129
			continue;
		}
		last = 1;
		for ( i = tot-1; i >= 1; --i){
			if (a[i] < a[i+1]){
				break;
			}
		} 
		j = i+1;
		while (j < tot && a[j] <= a[j+1]){
			j++;
		}
		a[j]--;
		rep (k,1,j-1){
			a[k] = 9;
		}
		if (a[tot]==0){
			tot--;
		}
		printf("Case #%d: ",s);
		rep2 (k,tot,1){
			cout << a[k];
		}
		cout << endl; 
	}
	return 0;
}

