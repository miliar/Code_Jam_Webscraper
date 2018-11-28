/**
* KagreTheBarbarian
* CodeJam 2017
* Compiles with Borland 5.5.1
*
* program framework coppied from the standard example on the google quick start guide.
*
* Compile
*  c:\bcc32 bathroom.cpp
* Run
*  c:\bathroom.cpp < in.txt > out.txt
*/

#include <iostream>
using namespace std;
unsigned __int64 GetS(unsigned __int64 n, unsigned __int64 k);

void main() {
   int t=0;
   unsigned __int64 n, k, ret, min, max;

   cin >> t;
   for (int i = 1; i <= t; ++i) {
      cin >> n >> k;
      min=max=0;
      ret = GetS(n,k);
      if(ret>1){
         if(ret&1){
            min=max=ret>>1;
         }else{
            max=(min=(ret-1)>>1)+1;
         }
      }
      cout << "Case #" << i << ": " << max << " " << min << endl;
   }
}

unsigned __int64 GetS(unsigned __int64 n, unsigned __int64 k){
   unsigned __int64 a, b, aa, ab, ba, bb, ac, bc, tmp;
   if(n==k)return 0;

   a=n;bc=ac=1;
   if(k<=ac)return a;k-=ac;

   if(a&1){
      b=(a>>=1);
   }else{
      b=(a=(a-1)>>1)+1;
   }
   if(k<=bc)return b;k-=bc;
   if(k<=ac)return a;k-=ac;

   while(k>0){
      if(a&1){
         aa=a>>1;ac<<=1;ab=-1;
      }else{
         aa=(a-1)>>1;ab=aa+1;
      }
      if(b&1){
         bb=b>>1;bc<<=1;ba=-1;
      }else{
         ba=(b-1)>>1;bb=ba+1;
      }
      tmp=ac;
      a=aa;if(a==ba)ac+=bc;
      b=bb;if(b==ab)bc+=tmp;
      if(k<=bc)return b;k-=bc;
      if(k<=ac)return a;k-=ac;
   }
   return 0;
}