#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <fstream>

using namespace std;

const long double pi=3.141592653589793238463;

struct cake{
long h,r;
} cakes[1005];

long double dp[1005][1005];
long n,k;
long double prefix[1005];

int compare(const void* a, const void* b ){

 cake *cakeA = (cake *)a;
 cake *cakeB = (cake *)b;

  if ( cakeB->r > cakeA->r ) return 1;
  if ( cakeB->r == cakeA->r) return (cakeB->h > cakeA->h);
  return -1;

}

long double recurse(int i, int j){
if(i<j-1) return 0;
if(j==1) return prefix[i];
if(dp[i][j]>= 0) return dp[i][j];
long double temp=2* pi * (long double)(cakes[i].r)*(cakes[i].h);
long double ans=temp+recurse(i-1,j-1);
long double ans1=recurse(i-1,j);
if(ans<ans1) ans=ans1;

return dp[i][j]=ans;

}


int main(){

ifstream myfile("sample.txt");
ofstream ifile("out.txt");

int tt,t;
myfile >> t;
for(tt=1;tt<=t;tt++){
    memset(dp,-1.00,1005*1005*sizeof(dp[0][0]));
    myfile >> n >> k;
    for(long i=0;i<n;i++){
    myfile >> cakes[i].r>> cakes[i].h;

    }
    qsort(cakes, n, sizeof(cake), compare);
    /*for(long i=0;i<n;i++){

    ifile << cakes[i].r << " " << cakes[i].h << endl;
    }
    */

    prefix[0]= pi *(long double)(cakes[0].r)*(cakes[0].r)+ 2* pi * (long double)(cakes[0].r)*(cakes[0].h);
    for(long i=1;i<n;i++){
        long double temp=pi * (long double)(cakes[i].r)*(cakes[i].r)+ 2* pi * (long double)(cakes[i].r)*(cakes[i].h);
        prefix[i]=max(prefix[i-1],temp);

    }

    /*for(int i=0;i<n;i++){
       printf("%lf\n", prefix[i]);
    }
    */
    ifile.precision(9);
    ifile.setf( std::ios::fixed, std:: ios::floatfield );
    ifile << "Case #" << tt << ": " <<recurse(n-1,k) << endl;
    //printf("%.9lf\n",recurse(n-1,k));


}




return 0;

}
