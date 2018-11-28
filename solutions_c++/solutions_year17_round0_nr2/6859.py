#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 1e5 + 5;
ll a[N];

int main() {
	//ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
	/*freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);*/
	int t, l = 0;
	cin >> t;
	while(t--) {
        string s;
        cin >> s;
        for(int i = s.size() - 1; i > 0; i--) {
            if(s[i] < s[i - 1]) {
                s[i - 1]--;
                for(int j = i; j < s.size(); j++) {
                    s[j] = '9';
                }
            }
        }
        cout << "Case #" << ++l << ": ";
        int i = 0;
        while(i < s.size() - 1 && s[i] == '0') {
            i++;
        }
        for(; i < s.size(); i++) {
            cout << s[i];
        }
        cout << "\n";
	}
}
