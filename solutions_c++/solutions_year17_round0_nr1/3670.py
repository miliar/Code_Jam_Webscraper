
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
		string s;
		int k,res=0;
		cin >> s >> k;
		for(int i=0;i<s.size()-k+1;i++){
			if(s[i]=='-'){
				res++;
				for(int j=i;j<i+k;j++)
					s[j] = '+'+'-'-s[j];
			}
		}
		if( count(s.begin(),s.end(),'-') )	cout << "Case #" << id << ": IMPOSSIBLE" << endl;
		else	cout << "Case #" << id << ": " << res << endl;
	}

}