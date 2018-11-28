/*************************************************************************
	> File Name: main.cpp
	> Author: cxlove
	> Mail: cxlove321@gmail.com
	> Created Time: 六  4/ 8 20:01:09 2017
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, cas = 0;
    cin >> t;
    while (t --) {
        int n , k;
        cin >> n >> k;
        priority_queue<int> que;
        que.push(n);
        cout << "Case #" << ++ cas << ": ";
        for(int i = 0 ; i < k ; i ++) {
            int now = que.top();que.pop();
            int A = (now - 1) / 2;
            int B = (now - 1) - A;
           // cout << now << " " << A << " " << B << endl;
            if(A < B) swap(A , B);
            if(A) que.push(A);
            if(B) que.push(B);
            if(i == k - 1) {
                cout << A << " " << B << endl;
            }
        }
    }

    return 0;
}

