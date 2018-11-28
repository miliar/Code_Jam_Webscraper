#include <iostream>
#include <string>
#include <queue>
#include <vector>
using namespace std;


int to[2][2] = {{0, -1}, {-1, 0}};
int dp[16][16];
int  n, r, c;
string a;
int b;


int main() {
    int T;
    cin>>T;
    int case_number = 1;
    while(T--)
    {
        cin>>a;
        for (int i = 0 ; i < a.length()-1; i++) {
            if (a[i] <= a[i+1]) {
                continue;
            } else {
                for (int j = i+1; j < a.length();j++) {
                    a[j] = '9';
                }
                a[i]--;
            }
            i = -1;
        }
        
        
        cout<<"Case #"<<case_number++<<": ";
        int i;
        for (i = 0; i < a.length(); i++) {
            if(a[i] != '0') {
                break;
            }
        }
        while(i < a.length()) {
            cout<<a[i];
            i++;
        }
        cout<<endl;
    }
}
