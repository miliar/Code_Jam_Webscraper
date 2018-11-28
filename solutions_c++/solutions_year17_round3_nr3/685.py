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

using namespace std;


int main()
{
    int t;
    cin >> t;
    for(int caso=1; caso<=t; caso++) {
        int n, k;
        cin >> n >> k;
        double u;
        double arr[100];
        cin >> u;
        for(int i=0; i<n; i++) {
            cin >> arr[i];
        }
        sort(arr, arr+n);
        for(int i=0; i<n; i++) {
            if(arr[i]-arr[0] < 1e-6) continue;
            if(i*(arr[i]-arr[0]) < u+1e-6) {
                u -= i*(arr[i]-arr[0]);
                for(int j=0; j<i; j++) arr[j] = arr[i];
            } else {
                for(int j=0; j<i; j++) arr[j] += u/i;
                u = 0.0;
                break;
            }
        }
        if(u > 1e-6) {
            for(int j=0; j<n; j++) arr[j] += u/n;
        }
        double res = 1.0;
        for(int i=0; i<n; i++) res *= arr[i];
        printf("Case #%d: %.8f\n", caso, res);
    }
}
