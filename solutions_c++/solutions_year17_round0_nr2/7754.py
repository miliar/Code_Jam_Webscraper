#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen ("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);
    int t;
    string s;
    cin>>t;
    for(int tc = 1; tc <= t; tc++){
        cin>>s;
        vector<int> v;
        for(int i = 0 ; i < s.size(); i++){
            v.push_back(s[i] - '0');
        }
        for(int i = 0; i < v.size() - 1; ++i){
            if(v[i] > v[i + 1]){
                v[i]--;
                for(int aux = i + 1; aux < v.size(); aux++){
                    v[aux] = 9;
                }
                i=-1;
            }
        }
        cout<<"Case #"<<tc<<": ";
        for(int i = 0 ; i < v.size(); i++){
            if(v[i] != 0) cout<<v[i];
        }
        cout<<endl;
    }
    return 0;
}
