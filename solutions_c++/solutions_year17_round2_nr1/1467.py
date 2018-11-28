#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;


struct node{long long x,y;}a[10001];


bool cmp(node a, node b){
    if(a.x * b.y < a.y * b.x) return true;
    else return false;
}


int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int r=0;r<T;r++){
        long long d, n;
        cin >> d >> n;
        
        for(int i=0;i<n;i++){
            long long s,v;
            cin >> s >> v;
            a[i].x = (s*v +d*v-s*v);
            a[i].y = (d-s);
        }
        
        sort(a, a+n, cmp);
        double q = a[0].x * 1.0;
        q /= a[0].y;
        printf("Case #%d: %.6lf\n",r+1, q);
     //   cout << "Case #" << r+1 << ": " << q << endl;

    }
    return 0;
}
