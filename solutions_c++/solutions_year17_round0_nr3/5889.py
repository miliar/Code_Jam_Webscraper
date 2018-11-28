
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
#include <langinfo.h>

#define fill2d(arr, val) std::fill(&arr[0][0],&arr[0][0] + sizeof(arr)/ sizeof(arr[0][0]),val);
#define fill1d(arr, val) std::fill(&arr[0],&arr[0] + sizeof(arr)/ sizeof(arr[0]),val);


using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i, m) for(int i=0;i<(int)(m);i++)
#define rep2(i, n, m) for(int i=n;i<(int)(m);i++)
#define For(it, c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define set(a, b) memset(a,b,sizeof(a))
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

int T,N,K;
int currCase = 1;

//999999 475712
const int maxIndex = (1 << 11) * 2 * 1000;
ii data[maxIndex];


void buildTree(int level,int left, int right){
    if(left > right){
        return;
    }
    int mid = left +  (right-left)/2;

    int theMin = min(mid-left,right-(mid));
    int theMax = max(mid-left,right-(mid));
    data[level] = {theMax,theMin};
    data[level].first = max(0,data[level].first);
    data[level].second = max(0,data[level].second);
    buildTree(level * 2 + 1,left,mid-1);
    buildTree(level * 2 + 2,mid+1,right);
}

ii findLocation(int searchingFor){
    struct Trip{
        int first,second,third;
    };
    auto cmp = [](const Trip & left, const Trip & right){
        if(left.first > right.first){
            return false;
        }else if(left.first == right.first && left.second >= right.second){
            return false;
        }
        return true;
    };
    priority_queue<Trip,vector<Trip>,decltype(cmp)> pq(cmp);
    pq.push({data[0].first,data[0].second,0});
    vector<Trip> orderedList;

    while(orderedList.size() < searchingFor){
        Trip top = {pq.top().first,pq.top().second,pq.top().third};
        pq.pop();
        orderedList.push_back(top);
        if(top.third * 2 + 1 >= 2 * N){
            continue; // dont add children they will be oob
        }
        ii left = data[top.third *2 +1];
        ii right = data[top.third *2 +2];
        pq.push({left.first,left.second,top.third* 2 + 1});
        pq.push({right.first,right.second,top.third * 2 + 2});
    }
    Trip toReturn = orderedList[searchingFor-1];
    return ii{toReturn.first,toReturn.second};
}
int main() {
    freopen("bathroomstalls/small.in", "r", stdin);
    cin >> T;
    set(data,0);
    while(T--){

        cin >> N;
        cin >> K;
        rep(i,2*N){
            data[i] = {-1,-1};
        }
        int mid =  (N-1)/2;
        // always inclusive
        // | 0 0 |
        //
        int theMin = min(mid,N-(mid+1));
        int theMax = max(mid,N-(mid+1));
        data[0] = {theMax,theMin};
        buildTree(1,0,mid-1);
        buildTree(2,mid+1,N-1);
//        ii = findLocation(2);
        ii index = findLocation(K);


        printf("Case #%d: %d %d\n",currCase,index.first,index.second);

        currCase++;
    }

    return 0;

}