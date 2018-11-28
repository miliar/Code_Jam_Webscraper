#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e3 + 10;

int main() {
    #ifdef LOCAL_DEBUG
        freopen("data.in", "r", stdin);
        freopen("data.out", "w", stdout);
    #endif

    cin.tie();
    ios_base::sync_with_stdio(0);
	#define endl '\n'
    int T; cin >> T;
    for(int tt = 1; tt <= T; tt++){
    	cout << "Case #" << tt << ": ";
    	string num; cin >> num;
    	for(int i = 0; i < (int)num.length() - 1; i++){
    		if(num[i] > num[i + 1]){
    			int equal = 0;
    			for(int j = i; j >= 0; j--){
    				if(num[i] == num[j])equal++;
    				else break;
    			}
    			num[i - equal + 1] -= 1;
    			for(int j =i - equal + 2; j < (int)num.length(); j++ )
    				num[j] = '9';

    		}
    	}
    	if(num[0] == '0')num = num.substr(1, num.size());
    	cout << num << endl;

    }


}

