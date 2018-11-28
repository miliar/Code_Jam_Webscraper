#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>
//#include <time.h>
using namespace std;
#define MAX 105
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define C 0
#define J 1
struct Interval{
	int beg, end, person;
	Interval(int b , int e , int p ) : beg(b) , end(e), person(p){}
	Interval(){}
};

int nC,nJ;
//vector<Interval > v;
vector<pii> vC, vJ;
int main() {
    int t, n, beg,end ;
    scanf("%d", &t) ;
    for( int q = 1 ; q <= t && scanf("%d %d" , &nC, &nJ ) ; ++q ){
		//v = vector<Interval>(nC + nJ, Interval() );
		//v.clear();
		//for( int i = 0 ; i < nC && scanf("%d %d" , &beg, &end ) ; ++i ) v.pb(Interval(beg,end,C));
		//for( int i = 0 ; i < nJ && scanf("%d %d" , &beg, &end ) ; ++i ) v.pb(Interval(beg,end,J));
		
		vC.clear(); vJ.clear();
		int minC = 1<<30, maxC = -1;
		int sumC = 0, sumJ = 0;
		for( int i = 0 ; i < nC && scanf("%d %d" , &beg, &end ) ; ++i ){
			vC.pb(mp(beg,end));
			//minC = min( minC , beg ); maxC = max( maxC , end );
			//sumC += end - beg;
		}

		int minJ = 1<<30, maxJ = -1;
		for( int i = 0 ; i < nJ && scanf("%d %d" , &beg, &end ) ; ++i ){
			vJ.pb(mp(beg,end));
			//minJ = min( minJ , beg ); maxJ = max( maxJ , end );
			//sumJ += end - beg;
		}
		int result = 2;
		sort(vC.begin(), vC.end());
		sort(vJ.begin(), vJ.end());
		if( nJ + nC == 1 ) result = 2;
		else{
		if( nJ == 0 ){
			maxC = max( vC[1].first - vC[0].second, 1440 - vC[1].second + vC[0].first );
			if( maxC < 720) result = 4;
		}else if( nC == 0 ){
			maxJ = max( vJ[1].first - vJ[0].second, 1440 - vJ[1].second + vJ[0].first );
			if( maxJ < 720) result = 4;
		}
		}
        printf("Case #%d: %d\n", q, result );
    }
    return 0 ;
}
