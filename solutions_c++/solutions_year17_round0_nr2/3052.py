#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <queue>
#include <math.h>
#include <set>
#include <map>
#include <climits>
#define INF 0x3f3f3f3f
using namespace std;
typedef long long ll;
int t,k;
int main()
{
    freopen("/Users/zhou_rui/Desktop/B-large.in.txt", "r", stdin);
    freopen("/Users/zhou_rui/Desktop/outt6.txt","w",stdout);
    scanf("%d",&t);
    for(int test= 0;test<t;test++){
        ll n;
        scanf("%lld",&n);
        ll temp = n;
        ll getdigit = n;
        ll base = 1;
        ll lastdigit = 9;
        ll build9 = 0;
        while (getdigit) {
            ll dig = getdigit%10;
            if(dig>lastdigit){
                temp = (getdigit-1)*base+build9;
            }
            
            build9*=10;
            build9+=9;
            lastdigit = (temp/base)%10;
            base*=10;
            getdigit/=10;
        }
        printf("Case #%d: %lld\n",test+1,temp);
    }
    
    
    return 0;
}
