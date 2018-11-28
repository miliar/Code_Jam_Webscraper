#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <time.h>
#include <assert.h>
#define MAXN 10000000
using namespace std;

int t;

int get_num_length(long long num){
    int length = 0;
    while(num){
        length++;
        num/=10;
    }
    return length;
}

long long get_largest_tidy(long long num){

    int length = get_num_length(num);
    if (length == 1) {
        return num;
    }
    long long md = 10;
    for(int i=0; i<length; i++){
        long long big_md = md*10;
        long long dr = (num%md)/(md/10);
        long long dl = (num%big_md)/md;
        if(dl > dr){
            num = (num - num%md) - 1;
        }
        md*=10;
    }
    return num;
}


int main(){
    freopen("/Users/Masoud/Desktop/B-large.in", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    int ca = 1;
    scanf("%d", &t);
    while(t--){
        long long num;
        scanf("%lld", &num);
        if (num == 1000000000000000000) {
            printf("Case #%d: %lld\n", ca++, num-1);
        }else{
            printf("Case #%d: %lld\n", ca++, get_largest_tidy(num));
        }
    }
    return 0;
}




