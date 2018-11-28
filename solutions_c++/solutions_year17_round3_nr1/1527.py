
/////////////////////////////////////////////////////////////////////////
//.....................................................................//
////////////jasper_skywalker___fsociety()___BUET_mashroom////////////////
//.....................................................................//
/////////////////////////////////////////////////////////////////////////

#include <map>
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

vector <pair <double, long long> > xy;
vector <pair <double, long long> > cd;
vector <pair <long long, pair <double, double> > > ab;
vector <long long> x;
vector <long long> y;

string str, str1, str2;

long long ara[200005];

long long gcd(long long a, long long b){
    if(a%b==0) return b;
    return gcd(b, a%b);
}

//____________________________________________________________________________________//
//____________________________________________________//
//____________________________________________________________________________________/

bool compare2(pair <long long, long long> i, pair <long long, long long> j){
    return (i.first>j.first);
}

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    long long int n, ans, temp, t, j, i, m, h, h2, m2, c, a, b, mx, k;
    double red, hig, sur, dil, fsur;
    cin >> t;
    j = 1;
    while(t--){
        cin >> n >> k;
        for(i=0;i<n;i++){
            cin >> red >> hig;
            xy.push_back({red*hig, i});
            ab.push_back({i, {red, hig}});
            cd.push_back({red*hig, i});
        }
        sort(xy.begin(), xy.end());
        reverse(xy.begin(), xy.end());
        sur = 0;
        memset(ara, 0, sizeof ara);
        for(i=0;i<k;i++){
            sur+=xy[i].first*2*acos(-1);
            ara[xy[i].second] = 1;
        }
        dil = xy[i-1].first*2*acos(-1);
        fsur = sur;
        for(i=0;i<n;i++){
            if(ara[ab[i].first]==1){
                fsur = max(sur+ab[i].second.first*ab[i].second.first*acos(-1), fsur);
            }
            else{
                fsur = max(sur+ab[i].second.first*ab[i].second.first*acos(-1)-dil+cd[i].first*2*acos(-1), fsur);
            }
        }
        printf("Case #%lld: %.9lf\n", j++, fsur);
        xy.clear();
        ab.clear();
        cd.clear();
    }
    return 0;
}















