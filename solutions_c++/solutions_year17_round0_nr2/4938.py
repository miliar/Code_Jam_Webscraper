#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;


int main(){

	int t;
	cin >> t;

	int i,j;
	long long int n;
	long long int a;
	int b,c,d,k;
	int arr[20];
	int flag = 0;
	int zero,zer1;

	ofstream myfile;
 	myfile.open ("output.txt");

	for(i=0;i<t;i++){

		cin >> n;

		j=0;
		a = n;

		zero = 0;
		zer1 = 0;

		while(a != 0){

			b = a%10;
			arr[j] = b;
			j++;

			a = a-b;
			a = a/10;


		}

		d = j-1;
		flag = 0;

		for(c=0;c<d;c++){

			if(arr[c] < arr[c+1] || arr[c] == 0 || arr[c+1] == 0){

				arr[c] = 9;
				zero = zer1;
				zer1 = c;

				for(k=zero;k<zer1;k++){

					arr[k] = 9;


				}


				if(arr[c+1] == 1 || arr[c+1] == 0 ){

					arr[c+1] = 9;

					if(c+1 == d){

						arr[c+1] = 0;
						d--;

					}else{

						arr[c+2]--;


					}

				}else{

					arr[c+1]--;

				}

			}

		}

		myfile << "Case #"<< i+1 << ": ";

		for(c=d;c>-1;c--){

			myfile << arr[c];

		}

		myfile << endl;



	}

	myfile.close();

	return 0;

}