#include<algorithm>
#include<assert.h>
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<ctime>
#include<map>
#include<set>

#define F0(i,n) for(i=0; i < n; i++)
#define F1(i,n) for(i=1; i < n; i++)
#define Fxy(i,x,y) for(i=x; i < y; i++)

#define LL long long
#define ULL unsigned long long

using namespace std;

int main()
{
  int c,i,j,T;
  int D,N,K,S;
  cin >> T;
  ULL maxK;
  ULL maxS;

  F1(c, T+1){
    cout << "Case #" << c << ":";

    cin >> D >> N;

    ULL slowK;
    ULL slowS;
    cin >> slowK >> slowS;

    F0(i,N-1){
      cin >> K >> S;
      if ((D-K)*slowS > (D-slowK)*S){
	slowK = K;
	slowS = S;
      }
    }

    printf(" %1.6f\n", ((double)(D*slowS))/(D-slowK));
  }
}
