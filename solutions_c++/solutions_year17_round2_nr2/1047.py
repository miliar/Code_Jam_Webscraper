#include <bits/stdc++.h>
#define MAX 100001
#define ll long long
using namespace std;


int main(){
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	int t,cs = 1;
	cin >> t;
	while(t--){
		int n,r,o,y,g,b,v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << cs++ << ": ";
		if (r>y+b || y>r+b || b>r+y){
			cout << "IMPOSSIBLE\n";
			continue;
		}
		int prev;
		int mx = max(r,max(b,y));
		int f;
		if (r==mx){
			r--;
			prev = 1;
		cout << 'R';
			f = 1;
		}
		else if (y==mx){
			y--;
			prev = 2;
		cout << 'Y';
			f = 2;
		}
		else if (b==mx){
			b--;
			prev = 3;
		cout << 'B';
			f = 3;
		}
		n--;
		while(n--){
			if (prev==1){
				if (y>b){
					y--;
					prev = 2;
		cout << 'Y';
				}
				else if (b>y){
					b--;
					prev = 3;
		cout << 'B';
				}
				else{
					if (f==2){
						y--;
						prev = 2;	
		cout << 'Y';	
					}
					else{	
						b--;
						prev = 3;
		cout << 'B';
					}
				}
			}
			else if (prev==2){
				if (r>b){
					r--;
					prev = 1;
		cout << 'R';
				}
				else if (b>r){
					b--;
					prev = 3;
		cout << 'B';
				}
				else{
					if (f==1){
						r--;
						prev = 1;
		cout << 'R';		
					}
					else{	
						b--;
						prev = 3;
		cout << 'B';
					}
				}
			}
			else if (prev==3){
				if (y>r){
					y--;
					prev = 2;
		cout << 'Y';
				}
				else if (r>y){
					r--;
					prev = 1;
		cout << 'R';
				}
				else{
					if (f==2){
						y--;
						prev = 2;
		cout << 'Y';		
					}
					else{	
						r--;
						prev = 1;
		cout << 'R';
					}
				}
			}
		}
		cout << endl;
	}
	return 0;
}