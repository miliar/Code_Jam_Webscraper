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
#define MAX 1005
#define pii pair<long long , long long>
#define mp make_pair

int main() {
    int t, result, k;
    scanf("%d", &t) ;
	string s;
    for( int q = 1 ; q <= t && cin>>s>>k ; ++q ){
        result = 0;
        for( int i = 0 ; i <= s.size() - k ; ++i ){
        	if( s[i] == '-' ){
            	result++;
                for( int j = 0 ; j < k ; ++j ){
					if( s[i + j] == '-' )
						s[i + j] = '+';
					else
						s[i + j] = '-';
                }
            }
        }
		bool possible = true;
		for( int i = 0 ; i < s.size() ; ++i ){
			if( s[i] == '-'){
				possible = false;
				break;
			}
		}

        printf("Case #%d: ", q );

		if( possible ) printf("%d\n", result);
		else printf("IMPOSSIBLE\n");

    }
    return 0 ;
}
