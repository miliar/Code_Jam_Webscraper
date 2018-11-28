
#include <cstring>
#include <string.h>
#include <map>
#include <unordered_map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

#define fill2d(arr, val) std::fill(&arr[0][0],&arr[0][0] + sizeof(arr)/ sizeof(arr[0][0]),val);
#define fill1d(arr, val) std::fill(&arr[0],&arr[0] + sizeof(arr)/ sizeof(arr[0]),val);


using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i, m) for(int i=0;i<(int)(m);i++)
#define rep2(i, n, m) for(int i=n;i<(int)(m);i++)
#define For(it, c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define set(a, b) memset(a,b,sizeof(a))
typedef stringstream ss;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vvii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;

typedef unsigned long long ull;
int T;
int curr = 1;
ull N = 0;

vector<int> number;
void good() {
    if(number.size() == 1){
        return;
    }
    ull lastDigit = number[number.size()-1];
    ull curr;

    for(int i = number.size() - 2; i >= 0; i--){
        curr = number[i];
        if(lastDigit < curr){
            int lastDigitIndex = i + 1;
            number[i]--;
            rep2(j,lastDigitIndex,number.size()){
                number[j] = 9;
            }

        }
        lastDigit = number[i];
    }


}

// do a zig zag through the numbers
int main() {
    freopen("tidynumbers/B-large.in", "r", stdin);

    cin >> T;
    while (T--) {
        cin >> N;

        number.clear();
        while(N){
            int curr = N % 10;
            N/=10;
            number.push_back(curr);
        }
        reverse(number.begin(),number.end());
        good();
        printf("Case #%d: ", curr++);
        rep(i,number.size()){
            if(i == 0 && number[i] == 0){

            }else {
                printf("%d", number[i]);
            }
        }

        if(T != 0) {
            printf("\n");
        }

    }

    return 0;
}