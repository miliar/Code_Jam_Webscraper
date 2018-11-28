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

/*********************** global type definitions ***********************/

/*********************** function prototypes ***************************/


void flip( string & cake, int s, int k );

/************************************************************************
Function:
Author:
Description:
Parameters:
 ************************************************************************/
int main( int argc, char * argv[] )
{
	
	int t,k,ret;
	string cake;

	cin >> t;

	for( int i = 0; i < t; i++){

			cin >> cake >> k;
			ret = 0;

			int len = cake.length();
			for( int j = 0; j < len; j++){
					if( cake.find('-') != string::npos ){
							if( len - j < k ){
									cout << "Case #" << i + 1 << ": IMPOSSIBLE\n";
									j = len;
									k = -1;
							}
							else if( cake[j] == '-') {
									flip( cake, j, k );
									ret ++;
							}
					}
			}

		if( -1 != k )
		cout << "Case #" << i + 1 << ": "<< ret <<"\n";

	}

	return 0;
}


void flip( string & cake, int s, int k ){

		for( int i = 0; i < k; i++){
				if( cake[s+i] == '-' ){
						cake[s+i] = '+';
				}
				else{
						cake[s+i] = '-';
				}

		}
}

