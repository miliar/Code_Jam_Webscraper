#include<fstream>
#include<sstream>
#include<iostream>
void tidy(std::string &s){
    for(int i=1; i<s.length(); i++){
        if(s[i-1]>s[i]){
            for(int k=i;k<s.length();k++) s[k] = '9';
            int k;
            for(k=i-2;k>=0;k--)
                if(s[k]==s[i-1]) s[k] = '9';
                else break;
            s[k+1] = s[i-1]-1;
            if(i-1 != k+1)
                s[i-1] = '9';
            break;
        }
    }
}
int main(){
    std::ofstream cout;
    cout.open("C:\\B-large.out");
    std::ifstream cin;
    cin.open("C:\\B-large.in");

    int T;
    cin >> T;
    for(int t=1; t<=T; t++){
        std::string s;
        cin >> s;
        tidy(s);
        std::stringstream ss (s);
        uint64_t ans;
        ss >> ans;
        cout << "Case #" << t << ": "<< ans << "\n";
    }

    cin.close();
    cout.close();
}
