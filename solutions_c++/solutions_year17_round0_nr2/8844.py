/*|In The Name Of Allah|*/

//your input- file : RECin.txt
//your output file : RECot.txt

#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;

int T , t = 1;

bool good(string a){
     string b = a;
     sort(b.begin() , b.end());
     return (a == b);
}

string noo(string a){
       bool fou = false;
       string n = "";
       for(int i = 0; i < a.size(); i++){
           if(a[i] != '0') fou = true;
           if(fou) n += a[i];
       }
       return n;
}

string gen(string a){
    while(!good(a)){
        bool doo = false;
        for(int i = 0; i < a.size()-1; i++){
            if(doo) a[i] = '9';
            if(a[i] > a[i+1] && !doo)
               a[i]-- , doo = true;
        } a[a.size()-1] = '9';
    }
    return noo(a);
}

int main(){
    freopen("B-large.in" , "r" , stdin);
    freopen("RECot.txt" , "w" , stdout);
    cin >> T;
    while(T--){
        string s;
        cin >> s;
        cout << "Case #" << t++ << ": ";
        if(good(s)){
            cout << s << endl;
        } else {
            cout << gen(s) << endl;
        }
    }
    return 0;
}
