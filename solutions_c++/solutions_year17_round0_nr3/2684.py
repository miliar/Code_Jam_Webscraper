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
#include <unordered_map>
//#include <time.h>
using namespace std;
#define MAX 1000005
#define pii pair<long long , long long>
#define mp make_pair
typedef long long LL;

int main() {
	map<LL, LL> counter;
    int t;
	LL n , k;
	LL left, right, left_cnt, right_cnt;
    cin>>t;
    for( int q = 1 ; q <= t && cin>>n>>k ; ++q ){
		right = n/2; left = (n - 1 - right);
        cout<<"Case #"<<q<<": ";
		if( k == 1 ){
			cout<<right<<" "<<left<<endl;
			continue;
		}

		LL nodes = 0;
		int depth = 0;
		for( int i = 0 ; i < 64 ; ++i ){
			nodes += 1LL<<i;
			if( nodes >= n ){
				depth = i;
				break;
			}
		}
		//cout<<endl<<"n "<<n<<" k "<<k<<" nodes "<<nodes<<"  depth "<<depth<<endl;
		left_cnt = nodes - n; left = 0;
		right_cnt = (1LL<<depth) - left_cnt; right = 1;		
		while( true ){		
			if( left_cnt > 0 ){
				counter[left] += left_cnt;
			}
			if( right_cnt > 0 ){
				counter[right] += right_cnt;
			}
			//cout<<left<<","<<left_cnt<<" -- "<<right<<","<<right_cnt<<endl;
			if( left_cnt > 0 && right_cnt > 0 ){
				LL mini = min( left_cnt, right_cnt );
				LL tmp = left + right + 1;
				left_cnt -= mini; right_cnt -= mini;
				if( left_cnt > 0 ){
					left_cnt /= 2;
					left = 2 * left + 1;
					right_cnt = mini; 
					right = tmp;
				}else{
					right_cnt /= 2;
					right = 2 * right + 1;
					left_cnt = mini;
					left = tmp;
				}
			}else if( left_cnt > 0 ){
				left_cnt /= 2;
				left = 2 * left + 1;
			}else if( right_cnt > 0 ){
				right_cnt /= 2;
				right = 2 * right + 1;
			}else break;
		}
		LL sum = 0;
		for(auto it:counter){
			if( it.first > 0 ){
				sum += it.second;
				//cout<<it.first<<": "<<it.second<<endl;
				if( n - sum + 1 <= k ){
					right = it.first/2; left = (it.first - 1 - right);
					cout<<max(left, right)<<" "<<min(left, right)<<endl;
					break;
				}
			}
		}
		counter.clear();
    }
    return 0 ;
}
