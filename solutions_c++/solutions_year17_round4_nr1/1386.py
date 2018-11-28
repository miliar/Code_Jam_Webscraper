#include <bits/stdc++.h> 
using namespace std;
int main (){
	ios_base::sync_with_stdio(0);
	int z;
	cin >> z;
	for (int juo = 1; juo <= z; ++juo){
		int n;
		cin >> n;
		int P;
		cin >> P;
		vector <int> A(P+5, 0);
		for (int i = 0; i < n; ++i){
			int a;
			cin >> a;
			++A[a%P];
		}
		if (P == 2){
			int odp = 0;
			odp += A[0];
			odp += A[1]/2;
			odp += A[1]&1;
			cout << "Case #" << juo<< ": "<<  odp << '\n';
		}
		if (P == 3){
			int odp = 0;
			odp += A[0];
			A[0] = 0;
			int k = min(A[2],A[1]);
			odp += k;
			A[2] -= k;
			A[1] -= k;
			odp += A[1]/3;
			odp += A[2]/3;
			if((A[1]%3) || (A[2]%3))odp += 1;
			cout << "Case #" << juo<< ": "<<  odp << '\n';
		}
		if(P == 4){
			int odp = 0;
			odp  += A[0];
			A[0] = 0;
			int k = min(A[3], A[1]);
			odp += k;
			A[3] -= k;
			A[1] -= k;
			int l = 0;
			if (A[1]) l = 1;
			if(A[3]) l = 3;
			if(l){
				int w1 = 0, w2 = 0;
				w1 = A[l]/4 + A[2]/2;
				if((A[l]%4) || (A[2]%2))++w1;
				if(A[l] >= 2)if(A[2] >= 1){
					w2 = ( (A[l]-2)/4) + ((A[2]-1)/2) + 1;
					if(((A[l]-2)%4) || ((A[2]-1) %2))++w2;
				}
				odp += max(w1,w2);
			}
			else {
				odp += (A[2]/2) + (A[2]&1);	
			}
			cout << "Case #" << juo<< ": "<<  odp << '\n';
		}
	}
}
