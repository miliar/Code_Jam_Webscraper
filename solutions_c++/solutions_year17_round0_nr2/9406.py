/*
 *
 *
 * Copyright 2015 Devesh Sawant <devesh@crunchbang>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 *
 */


#include <iostream>


#include <algorithm>
#include <numeric>  // accumulate
#include <fstream>
#include <vector>
#include <string>

#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
// GCJ Challenge 2017
//


using namespace std;


#define SMALL_INPUT_FILE "B-small-attempt3.in"
#define LARGE_INPUT_FILE "B-large-attempt.in"
#define OUTPUT_FILE "tidynum-output.txt"
#define FILENAME_SIZE 20


typedef long long ll;


ll ipow(ll base, ll exp)
{
   ll result = 1;

   while(exp)
   {
       if(exp & 1)
          result *= base;

       exp >>= 1;
       base *= base;

   }

   return result;

}


ll largTidyNum(ll N)
{
   int count=0;
   vector <ll> digits;
   ll ans;

   while(N > 0)
   {
       digits.push_back(N % 10);
       N /= 10;
       count++;

   }

   if(count==1)
    return digits[0];

   // standard case

   for(int i=count-1; i>0; --i)
   {
        if(digits[i] > digits[i-1])
        {
              if(i+1==count)
              {
                 digits[i] -= 1;
              }
              else
              {
                 digits[i] -= 1;
                 if(digits[i+1] > digits[i])
                 {

                    digits[i+1] -= 1;
                    digits[i] = 9;
                 }
              }
              // 1111...10.00..0 case
              if(digits[i]==0)
              {

                 ans =  ipow(10,count-1) - 1;
                 cout << ans << endl;
                 return ans;
              }

              while(i-->=0)
                digits[i] = 9;
        }

   }

   // construct number;

   ans = 0;
   ll mult=1;
   for(int k=0; k<count; ++k)
   {
       ans = ans + digits[k]*mult;
       mult = mult * 10;

   }

   return ans;


}




int main(int argc, char **argv)
{
	fstream  inpfd ,outfd ;
	char inputfile[FILENAME_SIZE];
	char ch;
	inputfile[FILENAME_SIZE - 1] = '\0';
	string inp;
	//cout << inputfile[3];
 /*
	if (argc > 1 )
	{
		// not overflow safe --> get string length of destination
		strncpy( inputfile , argv[1] , strlen( argv[1] ) );
	}
	*/
    cin >> ch ;

    if ( ch == 's' )
    {
		inpfd.open( SMALL_INPUT_FILE ,ios::in);
	}
	else
	{
		inpfd.open( LARGE_INPUT_FILE ,ios::in);
	}


	outfd.open( OUTPUT_FILE , ios::out );

	if ( ! inpfd )
	     printf("Not opened\n");


	int T, i = 1 ;
	ll N;

    inpfd >> T;

    while(T-->0)
    {
        inpfd >> N;

        outfd << "Case #" << i++ << ": " << largTidyNum(N) << "\n";



    }


	inpfd.close();
	outfd.close();


	return 0;
}
