/*
Author @kbstudios
Kaushal Bhogale GCJ 2017
*/
#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <utility>
#include <string>
#include <cctype>
#include <cmath>

using namespace std;

#define end '\n'

typedef long long ll;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const int mod=1000000007;

#define rep(i,n) for(auto i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9

#define testcase(t) int tc;cin >> tc;for(int t=1; t<=tc; t++)
#define out(result) cout << "Case #" << t << ": " << result << end;cerr << "Case #" << t << ": " << result << end;
#define outT(result) cout << "Case #" << t << ": " << result << end;

int main()
{
    //ios::sync_with_stdio(false);

    #ifndef ONLINE_JUDGE
    // For getting input from input.txt file
    freopen("B-large.in", "r", stdin);
    // Printing the Output to output.txt file
    freopen("B-large.out", "w", stdout);
    #endif
    testcase(t){
        string num;

        cin>>num;
        int n =(int)num.length();
        int arr[n];

        for(int i=0; i<n; i++){
            arr[i] = num[i] - '0';
        }

        while(true){
            int smaller = arr[0];
            int i;
            for(i=1; i<n; i++){
                if(arr[i] >= smaller){
                    smaller = arr[i];
                }
                else{
                    arr[i-1] -= 1;
                    for(int j = i; j<n; j++) arr[j] = 9;
                    break;
                }
            }
            if(i == n){
                break;
            }
        }

        cout << "Case #" << t << ": ";
        cerr << "Case #" << t << ": ";
        if(arr[0] != 0){
            cout << arr[0];
            cerr << arr[0];
        }
        for(int i = 1; i<n; i++){
            cout << arr[i];
            cerr << arr[i];
        }
        cout << end;
        cerr << end;
    }

    return 0;
}

