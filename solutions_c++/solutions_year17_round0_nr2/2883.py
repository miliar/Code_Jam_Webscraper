#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int t;
    string s;
    vector<int> v;
    int n;
    char c;
    int digit;
    cin>>t;
    bool flag;
    int start;
    for(int i=1; i<=t; i++){
        cin>>s;
        v.clear();
        n = s.size();
        for(int j=0; j< (int)n; j++){
           c = s[j];
           digit = c - '0';
            v.push_back(digit);
        }

        flag = true;
        digit = v[0];
        start = 0;
        for(int j=0; j<n && flag == true; j++){
            if(v[j] == digit)
                continue;
            if(v[j] > digit){
                digit = v[j];
                start = j;
            } else {
                flag = false;
                v[start] --;
                for(int k = start+1; k<n; k++){
                    v[k] = 9;
                }
            }
        }
        cout<<"Case #"<<i<<": ";
        if(v[0] != 0){
            cout<<v[0];
        }

        for(int j = 1; j < n; j++){
            cout<<v[j];
        }

        cout<<'\n';
    }

    return 0;
}
