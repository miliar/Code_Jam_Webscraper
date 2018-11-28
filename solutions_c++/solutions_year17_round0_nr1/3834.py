#include<fstream>
int main(){
    std::ofstream cout;
    cout.open("C:\\A-large.out");
    std::ifstream cin;
    cin.open("C:\\A-large.in");

    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        std::string s;
        int k;
        cin >> s >> k;
        int cnt = 0, j;
        for(j=0; j<=s.length()-k; j++){
            if(s[j]=='-'){
                for(int r=0; r<k; r++){
                    if(s[j+r]=='+') s[j+r] = '-';
                    else            s[j+r] = '+';
                }
                ++cnt;
            }
        }
        bool all_happy = true;
        for(j=j; j<s.length(); j++){
            if(s[j]=='-'){
                all_happy = false;
                break;
            }
        }
        if(all_happy)
            cout << "Case #" << i+1 << ": " << cnt << "\n";
        else
            cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
    }

    cin.close();
    cout.close();
}
