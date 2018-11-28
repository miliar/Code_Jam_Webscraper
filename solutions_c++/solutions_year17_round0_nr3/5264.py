#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

typedef pair<int, int> lsrs;

lsrs binarysearch(int len, int iters){
    priority_queue<int> q;
    q.push(len);
    lsrs curAns;
    while (iters--){
        int curLen = q.top(); q.pop();
        int curPos = ceil((float)curLen/2.0)-1;
        //printf("Length: %d\n", curLen);
        //printf("Pos: %d\n", curPos);
        curAns = lsrs(curPos, curLen-curPos-1);
        //printf("Ans: %d %d\n", curPos, curLen-curPos-1);
        if (curLen>1) {
            q.push(curLen-curPos-1);
            q.push(curPos);
        }
    }
    return curAns;
}

lsrs calcLSRS(int len, int pos){
    return lsrs(pos, len-pos-1);
}

int main(){
    int t;
    cin >> t;
    for (int ncase = 1; ncase<=t; ncase++){
        int n, k;
        cin >> n >> k;
        lsrs ans = binarysearch(n, k);
        printf("Case #%d: ", ncase);
        cout << max(ans.first, ans.second) << " " << min(ans.first, ans.second) << endl;
    }
}