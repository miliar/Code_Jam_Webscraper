#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define For(i,N) for(int i=0; i<N; i++)
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

void solve(){   
    string s;
    int k;

    cin >> s >> k;

    int flips = 0;
    for(int i=0; i<s.size(); i++) if(s[i] == '-') {
        flips++;

        for(int j=i; j<i+k; j++){
            if (j >= s.size()){
                printf("IMPOSSIBLE\n");
                return;
            }
            if (s[j] == '-') s[j] = '+';
            else s[j] = '-';
        }
    }

    printf("%d\n", flips);
}

int main(){
  int T;
  scanf(" %d", &T);
  For(t,T){
    printf("Case #%d: ",t+1);
    solve();
  }
  return 0;
}