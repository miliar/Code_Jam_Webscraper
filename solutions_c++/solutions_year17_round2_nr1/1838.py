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
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#define ll long long
using namespace std;
int main(){
    freopen("A-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,tc=1;
    cin>>t;
    while(t--){
        int d,n,arr[2000][2];
        cin>>d>>n;
        int mini=0;
        for(int i=0; i<n; i++) {
            cin>>arr[i][0]>>arr[i][1];
            double t1=1.0*(d-arr[i][0]);
            double t2=1.0*(d-arr[mini][0]);
            if(t1*arr[mini][1]>t2*arr[i][1]){
                mini=i;
            }
        }
        double t = 1.0*(d-arr[mini][0])/arr[mini][1];
        cout<<fixed<<setprecision(6)<<"Case #"<<tc++<<": "<<d/t<<endl;
    }
}
