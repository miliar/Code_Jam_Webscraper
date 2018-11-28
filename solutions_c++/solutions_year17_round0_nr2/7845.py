#include<iostream>
#include<string>
#include<cstdlib>
using namespace std;

string solve(string s){
    if(s.size() == 1){
        return s;
    } else {
        int ind=0;
        char c=s[0];
        for(int i=1;i<s.size();i++){
            if(s[i]>c){
                c=s[i];
                ind=i;
            } else if(s[i]<c){
                s[ind]=s[ind]-1;
                for(int j=ind+1;j<s.size();j++){
                    s[j] = '9';
                }
            }
        }
    }

    return s;
}

int main(){
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        string res = solve(s);
        res.erase(0, res.find_first_not_of('0'));
        cout << "Case #" << i+1 << ": " << res << endl;
    }
}
