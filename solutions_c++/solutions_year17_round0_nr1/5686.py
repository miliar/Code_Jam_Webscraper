
#include <cstring>
#include <string.h>
#include <map>
#include <unordered_map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

#define fill2d(arr,val) std::fill(&arr[0][0],&arr[0][0] + sizeof(arr)/ sizeof(arr[0][0]),val);
#define fill1d(arr,val) std::fill(&arr[0],&arr[0] + sizeof(arr)/ sizeof(arr[0]),val);


using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define set(a,b) memset(a,b,sizeof(a))
typedef stringstream ss;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vvii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
int T;
int S;
int currMin;
int currCase = 0;
string curr;
// represents 12 1's
int states[(2<<12)-1];
ll kToTheC;
/*
 * 3
---+-++- 3
+++++ 4
-+-+- 4
 */
bool isValidFlip(const string & pStack,int index){

    bool leftValid = index == 0 ? true : pStack[index] != pStack[index-1];
    bool rightValid = index+S >= pStack.size() ? true : pStack[index+S] != pStack[index+S-1];
    return leftValid && rightValid;
}
bool isValidStack(int val){
    rep(i,S){
        if(!(1<<i & val)){
            return false;
        }
    }
    return true;
}
bool isAllUnhappy(const string & pStack){
    rep(i,pStack.size()){
        if(pStack[i] != '-'){
            return false;
        }
    }
    return true;
}
int getBinRep(string s){
    int toReturn = 0;
    rep(i,s.size()){
        toReturn*=2;
        toReturn += s[i] == '+' ? 1 : 0;
    }
    return toReturn;
}
int flipStarting(int value,int here){
    // remember i is the left index
    // 1000010
    // if i == 0 and goes to 3
    // 1000101
    rep2(i,here,here+S){
        value ^= (1 << i);
    }
    return value;
}
int flips(int value,int minSoFar){
    rep(i,curr.size() - (S-1)){
        int flipVal = flipStarting(value,i);
        if(states[flipVal] == -1){
            states[flipVal] = minSoFar + 1;
            flips(flipVal,minSoFar+1);
        }else if(states[flipVal] > minSoFar + 1){
            states[flipVal] = minSoFar +1;
            // recalculate
            flips(flipVal,minSoFar+1);
        }
    }
    return states[value];
}
///home/devsquad/CLionProjects/gcj2017/oversizedpancake
int main(){
    freopen("oversizedpancake/small.txt","r",stdin);
    cin >> T;
    while(T--){
        currMin = -1;
        curr.resize(1050);
        cin >> curr; cin >> S;
        int representation = getBinRep(curr);
        int startVal = 0;
        rep(i,curr.size()){
            startVal <<= 1;
            startVal+=1;
        }
        rep(i,(2<<12)-1){
            states[i] = -1;
        }
        states[startVal] = 0;
        flips(startVal,0);
        currCase+=1;
        if(states[representation]== -1){
            printf("Case #%d: IMPOSSIBLE\n", currCase);
        }else {
            printf("Case #%d: %d\n", currCase, states[representation]);
        }
    }

    return 0;

}