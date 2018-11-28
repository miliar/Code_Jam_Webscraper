/*
    *
    * Cyrus Jackson
    * VIT University - India
    *
*/
#define TCase(k) cout<<"Case #"<<(int)k+1<<": ";
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory.h>
#include <cassert>
#include <stdio.h>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <functional>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <time.h>
#include <stack>
#include <set>
#define cl1 double _time=clock();
#define cl2 cout<<"time: "<<double(clock()-_time);
#define BO ios_base::sync_with_stdio(false); cin.tie(NULL)
#define fi BO;freopen("in.txt","r",stdin);
#define fo freopen("out.txt", "w", stdout);
#define test()    int test_case;cin>>test_case;while(test_case--)
 
#define forR(i,n) for (int i = n; i --> 0; )
#define forO(i,n) for(int i = 1; i <= n; i++)
#define forN(i,n) for(int i = 0; i < n; i++)
#define forA(i,a,n) for(int i = a; i < n; i++)
#define s(t) scanf("%d",&t)

#define fill(t) memset(t,0,sizeof(t));
typedef long long int ll;
int GCD(int A, int B) {    if(B==0)        return A;    else        return GCD(B, A % B); }

int MOD = 1e9 + 7;
const int INF = 1<<29;
#define MAX 11111
using namespace std;


int main(){
  fi;fo;
  int testCase = 0;
    test(){
        string s;
        cin>>s;
        int n = s.length(), t,pl = 0;
        cin>>t;
        int ans = 0;
        forN(i,n-t+1){
            if(s[i] == '-'){
            ans++;
            forA(j,i,i+t){
                if(s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
            }
        }
        END:;
        forN(i,n){
            if(s[i] == '+') pl++;
            else break;
        }
        TCase(testCase);
        if(pl != n)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<ans<<endl;
        testCase++;
    }
    return 0;
}
