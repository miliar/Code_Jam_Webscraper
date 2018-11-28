#include<iostream>
#include<string>

using namespace std;

int main() {
    int cases;
    cin>>cases;
    for(int cas = 0; cas < cases; ++cas) {
        cout << "Case #"<< cas+1 << ": ";
        string s;
        cin>> s;
        int k;
        cin>> k;
        int c = 0;
        for(int i = 0; i < s.size() -k + 1; ++i) {
            c++;
            if(s[i] == '-') for(int j = i; j < i + k; ++j) s[j] = (s[j]=='+' ? '-' : '+');
            else c--;
        }
        for(int i = s.size() - k;i < s.size(); ++i) if (s[i] == '-') c = -1;
        if (c ==-1) cout << "IMPOSSIBLE" << endl;
        else cout << c <<endl;
    }
}
