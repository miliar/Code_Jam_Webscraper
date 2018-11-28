
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

vector <pair <long long, long long> > xy;
vector <pair <long long, long long> > ab;
vector <long long> x;
vector <long long> y;

string str, str1, str2;

long long ara[200005];

bool compare(pair <long long, long long> i, pair <long long, long long> j){
    return (i.first<j.first);
}

bool compare2(pair <long long, long long> i, pair <long long, long long> j){
    return (i.first>j.first);
}

long long gcd(long long a, long long b){
    if(a%b==0) return b;
    return gcd(b, a%b);
}

//____________________________________________________________________________________//
//____________________________________________________//
//____________________________________________________________________________________//


int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    long long int n, ans, temp, t, j, i, m, h, h2, m2, c, a, b, mx, k;
    cin >> t;
    a = 1;
    while(t--){
        cin >> str >> k;
        n = str.length();
        ans = 0;
        for(i=0;i<=n-k;i++){
            if(str[i]=='-'){
                ans++;
                for(j=i;j<i+k;j++){
                    if(str[j]=='-') str[j] = '+';
                    else str[j] = '-';
                }
            }
        }
        for(i=n-1;i>=k-1;i--){
            if(str[i]=='-'){
                ans++;
                for(j=i;j>i-k;j--){
                    if(str[j]=='-') str[j] = '+';
                    else str[j] = '-';
                }
            }
        }
        //cout << str << endl;
        bool flag = true;
        for(i=0;i<n;i++){
            if(str[i]=='-') flag = false;
        }
        cout << "Case #"<<a++<<": ";
        if(flag) cout << ans <<endl;
        else cout << "IMPOSSIBLE" <<endl;
    }
    return 0;
}















