//bismillahir rahmanir raheem

#include <string>
#include <vector>
#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<math.h>
#include<string.h>
#include <stdlib.h>
#include<map>
#include<queue>
#include<stack>
#include<utility>
#include<stdlib.h>
#include<string>
#include<set>
#include<iomanip>
#define lld long long int
#define CLR(a) memset(a,0,sizeof(a))
#define RESET(a) memset(a,-1,sizeof(a))
#define act(a) memset(a,1,sizeof(a))
#define setinf(a) memset(a,0b01111111,sizeof(a));
#define FRO freopen("/Users/sheikahm/Contests/General/General/B-large.in","r",stdin);
#define FROF(a) freopen(a,"r",stdin);
#define FROut freopen("/Users/sheikahm/Contests/General/General/B-Large-output.txt","w",stdout);
#define ui unsigned int
#define came "came"
#define pii pair<int,int>
#define plii pair<long long int, int>
#define pll pair<long long,long long>
#define pic pair<int,char>
#define ninf (-1e9)-2
#define inf (1e9)+2
#include<fstream>
#include <assert.h>
#include <bitset>
#include <unordered_map>
#define foreach(x) for(__typeof(x.begin()) it=x.begin(); it!=x.end();it++)

using namespace std;
#define pid pair<int,double>
#define pdi pair<double,int>

#define PB push_back
#define MP make_pair
#define pri(x) printf("%d\n",x)
#define F first
#define S second
#define vit vector<int>::iterator

lld memo[20][10][2];
bool visited[20][10][2];
lld numDigit[20];
lld numFactor[20];
char arr[20];
int ln;

lld dp(int indx, int lastBigDigit, bool limitedBy) {
    if(indx == ln) {
        return 0;
    } else if(visited[indx][lastBigDigit][limitedBy]) {
        return memo[indx][lastBigDigit][limitedBy];
    } else {
        lld &ret = memo[indx][lastBigDigit][limitedBy];
        visited[indx][lastBigDigit][limitedBy] = true;
        ret = - 1;
        if(limitedBy) {
            lld i;
            
            for(i = lastBigDigit; i<= numDigit[indx]; i++) {
                lld v = dp(indx + 1, i,
                           numDigit[indx] == i);
                if(v == -1) {
                    continue;
                }
                lld val = i * numFactor[indx] + v;
                ret = max(ret, val);
            }
        } else {
            lld i;
            for(i = lastBigDigit; i<= 9; i++) {
                lld v = dp(indx + 1, i, false);
                if(v == -1) continue;
                ret = max(ret, i * numFactor[indx] + v);
            }
        }
        return ret;
    }
}

int main() {
    FRO
    FROut
    int t, ca;
    scanf("%d",&t);
    for(ca = 1; ca <= t; ca++) {
        scanf("%s", arr);
        ln = (int) strlen(arr);
        int i, j;
        for(i = 0; i < ln; i++) {
            numDigit[i] = (arr[i] - '0');
            numFactor[i] = pow(10, ln -1 - i);
        }
        RESET(memo);
        CLR(visited);
        lld value = dp(0, 0, true);
        printf("Case #%d: %lld\n", ca, value);
    }
    return 0;
}
