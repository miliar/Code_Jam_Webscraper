
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
		cin >> s;
		int i=1;
		while( i<s.size() ){
			if( s[i]<s[i-1] ){
				for(int j=i-1;j>=0;j--)
					if( j and s[j]>s[j-1] ){
						s[j]--;
						for(int k=j+1;k<s.size();k++)
							s[k] = '9';
						break;
					}
					else if( !j ){
						s[j]--;
						for(int k=j+1;k<s.size();k++)
							s[k] = '9';
						if(s[0]=='0')	s.erase(s.begin());
						break;
					}
				break;
			}
			i++;
		}
		cout << "Case #" << id << ": " << s << endl;
	}

}