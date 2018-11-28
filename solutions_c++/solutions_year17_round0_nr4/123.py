#include<cstdio>
#include<iostream>
using namespace std;
char a[110][110], b[110][110];
bool R[110],C[110],A[300],B[300];
int RR[110],CC[110],AA[330],BB[330];
int rrr, ccc, aaa, bbb;
// char ans1[30000];
// int ans2[30000];
// int ans3[30000];
bool vA[3000],vB[3000];

void fill(int r, int c, char x) {
	if(x == 'x') {
		if(b[r][c] == '+') {
			b[r][c] = 'o';
		} else if(b[r][c] == '.') {
			b[r][c] = 'x';
		}
	} else if(x == '+') {
		if(b[r][c] == 'x') {
			b[r][c] = 'o';
		} else if(a[r][c] == '.') {
			b[r][c] = '+';
		}
	}
}

int pts1(int n) {
	int ret = 0;
	for(int i=1;i<=n;i++) {
		for(int j=1;j<=n;j++) {
			if(a[i][j] == '+' || a[i][j] == 'x')
				ret++;
			else if(a[i][j] == 'o')
				ret += 2;
		}
	}
	return ret;
}

int pts2(int n) {
	int ret = 0;
	for(int i=1;i<=n;i++) {
		for(int j=1;j<=n;j++) {
			if(b[i][j] == '+' || b[i][j] == 'x')
				ret++;
			else if(b[i][j] == 'o')
				ret += 2;
		}
	}
	return ret;
}

int diff(int n) {
	int ret = 0;
	for(int i=1;i<=n;i++) {
		for(int j=1;j<=n;j++) {
			if(a[i][j] != b[i][j]) ret++;
		}
	}
	return ret;
}

void print_diff(int n) {
	for(int i=1;i<=n;i++) {
		for(int j=1;j<=n;j++) {
			if(a[i][j] != b[i][j]) 
				cout << b[i][j] << " " << i << " " << j << endl;
		}
	}
}

int main() {
	freopen("D.in","r",stdin);
	freopen("D.txt","w",stdout);
	int t,r, rr,x,y,n,m;
	char c;
	cin >> t;
	for(int aa=0;aa<t;aa++) {
		for(int i=0;i<101;i++) for(int j=0;j<101;j++) {
			a[i][j] = '.';
			b[i][j] = '.';
		}
		for(int i=0;i<101;i++) {
			R[i] = true;
			C[i] = true;
		}
		for(int i=0;i<250;i++) {
			A[i] = true;
			B[i] = true;
		}


		cin >> n >> m;
		for(int i=0;i<m;i++) {
			cin >> c >> x >> y;
			a[x][y] = c; 
			b[x][y] = c;
			if(c == '+') {
				A[x+y-2] = false;
				B[n-1-y+x] = false;
			} else if(c == 'x') {
				R[x] = false;
				C[y] = false;
			} else if(c == 'o') {
				A[x+y-2] = false;
				B[n-1-y+x] = false;
				R[x] = false;
				C[y] = false;
			}
		}

		rrr = 0;
		ccc = 0;
		aaa = 0;
		bbb = 0;
		for(int i=1;i<=n;i++) {
			if(R[i]) {
				RR[rrr++] = i;
			}
			if(C[i]) {
				CC[ccc++] = i;
			}
		}

		for(int i=0;i<rrr;i++) {
			// cout << "RRR " << RR[i] << " " << CC[i] << endl;
			fill(RR[i],CC[i],'x');
		}

		int l = 2*n - 2;
		int pp , qq;
		for(int i=0;i<n-1;i++) {
			if(A[i]) {
				AA[aaa++] = i;
			}
			if(A[l-i]) {
				AA[aaa++] = l-i;
			}
			if(B[i]) {
				BB[bbb++] = i;
			}
			if(B[l-i]) {
				BB[bbb++] = l-i;
			}
		}
		if(A[n-1]) {
			AA[aaa++] = n-1;
		}
		if(B[n-1]) {
			BB[bbb++] = n -1;
		}
		int xx ,yy;
		int nn = 2*n;
		for(int i=0;i<aaa;i++) vA[i] = false;
		for(int j=0;j<bbb;j++) vB[j] = false;

		// for(int i=0;i<aaa;i++) cout << AA[i] << " " ; cout << endl;
		// for(int i=0;i<bbb;i++) cout << BB[i] << " " ; cout << endl;

		for(int i=0;i<aaa;i++) {
			for(int j=0;j<bbb;j++) {
				if(vA[i] | vB[j]) continue;
				xx = AA[i]+BB[j]-n+1 + 2;
				yy = AA[i]-BB[j]+n-1 + 2;
				
				if(xx % 2 == 0 && yy % 2 == 0 && xx >= 1 && xx <= nn && yy >= 1 && yy <= nn) {
					// cout << i << " " << j << " xx " << xx << " yy " << yy << endl;
					fill(xx/2,yy/2,'+');
					vA[i] = true;
					vB[j] = true;
				}
			}
		}
		// cout << pts1(n) << endl;;
		// for(int i=1;i<=n;i++) {
		// 	for(int j=1;j<=n;j++) {
		// 		cout << a[i][j];
		// 	}
		// 	cout << endl;
		// }

		// cout << "----" <<endl;

		// cout << pts2(n) << endl;;
		// for(int i=1;i<=n;i++) {
		// 	for(int j=1;j<=n;j++) {
		// 		cout << b[i][j];
		// 	}
		// 	cout << endl;
		// }





		cout << "Case #" << aa+1 << ": " << pts2(n) << " " << diff(n) << endl;
		print_diff(n);
	}
}