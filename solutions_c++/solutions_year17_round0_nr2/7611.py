#include <bits/stdc++.h>

using namespace std;

string res(string n)
{
    bool end;
    do {
        end = true;
        for(uint i = 0; i < n.size()-1; i++) {
            if(n[i] > n[i+1]){
                end = false;
                for(uint j = i+1; j < n.size(); j++) {
                    n[j] = '9';
                }
                if(n[i] == '0') n[i] = '9';
                else n[i]--;
                // cout << n << endl;
            }
        }
    } while(!end);

    return n;
}

void strip0(string& s)
{
    int i = 0;
    while(s[i] == '0') i++;
    s = s.substr(i,s.size());
}

int main()
{
    int t;
    string n;
    cin >> t;
    for(int i = 1; i <= t; i++){
        cin >> n;
        n = res(n);
        strip0(n);
        printf("Case #%d: %s\n", i, n.c_str());
    }
    return 0;
}
