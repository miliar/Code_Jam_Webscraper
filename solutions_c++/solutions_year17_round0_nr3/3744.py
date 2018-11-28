
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <set>
#include <string>

#define	st first
#define	nd second
#define	mp make_pair
#define	pb push_back
#define	lli long long int
#define	all( gg )	gg.begin(),gg.end()
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	FP( ii,aa,bb ) for( int ii=aa;ii<=bb;ii++ )
#define	FM( ii,aa,bb ) for( lli ii=aa;ii>=bb;ii-- )
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;
#define next asdaskhjdkjs
#define	mod	10000LL
#define hash jaklsfjalks
using namespace std;



int main(){

	int t,id=0;
	cin >> t;

	while(t--){
		id++;
		lli n,k;
		multiset<lli>	S;
		cin >> n >> k;
		S.insert(n+1);
		lli l,r,p;
		while(k--){
			p = *S.rbegin();
			S.erase(S.find(p));
			l = p/2;
			r = p-p/2;
			S.insert(l);
			S.insert(r);
		}
		cout << "Case #" << id << ": " << max(l,r)-1 << " " << min(l,r)-1 << endl;
	}

}