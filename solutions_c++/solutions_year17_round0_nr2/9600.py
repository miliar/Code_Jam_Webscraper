#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<int>ve;
string s;
int k = 0;

int main()
{
    #ifdef TooLazy
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif /// TooLazy


    int q;
    cin >> q;
    while(q--) {

            ve.clear();
            cin >> s;
            int n = s.size();

            for(int i=0; i<n; i++) {
                    int a = s[i] - '0';
                    ve.push_back(a);
            }
            for(int m=0; m<n; m++) {
                    for(int i=0; i<n-1; i++) {
                            if(ve[i] > ve[i+1]) {
                                ve[i]--;
                                for(int j=i+1; j<n; j++) {
                                    ve[j] = 9;
                                }
                            }
                    }
            }
            printf("Case #%d: ", ++k);
            for(int i=0; i<n; i++) {
                    if(ve[i] > 0) {
                        cout << ve[i];
                }
            }

            cout << "\n";
    }

    return 0;
}
