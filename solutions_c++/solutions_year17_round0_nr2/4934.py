
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
        cin >> str;
        n = str.length();
        for(i=0;i<n-1;i++){
            if(str[i]>str[i+1]) break;
        }
        if(i==n-1){
            str1 = str;
            cout << "Case #"<<a++<<": "<<str1<<endl;
            str.clear();
            str1.clear();
            continue;
        }
        if(str[i]=='0'||str[i]=='1'){
            for(j=0;j<i;j++) str1+='9';
        }
        else if(i==0){
            str1+=(str[i]-1);
        }
        else{
            char ch = str[i];
            if(str[i-1]==ch){
                for(j=i-1;j>=0&&str[j]==ch;j--){
                    str1+='9';
                }
                str1+=ch-1;
                for(j=j;j>=0;j--){
                    str1+=str[j];
                }
            }
            else{
                str1+=str[i]-1;
                for(j=i-1;j>=0;j--){
                    str1+=str[j];
                }
            }
            reverse(str1.begin(), str1.end());
        }
        for(i=i+1;i<n;i++){
            str1+='9';
        }
        cout << "Case #"<<a++<<": "<<str1<<endl;
        str.clear();
        str1.clear();
    }
    return 0;
}















