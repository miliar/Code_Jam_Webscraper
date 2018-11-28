#include <iostream>
#include <cstdio>

#define For(i, n) for(int i = 0; i < (n); i++)

using namespace std;

int main () {   
    ios::sync_with_stdio(0);

    int t;
    cin >> t;

    For (i, t) {
        string s;
        cin >> s;
        
        s += "9";

        string res = "";
        For (j, (int)s.size() - 1) {
            if (s[j + 1] < s[j]) {
                if (s[j] > '1') {
                    res += s[j] - 1; 
                    int firstPos = j;
                    string tmpRes = "";

                    For (l, j + 1) {
                        if (res[l] <= s[j] - 1)
                            tmpRes += res[l];
                        else
                        {
                            firstPos = l;
                            tmpRes += s[j] - 1;
                            break;
                        }
                    }
                    
                    for (int l = firstPos + 1; l < (int)s.size() - 1; l++)
                        tmpRes += "9";

                    res = tmpRes;
                }
                else {
                    res = "";
                    For (l, (int)s.size() - 2)
                        res += "9";
                }
                break;
            }
            else
                res += s[j];
        }

        cout << "Case #" << i + 1 << ": " << res << "\n";
    }
}