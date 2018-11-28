
/*
USER: nguyens1
PROG: nocows
LANG: C++
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <limits.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

int main(){
    ifstream fin("C-small-2-attempt0.in");
    ofstream fout("output.txt");
    
    int T;
    int K[101], N[101];
    fin >> T;
    priority_queue<int> q;
    for (int i = 0; i < T; ++i){
        fin >> N[i];
        fin >> K[i];
    }

    // for (int i = 0; i < T; ++i){
    //     cout << i + 1 << " " << N [i] << " " << K[i] << endl;

    // }
    for (int i = 0; i < T; ++i){
        int k = K[i];
        int n = N[i];
        int rem = INT_MIN, tem;
        q = priority_queue <int>();
        for (int j = 1; j <= k; ++j){

            if (!q.empty() && n < q.top()){
                int t = n;
                n = q.top();
                q.pop();
                if (t != 0)
                    q.push(t);
            }

            tem = n;
            n /= 2;
            q.push(tem - (n + 1));
            // cout << tem << " " << rem << endl;
        }
        if (tem != n)
            fout <<"Case #" << i + 1 << ": " << n << " " << tem - (n + 1) << endl;
        else 
            fout <<"Case #" << i + 1 << ": " << n << " " << n << endl;
    }

    return 0;
}