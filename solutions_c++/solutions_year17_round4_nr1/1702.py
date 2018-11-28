#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

int solve(){
    int N, P;
    cin >> N >> P;
    vector<int> divs = vector<int>(P, 0);
    while (N--){
        int g;
        cin >> g;
        divs[g%P]++;
    }
    int res = 0;
    if (P == 2){
        res += divs[0];
        res += divs[1]/2;
        if (divs[1] % 2 == 1)
            res++;
    } else if (P == 3){
        res += divs[0];
        int m = min(divs[1], divs[2]);
        res += m;
        divs[1] -= m;
        divs[2] -= m;
        int rest = divs[1]+divs[2];
        res += rest/3;
        if (rest % 3 != 0)
            res++;
    } else if (P==4){
        res += divs[0];
        res += divs[2]/2;
        divs[2] %= 2;
        int m = min(divs[1], divs[3]);
        res += m;
        divs[1] -= m; divs[3] -= m;
        int rem = divs[1] + divs[3];
        if (divs[2] == 1 && rem >= 2){
            res++;
            rem -= 2;
        } else if (divs[2] == 1 && rem < 2){
            res++;
        } else {
            res += rem / 4;
            if (rem % 4 != 0)
                res++;
        }
    }
    return res;
}
        
	

int main(){
    int T;
    cin >> T;
	for (int i=1; i<=T; i++){
		cout << "Case #" << i << ": " << solve() << endl;
	}
}
