#include<iostream>
#include<cstdint>
#include<string>
#include<algorithm>

using namespace std;
typedef int64_t var;

var find_best(var a){
    std::string str(to_string(a));
    reverse(str.begin(),str.end());
    var s = 0;
    for(var i = 1; i < str.size(); ++i){
        if(str[i]>str[i-1]){
            for(var j = s; j < i; ++j){
                str[j]='9';
            }
            s=i;
            str[i]--;
        }
    }
    while(str[str.size()-1]=='0'){
        str.pop_back();
    }
    reverse(str.begin(),str.end());
    return stoll(str);
}

int main(){
    var t;
    cin >> t;
    for(var i = 0; i < t; ++i){
        var b;
        cin >> b;
        cout << "Case #" << (i+1) << ": " << find_best(b) << endl;
    }
    return 0;
}
