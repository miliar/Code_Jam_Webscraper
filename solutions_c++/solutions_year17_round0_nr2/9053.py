#include<stdio.h>
#include<cstring>
#include<string>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<map>
#include<list>
#include<iostream>

using namespace std;

long long int scanint();
 
inline long long int scanint()
{
    long long int c = getchar_unlocked(),x=0;
    for(;((c<48 || c>57) && c != '-');c = getchar_unlocked());
    for(;c>47 && c<58;c = getchar_unlocked()) {x = (x<<1) + (x<<3) + c - 48;}
    return x;
}

//unsigned int getDigits(unsigned long long int N, list<short> &digits)
unsigned int getDigits(unsigned long long int N, short *digits)
{
   unsigned int length = 0;
   while(N)
   {
      short digit = N%10;
      N /= 10;
      digits[length] = digit;
      ++length;
   }
   return length;
}

bool isTidy(unsigned long long int N)
{
   short a[30] = {0};
   unsigned int numOfDigits = getDigits(N, a);
   short prev = a[numOfDigits-1];
   for( int i=numOfDigits-2; i>=0; --i )
   {
      if( prev > a[i] )
      {
         return false;
      }
      prev = a[i];
   }
   return true;
}

int main()
{
   FILE *fout,*fin;
   fout = fopen( "output.txt", "w" );
   if( NULL == fout )
   {
      printf("Not able to open file");
      return -1;
   }
   fin = fopen( "input1.txt", "r" );
   if( NULL == fin )
   {
      printf("Not able to open file");
      return -1;
   }

   int T;
   char read[1020],outString[1020];
   memset( read, 0, 1020 );
   fscanf( fin, "%s", read );
   T = atoi( read );
   for( int x=1;x<=T;x++ )
   {
      memset( read, 0, 1020 );
      //unsigned long long int N =
      fscanf( fin, "%s", read );
      std::string data = read;
      std::string::size_type sz = 0;
      unsigned long long int N = std::stoull(data, &sz, 0);//scanint();
      //printf("%llu\n", N);
      //short prev = a[numOfDigits-1];
      unsigned int curPos = 0;
      while( !isTidy(N) )
      {
         short a[30] = {0};
         unsigned int numOfDigits = getDigits(N, a);
         if( curPos<numOfDigits )
         {
            short curDig = a[curPos];
            //std::cout<<curDig<<":"<<N<<std::endl;
            if( curDig < 9 )
            {
               curDig = curDig+10;
            }
            unsigned long long int minusNum = (curDig-9);
            minusNum = minusNum*(pow(10, curPos));
            N -= minusNum;
            curPos++;
         }
         else
         {
            break;
         }
      }
      fprintf( fout, "Case #%d: %llu\n", x, N );
   }
   return 0;
}
