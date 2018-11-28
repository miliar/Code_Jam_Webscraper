#include<iostream>

using namespace std;

int main(){
  int c;
  cin >> c;
  for(int cur =1; cur <= c; cur++){
    cin.ignore();
    long long N,K;
    cin >> N >> K;

    long long max, min;
    long long n_max, n_min;

    long long k = 0;
    long long pw = 1;

    max = N+1;
    min = N;
    n_max = 0;
    n_min = 1;

    while(k + pw < K){
      if(min%2==0){
	long long m = min/2;
	min = m-1;
	max = m;
	long long n_max2 = 2*n_max+n_min;
	long long n_min2 = n_min;
	n_min = n_min2;
	n_max = n_max2;
      }else{
        long long m = min/2;
	min = m;
	max = m+1;
        long long n_max2 = n_max;
        long long n_min2 = 2*n_min+n_max;
	n_min = n_min2;
	n_max = n_max2;
      }
      k+=pw;
      pw*=2;
    }

    long long t = K-k;
    long long toCut = (t<=n_max ? max : min);
    
    cout << "Case #" << cur << ": " << (toCut)/2 << " " << ((toCut-1)/2) << endl;
  
  }

}
