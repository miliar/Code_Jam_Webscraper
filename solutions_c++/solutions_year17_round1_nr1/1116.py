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
#include <unordered_set>
#include <unordered_map>
//#include <time.h>
using namespace std;
#define MAX 50
string s[ MAX ];
int main() {
    int t, n, h, w ;
    scanf("%d", &t) ;
    for( int q = 1 ; q <= t && scanf("%d %d" , &h, &w ) ; ++q ){
		
		for( int i = 0 ; i < h && cin>>s[i] ; ++i );


		for( int i = 0 ; i < w ; ++i ){
			//bool seen = false;
			for( int j = 0 ; j < h ; ++j ){
				if( s[j][i] != '?'){
					//seen = true;
					for( int k = j - 1 ; k >= 0 && s[k][i] == '?' ; --k ){
						s[k][i] = s[j][i];
					}
					for( int k = j + 1 ; k < h && s[k][i] == '?' ; --k ){
						s[k][i] = s[j][i];
					}
				}
			}
		}

		for( int i = 0 ; i < h ; ++i ){
			for( int j = 0 ; j < w ; ++j ){
				if( s[i][j] != '?'){
					for( int k = j - 1 ; k >= 0 && s[i][k] == '?' ; --k ){
						s[i][k] = s[i][j];
					}
					for( int k = j + 1 ; k < w && s[i][k] == '?' ; --k ){
						s[i][k] = s[i][j];
					}
				}
			}
		}



        printf("Case #%d: \n", q );

		for( int i = 0 ; i < h ; ++i ){
			cout<<s[i]<<endl;			
		}

    }
    return 0 ;
}
