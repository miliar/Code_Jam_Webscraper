#include <bits/stdc++.h>

using namespace std;
int A[18];

void arreglo(long long x, int &n){
	int i=0;
	while(x>0){
		A[i]= x%10;
		x/=10;
		i++;
	}
	int aux;
	int k=i-1;
	n=i;
	for(int j=0; j<(i-i%2)/2; j++){
		aux=A[j];
		A[j]=A[k];
		A[k]=aux;
		k--;
	}
}

bool tidy(int n ){
	for(int i=0; i<n-1; i++){
		if(A[i]>A[i+1]){
			return false;
		}
	}
	return true;
}
void tidyzar(int m){
	int i=0;
	while(i<m-1){
		if(A[i]>A[i+1]){
			A[i]-=1;
			for(int k=i+1; k<m; k++){
				A[k]=9;
		    }
		}
		i++;
	}
}


int main(){
	int T;
	cin >> T;
	long long N;
	for(int i=1; i<=T;i++){
		int m;
		cin >> N;
		arreglo(N, m);
		while(!tidy(m)){
			tidyzar(m);
		} 
		cout << "Case #" << i << ": " ;
		for(int k=0; k<m; k++){
			if(k!=0 || A[k]!=0) cout << A[k];
		}
		cout << endl;
	}
	return 0;
}

