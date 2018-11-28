#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

int power_of_two(long long int k);
long long int tree_bla(long long int n, long long int k);

long long int num_bla(long long int n, long long int k);

int cc = 0;

int main(){

	long long int t;
	cin >> t;

	long long int i,j;
	long long int n;
	long long int k;

	long long int count=0;
	long long int temp;
	
	ofstream myfile;
 	myfile.open ("output4.txt");

	for(i=0;i<t;i++){

		cin >> n >> k;

		cc = 0;
		temp = num_bla(n,k);


		myfile << "Case #"<< i+1 << ": ";

	
			if(temp % 2 == 0){

				myfile << temp/2 << " " << temp/2 - 1 ; 

			}else{

				myfile << temp/2 << " " << temp/2; 

			}


		myfile << endl; 


	}
	
	myfile.close();	

	return 0;

}

int power_of_two(long long int k){


	int count = 0;
	long long int num = 1;

	while(num <= k){

		num*=2;
		count++;

	}


	return count;


}


long long int tree_bla(long long int n, long long int k){

		long long int h = log2(k);

		long long int i;

			for(i=0;i<h;i++){

				long long int height = log2(k);
				long long int temp = k ;
				long long int partition = pow(2,height);
				long long int place = partition/2;

				k = k - partition + 1;

				if(k <= place){
				
					n = n/2;

				}else{

					k -= place;

					if(n%2 == 0){

						n = n/2 - 1;

					}else{

						n = n/2;

					}

				}

				k += place-1;

				cout << n << "  " << k << endl;
	 
			}
		
		return n;

}


long long int num_bla(long long int n, long long int k){

		long long int h = log2(k);

		long long int i;

		long long int partition = pow(2,h);
		long long int place = partition/2;

		k = k - partition + 1;

		long long int even,odd,even_c,odd_c,temp_even,temp_odd,temp_evenc,temp_oddc;

		if(n%2 == 0){

			even = n;
			even_c = 1;
			odd = -1;
			odd_c = 0;

		}else{

			even = -1;
			even_c = 0;
			odd = n;
			odd_c = 1;

		}

		for(i=0;i<h;i++){

			temp_evenc = 0;
			temp_oddc = 0;
			temp_even = -1;
			temp_odd = -1;

				
			if(even_c > 0){

				if((even/2)%2 == 0){

					temp_even = even/2;
					temp_odd = even/2  - 1;


				}else{

					temp_even = even/2  - 1;
					temp_odd = even/2;


				}
				temp_evenc += even_c;
				temp_oddc += even_c;

			}


			if(odd_c > 0){

				if((odd/2) %2 == 0){

					temp_even = odd/2;
					temp_evenc += 2*odd_c;

				}else{

					temp_odd = odd/2;
					temp_oddc += 2*odd_c;

				}


			}


			even = temp_even;
			odd = temp_odd;
			even_c = temp_evenc;
			odd_c = temp_oddc;


			//cout << even << " " << even_c << " "<< odd << " "<< odd_c << " ";
			//cout << endl; 
 
		}

		long long int large,large_c,small,small_c;

		if(even > odd){

			large = even;
			large_c = even_c;
			small = odd;
			small_c = odd_c;


		}else{

			large = odd;
			large_c = odd_c;
			small = even;
			small_c = even_c;

		}
	
		if(k <= large_c){

			return large;


		}else{

			return small;

		}		

}