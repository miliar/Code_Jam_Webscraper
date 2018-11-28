#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;


int main(){

	int t;
	cin >> t;

	string a;

	int i,j,k,n,z;

	int arr[1001];

	ofstream myfile;
 	myfile.open ("output6.txt");


	for(i=0;i<t;i++){


			cin >> a >> k;

			myfile << "Case #"<< i+1 << ": ";

			for(j=0;j<a.length();j++){


				if(a[j] == '+'){

					arr[j] = 1;


				}else{


					arr[j] = 0;

				}

			}

			n = a.length();
			n = n - k + 1;

			int count = 0;
			int count1 = 0;
			int flag = 0;

			for(j=0;j<n;j++){

				if(arr[j] == 0){

					for(z = j;z<j+k;z++){


						arr[z] = abs(arr[z] - 1);


					}

					count++;

				}

				// for(z = 0;z<a.length();z++){


				// 	cout <<	arr[z] ;


				// }

				// cout << endl;

			
			}

			for(j=n;j<a.length();j++){



				if(arr[j] == 0){

					flag = 1;
					break;

				}


			}


			if(flag == 0){

				myfile << count << endl;


			}else{

					flag = 0;

					for(j=a.length()-1;j>=0;j--){


						if(a[j] == '+'){

							arr[a.length()-1-j] = 1;


						}else{


							arr[a.length()-1-j] = 0;

						}

					}

					

					for(j=0;j<n;j++){

							if(arr[j] == 0){

								for(z = j;z<j+k;z++){


									arr[z] = abs(arr[z] - 1);


								}

								count1++;

							}

							// for(z = 0;z<a.length();z++){


							// 	cout <<	arr[z] ;


							// }

							// cout << endl;

						
						}

						for(j=n;j<a.length();j++){



							if(arr[j] == 0){

								flag = 1;
								break;

							}


						}

					if(flag == 0){

							myfile<< count1 << endl;


					}else{


						myfile << "IMPOSSIBLE" << endl;

					}



			}


	}

	myfile.close();

	return 0;

}