#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define s second
#define f first
#define _ ios_base::sync_with_stdio(false);cin.tie(0);

using namespace std;

const int maxn = (int)(1e5)+2;
const int mod = (int)(1e9)+7;

int n, m, u[22];
char row[333], a[55][55];

int main() {
	int tt;
	cin >> tt;
	for (int ii = 1; ii <= tt; ii++) {
	 //	printf("Case #%d:\n", ii);
	 	cout << "Case #" << ii << ":\n";
	 	memset(u,0,sizeof u);
	 	cin >> n >> m;
	 	char last = 'A';
	 	bool flag = false;
	 	for (int i = 1; i <= n; i++) {
	 		last = '#';
	 		for (int j = 1; j <= m; j++)  {
	 			cin >> a[i][j];
	 			if (a[i][j] != '?') 
	 				last = a[i][j];
	  	 	}
	  		if (last != '#') {
	  			u[i] = 1;
	  			row[i] = last;
	  			flag = true;
	  	  	}
	   	}
	   	
	   	for (int i = n; i >= 1; i--) {
	   		if (!u[i]) continue;
	   		for (int j = m; j >= 1; j--) {
	   			if (j==m) last = row[i];
	   	 		if (a[i][j] != '?') last = a[i][j];
	   		 	a[i][j] = last;
	   	 	}
	   	}
	  	for (int i = 1; i <= n; i++)
	  	for (int j = 1; j <= m; j++) {
	  	 	if (a[i][j] != '?') {
	  	 	 	for (int up = i-1; up >= 1; up--)
	  	 	 		if (a[up][j] == '?') a[up][j] = a[i][j];
	  	 	 		else break;
	  	 	  	for (int down = i+1; down <= n; down++)
	  	 	  		if (a[down][j] == '?') a[down][j] = a[i][j];
	  	 	  		else break;
	  	 	}
	  	}
	  	if (!flag)
	  		for (int i = 1; i <= n;i++)
	  		for (int j = 1; j <= m; j++)
	  			a[i][j] = 'A';
	  	for (int i = 1; i <= n; i++) {
	  	    for (int j = 1; j <= m; j++)
	  	    	cout << a[i][j];
	  	   	cout << endl;
	  	}	
	}
	return 0;
}