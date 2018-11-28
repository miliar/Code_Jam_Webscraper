#include <bits/stdc++.h>

using namespace std;
void change(string &s);
bool found(string s);
int main()
{
    freopen("B-large.in" , "r" ,stdin);
    freopen("output.txt" , "w" ,stdout);
    int t;
    cin>>t;
    for(int i = 0 ; i < t ;i++){
        string s;
        cin>>s;
        while(found(s)){
            change(s);
        }
        if(s.at(0) == '0'){
            s.erase(s.begin());
        }
        cout << "Case #"<<i+1<<": "<<s<<"\n";
    }
    return 0;
}
void change(string &s){
    for(int i = 1 ; i < s.size() ; i++){
        if(s.at(i-1)>s.at(i)){
            s.at(i-1) -= 1;
            for(int x = i ; x< s.size();x++){
                s.at(x) = '9';
            }
            break;
        }
    }
}
bool found(string s){
    for(int i = 1 ; i < s.size() ; i++){
        if(s.at(i-1) > s.at(i)){
            return true;
        }
    }
    return false;
}
