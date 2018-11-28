#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <stack>
#include <ctime>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <cassert>
#include<iomanip>
using namespace std;
 
int main(int argc, char const *argv[])
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout<<"Case #"<<i+1<<":"<<" ";
        double dist, num;
        double min = 0;
        cin >> dist >> num;
        for (int j = 0; j < num; j++) {
            double pos, speed;
            cin >> pos >> speed;
            double calc = (dist - pos) / speed;
            if (calc > min) {
                min = calc;
            }
        }
        cout << setprecision(6) << fixed << dist / min << endl;
    }
    return 0;
}