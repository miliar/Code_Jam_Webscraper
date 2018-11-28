#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> result;
    for(int i = 1; i <= n; i++) {
        int k;
        string s;
        cin>>s>>k;
        int count = 0;
        bool done = true;
        while(s.length() != 0) {
            if(s.length() < k && s[0] == '-') {
                done = false;
                break;
            }
            if(s[0] == '-') {
                count++;
                for(int j = 0; j < k; j++) {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
            s.erase(s.begin());
        }
        if(done)
            result.push_back("Case #"+to_string(i)+": "+to_string(count));
        else
            result.push_back("Case #"+to_string(i)+": IMPOSSIBLE");
    }
    for(auto i:result)
        cout<<i<<endl;
    return 0;
}
