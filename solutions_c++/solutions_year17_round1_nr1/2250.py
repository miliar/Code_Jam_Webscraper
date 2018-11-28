/************************************************************************
Program: 
Author: ZArthur 
Class:
Instructor:
Date:
Description: 
Input:
Output:
Compilation instructions:
Usage:
Known bugs/missing features:
Modifications:
Date                Comment            
----    ------------------------------------------------
 ************************************************************************/

#include <iostream>
#include <fstream> 
#include <vector> 
#include <cmath>
#include <string>


using namespace std;
/*********************** global symbolic constants *********************/

int r,c;
/*********************** global type definitions ***********************/

/*********************** function prototypes ***************************/



void vdfill( char arr[][25] ){
		int it;
	for( int i = 0; i < r; i++){
			for( int j = 0; j < c; j++){
					if( arr[i][j] != '?' ){
							it = 1;
							while( arr[i+it][j] == '?' && i+it < r) {
									arr[i+it][j] = arr[i][j];
									it++;	
							}
					}
			}
	}
}

void vufill( char arr[][25] ){
		int it;
	for( int i = 0; i < r; i++){
			for( int j = 0; j < c; j++){
					if( arr[i][j] != '?' ){
							it = 1;
							while( arr[i-it][j] == '?' && i-it >= 0) {
									arr[i-it][j] = arr[i][j];
									it++;	
							}
					}
			}
	}
}

void rfill( char arr[][25] ){
		int it;
	for( int i = 0; i < r; i++){
			for( int j = 0; j < c; j++){
					if( arr[i][j] != '?' ){
							it = 1;
							while( arr[i][j+it] == '?' && j+it < c) {
									arr[i][j+it] = arr[i][j];
									it++;	
							}
					}
			}
	}
}
void lfill( char arr[][25] ){
		int it;
	for( int i = 0; i < r; i++){
			for( int j = 0; j < c; j++){
					if( arr[i][j] != '?' ){
							it = 1;
							while( arr[i][j-it] == '?' && j-it >= 0) {
									arr[i][j-it] = arr[i][j];
									it++;	
							}
					}
			}
	}
}

void fill( char arr[][25]){
	vdfill( arr );
	vufill( arr );
	rfill( arr );
	lfill( arr );
}

int main( int argc, char * argv[] )
{
		int t;
		string mystr;
	
		cin >> t;

		for( int i = 0; i < t; i++){
				char cake[25][25] = {0};

				cin >> r >> c;
				

				for( int j = 0; j < r; j++){
						cin >> mystr;
						for( int k = 0; k < c; k++){
								cake[j][k] = mystr[k];			
						}
				}



				fill( cake );


				cout << "Case #" << i +1 << ":" << endl;

				for( int j = 0; j < r; j++){
						for( int k = 0; k < c; k++){
								cout << cake[j][k];
						}
						cout<< endl;
				}


		}

	return 0;
}

