#include <iostream>
#include <queue>
#include <set>
using namespace std;
string flip(string s,int a,int b){

    for(int i =a;i<a+b;i++){
        if(s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    return s;

}
bool chk(string& s){

    for(int i = 0;i<s.length();i++){
        if(s[i] == '-') return false;
    }
    return true;
}
int main(){
    int t;
    cin >> t;
    string s;

    int a,b,c;
    c=t;
    while(t--){
        cin >> s >> a;
        queue<pair<string,int>> q;
        set<string> se;
        q.push(make_pair(s,0));
        se.insert(s);
        b = -1;
        while(!q.empty()){
            pair<string,int> x = q.front();
            q.pop();
            if(chk(x.first)) {
                    b = x.second;
                    break;}
            for(int i =0;i<s.length()-a+1;i++){
                int mm = se.size();
                se.insert(flip(x.first,i,a));
                if(mm!=se.size()) q.push(make_pair(flip(x.first,i,a),x.second+1));
            }
        }
        if(b==-1) cout << "Case #" << c-t << ": " << "IMPOSSIBLE"<<endl;
        else cout << "Case #" << c-t << ": " <<b<< endl;


    }




return 0;
}
