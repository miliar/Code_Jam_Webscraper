#include<iostream>
#include <cstdio>      
#include <cstdlib>     
#include <ctime>       
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>

using namespace std;

typedef long long ll;

string str;

string getMinimumTidyNumber(string s) {

    int n = s.length();

    ll num = 0;
    ll mi = 0;
    for(int i=0; i<n; i++) {
        num = 10*num + (ll)(s[i] - '0');
        mi = 10*mi + 1;
    }

    if (num < mi) {
        string res = "";
        for(int i = 0; i<n-1; i++) {
            res = res + '9';
        }

        return res;
    }

    for(int i=0; i+1<n; i++) {
        if (s[i] > s[i+1]) {
            string res = "";

            int u = i;
            while (u > 0 && s[u] == s[u-1]) {
                u--;
            }

            for(int j=0; j<u; j++) {
                res = res + s[j];
            }

            res = res + (char)(((int)(s[u] - '0') - 1) + '0');
            
            for(int j=u+1; j<n; j++) {
                res = res + '9';
            }

            return res;
        }
    }

    return s;
}

int main() {

    std::ios::sync_with_stdio(false);
	freopen("b-large-in.txt", "r", stdin);
	freopen("b-large-out.txt", "w", stdout);

    int test;
    cin >> test;

    for(int t=1; t<=test; t++) {
    	cin >> str;

        cout << "Case #" << t << ": " << getMinimumTidyNumber(str) << endl;
    }

    return 0;
}