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
#include <queue>

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
	
	int t,i;
	unsigned long mygap;

	cin >> t;
	for( i = 0; i < t; i++){

			unsigned long k, n;

			//cin >> k >> n;
			cin >> n >> k;


//			while( n != 1){ 
//					if( k & 1 == 0 ){
//							n>>=1;
//							k>>=1; 
//					}
//					else{
//
//							if( n & 1 == 1){
//								k>>=1;
//								k-+1;
//								n>>=1;
//							}
//							else{
//									k>>=1;
//									n>>=1;
//							}
//					}
//			}

			while( k != 1)
			{
					//cout << n << " " << k << endl;

					k = k - 1;

					if((n % 2) == 1 && (k % 2) == 0)
					{
							k = (k / 2);
							n = (n / 2);
					}
					else if((k % 2) == 1)
					{
							k = (k / 2) + 1;
							n = (n / 2);
					}
					else if((n % 2) == 0 && (k % 2) == 0)
					{
							k = (k / 2);

							if(n / 2 == 0)
							{
									n = 0;
							}else
							{
									n = (n / 2) - 1;
							}
					}

					//cout << n << " " << k << endl;
			}


			//cout << "Case #" << i + 1 << ": "<< n  << " " << k <<"\n";
			mygap = n;

			if( mygap & 0x1 == 1 ){
					//cout << "Case #" << i + 1 << ": "<< (mygap>>1)  << " " << (mygap>>1) <<"\n";
					cout << "Case #" << i + 1 << ": "<< (mygap>>1)  << " " << (mygap>>1) <<"\n";
			}
			else {
					//cout << "Case #" << i + 1 << ": "<< (mygap>>1)  << " " << ( mygap>>1) -1 <<"\n";
					cout << "Case #" << i + 1 << ": "<< (mygap>>1)  << " " << ( mygap>>1) -1 <<"\n";
			}

	}
}

