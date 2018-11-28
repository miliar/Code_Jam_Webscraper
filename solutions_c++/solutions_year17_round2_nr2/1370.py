#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int r=0;r<T;r++){
        int n;
        cin >> n;
        int a[7];
        for(int i=0;i<6;i++) cin >> a[i];
        if(a[0] < a[3] || a[4] < a[1] || a[2] < a[5]) {
            cout << "Case #" << r+1 << ": IMPOSSIBLE" << endl;
            continue;
        }
        if((a[0] == a[3] && (a[1] + a[2] + a[4] + a[5]) > 0 && a[0] != 0) ||
                (a[4] != 0 && a[4] == a[1] && (a[0] + a[2] + a[3] + a[5]) > 0) ||
                    (a[2] != 0 && a[2] == a[5] && (a[1] + a[0] + a[4] + a[3]) > 0)){
            cout << "Case #" << r+1 << ": IMPOSSIBLE" << endl;
            continue;
        }
        //for(int i=0;i<6;i++) cout << a[i] << endl;
        string s1 = "";
        while(a[3] > 0){
            s1 += "RG";
            a[0] -- ;
            a[3] -- ;
        }
        string s2 = "";
        while(a[1] > 0){
            s2 += "BO";
            a[1] -- ;
            a[4] -- ;
        }
        string s3 = "";
        while(a[5] > 0){
            s3 += "YV";
            a[2] -- ;
            a[5] -- ;
        }
        if(a[0] == 0 && s1 != "") {
            cout << "Case #" << r+1 << ": " << s1 << endl;
            continue;
        }
        if(a[0] > 0 && s1 != "") s1 += 'R';
        
        if(a[4] == 0 && s2 != ""){
            cout << "Case #" << r+1 << ": " << s2 << endl;
            continue;
        }
        if(a[4] > 0 && s2 != "")s2 += 'B';
        
        if(a[2] == 0 && s3 != ""){
            cout << "Case #" << r+1 << ": " << s3 << endl;
            continue;
        }
        if(a[2] > 0 && s3 != "") s3 += 'Y';
        if(a[0] + a[2] < a[4] || a[0] + a[4] < a[2] || a[4] + a[2] < a[0]){
            cout << "Case #" << r+1 << ": IMPOSSIBLE" << endl;
            continue;
        }
        string s = "";
        int k = 0;
        while(a[0] > 0 || a[2] > 0 || a[4] > 0){
            if(k == 0) {
                if(a[0] >= a[2] && a[0] >= a[4]) {
                    s+='R';
                    a[0]--;
                }
                else{
                    if(a[2] >= a[0] && a[2] >= a[4]){
                        s += 'Y';
                        a[2] --;
                    }
                    else{
                        s += 'B';
                        a[4] --;
                    }
                }
            }
            else{
                if(s[k-1] == 'R'){
                    if(a[2] > a[4]){
                        s += 'Y';
                        a[2] --;
                    }
                    else{
                        s += 'B';
                        a[4] -- ;
                    }
                }
                if(s[k-1] == 'B'){
                    if(a[0] > a[2]){
                        s += 'R';
                        a[0] --;
                    }
                    else {
                        s += 'Y';
                        a[2] --;
                    }
                }
                if(s[k-1] == 'Y'){
                    if(a[0] > a[4]){
                        s += 'R';
                        a[0] --;
                    }
                    else{
                        s += 'B';
                        a[4] -- ;
                    }
                }
            }
            k++;
        }
        
        if(s[0] == s[s.size()-1]) {
            char c = s[s.size()-2];
            s[s.size()-2] = s[s.size()-1];
            s[s.size()-1] = c;
        }
        
        if(s1 != ""){
            string z = "";
            for(int i=0;i<s.size();i++){
                if(s[i] == 'R'){
                    z += s1;
                    for(int j=i+1;j<s.size();j++) z += s[j];
                    break;
                }
                else z += s[i];
            }
            s = z;
        }
        
        if(s2 != ""){
            string z = "";
            for(int i=0;i<s.size();i++){
                if(s[i] == 'B'){
                    z += s2;
                    for(int j=i+1;j<s.size();j++) z += s[j];
                    break;
                }
                else z += s[i];
            }
            s = z;
        }
        
        if(s3 != ""){
            string z = "";
            for(int i=0;i<s.size();i++){
                if(s[i] == 'Y'){
                    z += s3;
                    for(int j=i+1;j<s.size();j++) z += s[j];
                    break;
                }
                else z += s[i];
            }
            s = z;
        }
        cout << "Case #" << r+1 << ": " << s << endl;
    }
    return 0;
}










