#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>
#define SZ(x) ( (int) (x).size() )
#define me(x,a) memset(x,a,sizeof(x))
#define FN(a,n) for(int a=0;a<n;a++)
#define FOR(a,ini,fin) for(int a=(ini);a<(fin);a++)
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define endl "\n"
#define MOD 1000000007
#define MAXN 1003
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
using namespace std;
string s;
int k;

struct LazyNode{
	bool change;
	LazyNode()
	{
		// neutro
		change = 0;
	}
	void operator +=(const LazyNode &ln)
	{
		change = (change != ln.change); // xor
	}
};

struct Node{
	int cntOnes;
	int si; // size
	
    Node(){
        // neutro:
        cntOnes = 0;
        si = 0;
    }
    
	void operator +=(const LazyNode &ln)
	{
		if (ln.change) {
			cntOnes = si - cntOnes;
		}
	}
	
	Node operator+( const Node &a) const {
		Node c;
		c.si = si + a.si;
		c.cntOnes = cntOnes + a.cntOnes;
	    return c;
	}
};

Node initNode(int i) {
	Node x;
	x.cntOnes = (s[i] == '+');
    x.si = 1;
    return x;
}

class ST{
private:
	Node T[ MAXN * 4 ];
	LazyNode LazyT[ MAXN * 4 ];
	int n;
    void build_tree( int node , int a , int b ){
        LazyT[ node ] = LazyNode();
        if( a == b ){
            T[ node ] = initNode(a);
            return;
        }
        build_tree( ((node<<1) + 1) , a , ((a+b)>>1) );
        build_tree( ((node<<1) + 2) , ((a+b)>>1) + 1  , b );
        T[ node ] = T[ ((node<<1) + 1) ] + T[ ((node<<1) + 2) ];
    }
    void push( int node , int a , int b ){
        T[ node ] += LazyT[ node ];
        if( a != b ){
            LazyT[ node*2 + 1 ] += LazyT[ node ];
			LazyT[ node*2 + 2 ] += LazyT[ node ];
        }
        LazyT[ node ] = LazyNode();
    }
    Node query( int node , int a , int b , int lo , int hi ){
        push( node , a , b );
        if( lo > b || a > hi ) return Node();
        if( a >= lo && hi >= b ) return T[ node ];
        return query( ((node<<1) + 1) , a , ((a+b)>>1) , lo , hi ) + query( ((node<<1) + 2) , ((a+b)>>1) + 1  , b , lo , hi );
    }
    void update( int node , int a , int b , int lo , int hi, const LazyNode& val){
        push( node , a , b );
        if( lo > b || a > hi ) return ;
        if( a >= lo && hi >= b ) {
            LazyT[ node ] = val;
            push( node , a , b );
            return;
        }
        update( ((node<<1) + 1) , a , ((a+b)>>1) , lo , hi , val);
        update( ((node<<1) + 2) , ((a+b)>>1) + 1  , b , lo , hi , val);
        T[ node ] = T[ ((node<<1) + 1) ] + T[ ((node<<1) + 2) ] ;
    }
public:
    ST(){}
    void setSizeAndBuild( int tam ){
        n = tam;
        build_tree( 0 , 0 , n - 1 );
    }
    Node query( int lo , int hi ){
        return query( 0 , 0 , n - 1 , lo , hi );
    }
    void update( int lo , int hi ,const LazyNode& val){
        update( 0 , 0 , n - 1 , lo , hi , val );
    }
}st;

int main() {
	int tc;
	sc(tc);
	FN (itc, tc) {
		cin >> s >> k;
		
		st.setSizeAndBuild(SZ(s));
		LazyNode ln;
		int cnt = 0;
		FN (i, SZ(s) - k + 1) {
			Node node = st.query(i,i);
			
			if (node.cntOnes == 0) {
				ln.change = 1;
				st.update(i, i + k - 1, ln);
				cnt ++;
			}
		}
		
		
		bool pos = (st.query(0, SZ(s) - 1).cntOnes == SZ(s));
		
		printf("Case #%d: ", itc + 1);
		
		if (!pos) puts("IMPOSSIBLE");
		else printf("%d\n", cnt);	
	}
}
