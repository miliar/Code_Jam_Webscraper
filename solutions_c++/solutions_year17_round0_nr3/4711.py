// Template for Codejam
// use ./a.out < smallQ#.in > smallQ#.txt

#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <cstdlib>
#include <vector>
#include <sstream>
#include <utility> // for pair
#define REP(i,n) for(ll i=0;i<(n);i++)
#define FOR(i,a,b,c) for(int i=a;i<b;i += c)
#define FORd(i,a,b,c) for(int i=a;i>=b;i -=c)
#define vi vector<ll>
#define vii vector<vector<ll> >
#define ll long long int //range -> –9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
#define ui unsigned int // range -> 0 to 4,294,967,295
#define ull unsigned long long
using namespace std;


int main(){
	int n;
	cin >> n;
	REP(i,n){
		ll N,k;
		cin >> N >> k;
		cout << "Case #"<< i+1 << ": ";
		ll partitions = (int)pow(2,(int)(log(k)/log(2)));
		ll toilets = N-partitions+1;
		ll minSize = (int)(toilets/partitions);
		ll maxSize = minSize+1;
		ll maxN = toilets - minSize*partitions;
		ll minN = partitions -maxN;
		ll rem = k - partitions +1;
		if (rem <= maxN){
			if(maxSize%2 ==0)cout << (int)(maxSize/2) << " " <<(int)(maxSize/2)-1<< endl;
			else cout << (int)(maxSize/2) << " " <<(int)(maxSize/2) << endl;
		}
		else{
			if(minSize%2 ==0)cout << (int)(minSize/2) << " " <<(int)(minSize/2)-1<< endl;
			else cout << (int)(minSize/2) << " " <<(int)(minSize/2) << endl;	
		}

	} 
	return 0;
}