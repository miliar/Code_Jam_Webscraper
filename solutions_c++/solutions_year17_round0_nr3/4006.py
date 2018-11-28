#include <iostream>
#include<string>
#include<vector>
#include <cmath>

/*
 Bathroom stalls
*/

using namespace std;

//#define DEBUG

// recursive solution

vector<long int> rec(long int n, long int k){
	// return A, #small (A) #big (A+1)
	vector<long int> res = vector<long int>(3);
	long int z = 0;
	if (k == 1){
		//initial case
		if( (n%2)==0){
			// pair
			res[0] = max(z, n/2 -1) ;
			res[1] = 1;
			res[2] = 1;
		}else{
			res[0] = n/2 ; 
			res[1] = 2;
			res[2] = 0;
		}
	}else{
		vector<long int> prec = rec(n, k/2);		
		//need x to compute max, min
		long int G = prec[2]; //number of big int
		long int P = prec[1]; //number of small int
		long int A = prec[0];
		if ( (A%2)==0){
			// Old A pair
			res[0] = max(z, A/2-1);
			res[1] = P;
			res[2] = P + 2*G;
			//opti var
		}else{
			res[0] = A/2;	
			res[1] = 2*P + G;
			res[2] = G;
		}
	}


#ifdef DEBUG
	cout << "k = "<< k << " | res : ";
	for (long int i : res){
		cout << i << ",";
	}
	cout << endl;
#endif

	return res;
}

int main(){

	int n; //number of test cases
	cin >> n; cin.ignore();
	vector<long int> bath =  vector<long int>(n);
	vector<long int> ppl =  vector<long int>(n);
	for (int i = 0; i<n ; ++i){
		cin >> bath[i]; cin>>ppl[i]; cin.ignore();
	}
	long int z = 0;
	for (int i = 0; i<n ; ++i){
		long int k = ppl[i];
		long int N = bath[i];
		long int mini, maxi;
		if (k == 1){
			if( (N%2)==0){
				mini = max(z, N/2-1);
				maxi = N/2;
			}else{
				mini = N/2;
				maxi = N/2;
			}
		}else{
			long int lg = floor(log(k)/log(2)); //log in base 2 of k
			vector<long int> res = rec(N, pow(2, lg-1));		
			long int x = k - pow(2,lg);
#ifdef DEBUG
			cout << "x " << x << endl;
#endif
			long int P = res[1];
			long int G = res[2];
			long int A = res[0];
			if (x<G){
				//it's a split of a A+1
				if ( ( A % 2 ) == 0 ){
					mini = (A+1)/2;
					maxi = (A+1)/2;
				}else{
					mini = max(z, (A+1)/2-1);
					maxi = (A+1)/2;
				}
			}else{
				//it's a split of A
				if ( ( A % 2 ) == 0 ){
					//spliting A that is pair
					mini = max(z, A/2-1);
					maxi = A/2;
				}else{
					mini = A/2;
					maxi = A/2;
				}			
			}
		}
		cout << "Case #"<<i+1<< ": " << maxi << " " << mini << endl;
	}
}
