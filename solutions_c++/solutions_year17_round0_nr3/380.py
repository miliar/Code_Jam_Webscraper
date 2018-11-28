#include<iostream>
#include<cmath>
#include<string>
#include<assert.h>
#include<vector>
#include<map>
#include<set>

#define F0(i,n) for(i=0; i < n; i++)
#define F1(i,n) for(i=1; i < n; i++)
#define ULL unsigned long long

using namespace std;

int main()
{
  int c,i, numCases;
  ULL K,N;
  cin >> numCases;

  F1(c, numCases + 1){
    cout << "Case #" << c << ": ";

    cin >> N >> K; 

    //    cerr << "N: " << N << ", K: " << K << "\n";

    multiset<ULL> nextStall;
    nextStall.insert(N);

    F0(i,K){
      ULL max = *(nextStall.rbegin());
      ULL a = max/2;
      ULL b = (max == 0) ? 0 : (max-1)/2;
      if (i == K-1){
	cout << a << " " << b << "\n";
      } else {
        //cerr << "erasing: " << max << ", inserting: " << a << ", " << b << "\n";
	nextStall.insert(a);
	nextStall.insert(b);
	nextStall.erase(nextStall.find(max));
      }
    }

  }
}
