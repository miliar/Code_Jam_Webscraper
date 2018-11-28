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
#define MAX 20

unsigned long long convertToNumber(vector<int> &value){
	unsigned long long result = 0;
	for( int i = value.size() - 1 ; i >= 0 ; --i ){
		result = result * 10 + value[i];
	}
	return result;
}

int main() {
    int t;
    long long n;
	unsigned long long result;
	vector<int> value;
	cin>>t;
    for( int q = 1 ; q <= t && cin>>n ; ++q ){
		result = 0;
		value = vector<int>(MAX, 0);
		while( result < n ){
			for( int i = 0 ; i < value.size() ; ++i ){
				if( value[i] < 9 ){
					value[i]++;
					if( convertToNumber(value) > n ){
						value[i]--;
						break;
					}
				}else{
					goto end;
				}
			}
			result = convertToNumber(value);
		}
		end:
        cout<<"Case #"<<q<<": "<<result<<endl;
    }
    return 0 ;
}
