#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;



void printarray(bool *array, int N) {
	for (int k=0; k<N; k++) {
		if (array[k])
			cerr << "O";
		else
			cerr << ".";
	}
	cerr << endl;
}

void fill(bool *array, int l, int r, int nb, int N) {
	if (nb<=0 || l<0 || l>=N)
		return;
		
	int mid = l+(r-l)/2;	
	
	array[mid]=true;
	nb--;
	//printarray(array,N);
	
	bool samsize = (mid-1-l == r-mid-1);
	
	if (samsize) {// Half on left
		if (nb%2>0)
			fill(array, l, mid-1, nb/2+1,N);
		else
			fill(array, l, mid-1, nb/2,N);
		// Rest on left
		fill(array, mid+1, r, nb/2,N);
	} else {
		if (nb%2>0)
			fill(array, mid+1, r, nb/2+1,N);
		else
			fill(array, mid+1, r, nb/2,N);
		// Rest on left
		fill(array, l, mid-1, nb/2,N);
	}
}

int main() {
	FILE *fin = freopen("C-small-2-attempt0.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("C-small-2-attempt0.out", "w", stdout);
	int T;
	int N;	// nb stalls
	int K;	// nb people
	cin >> T;


	int mx=0, mn=N;

	for(int t = 0; t < T; t++){
		// Get N
		cin >> N >> K;

		if (K==0) {
			cout << "Case #" << t+1 << ": " << N << " " << N << endl;
			continue;
		}
		
		bool *array = new bool[N];
		for (int n=0; n<N; n++)
			array[n]=false;
		
		// Fill array
		//cerr << N << " " << K << endl;
		//printarray(array,N);
		fill(array, 0, N-1, K-1, N);
		//printarray(array,N);
		
		// Find largest hole
		int cnt=1;
		int maxx=0;
		for (int n=0; n<N; n++) {
			if (array[n]) {
				// Reset
				cnt=0;
			}
			// Remember max
			if (cnt>maxx)
				maxx=cnt;
			//cerr << n << " " << cnt << endl;
			cnt++;
		}
		//cerr << maxx << endl;
				
		if (maxx%2==0) {
			mx=maxx/2;
			mn=maxx/2-1;	
		} else {
			mx=maxx/2;
			mn=mx;	
		}

		//cerr << mx << " " << mn << endl << endl;
		
		//cerr << N << " " << K << ":" << i << " (" << p << " " << q << "): " << mx << " " << mn << endl;//" " << mn << endl;
		
		cout << "Case #" << t+1 << ": " << mx << " " << mn << endl;
		delete[] array;
	}
	return 0;
}
