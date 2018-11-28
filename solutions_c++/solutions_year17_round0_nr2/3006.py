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



/************************************************************************
Function:
Author:
Description:
Parameters:
 ************************************************************************/
int main( int argc, char * argv[] )
{
	int t, j;
	string num;

	cin >> t;
	for ( int i = 0; i < t; i++ ){

			cin >> num;

			int len = num.length();
			int prev = 0;
			int setprev =0;

			for( j = 1; j < len ; j ++ ){
					if( num[ j-1 ] > num[j] ){
							prev = j;
							break;
					}
			}

			if( prev != 0 ){
					setprev = prev - 1;
					while( setprev >= 0 && num[prev-1] == num[setprev] ){setprev--;}
					
					setprev++;

					num[setprev] -= 1;

					for( j = setprev+1; j < len ; j ++ ){
							num[j] = '9';
					}
			}			
			cout << "Case #" << i + 1 << ": "<< stoull(num) <<"\n";
	}

	return 0;
}

