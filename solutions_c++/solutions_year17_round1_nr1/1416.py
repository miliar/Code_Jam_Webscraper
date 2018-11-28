# include <bits/stdc++.h>
using namespace std;
char a[102][102];
int main () {
	
	int t, n, m, i, j, k;
	
	freopen ("Al.in", "r", stdin);
	freopen ("Ao.txt", "w", stdout);
	
	cin >> t;
	
	int x = 1;
	while (t--) {
		
		cin >> n >> m;
		
		for (i=0; i<n; i++)
			for (j=0; j<m; j++)
				cin >> a[i][j];
			
		for (i=0; i<n; i++) {
			
			for (j=0; j<m; j++) {
				
				if (a[i][j] != '?') {
					
					char temp = a[i][j];
					
					for (k = j-1; k>=0; k--) {
						
						if (a[i][k] != '?')
							break;
							
						a[i][k] = temp;	
					}
					
					for (k = j+1; k<m; k++) {
						
						if (a[i][k] != '?')
							break;
						
						a[i][k] = temp;
							
					}
					
					j = k-1;
				}
			}
				
		}
		
			
		for (j=0; j<m; j++) {
			
			for (i=0; i<n; i++) {
				
				if (a[i][j] != '?') {
					
					char temp = a[i][j];
					
					for (k = i-1; k>=0; k--) {
						
						if (a[k][j] != '?')
							break;
							
						a[k][j] = temp;	
					}
					
					for (k = i+1; k<n; k++) {
						
						if (a[k][j] != '?')
							break;
						
						a[k][j] = temp;
							
					}
					
					i = k-1;
				}
			}
				
		}
		
		cout << "Case #" << x << ": \n";
		
		for (i=0; i<n; i++) {
			
			for (j=0; j<m; j++)
				cout << a[i][j];
				
			cout << endl;
				
		}
		
		x++;
		
	}
	
	return 0;
	
}
