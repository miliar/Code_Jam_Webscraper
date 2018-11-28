#include <bits/stdc++.h>

#define verbose 0
#define inf 1e9;
using namespace std;

void write(int n, long long ans){
   ofstream ofs;
   ofs.open ("out.txt", ios_base::app);
   // ofs << fixed << setprecision(6);
   ofs << "Case #" << n << ": " << ans << endl;
   ofs.close();
}


long long solve(string s){
    for (int i = 0; i < s.size()-1; i++){
        if (s[i] > s[i+1]){
            s[i] = char(int(s[i]) - 1);
            if (i > 0 && s[i-1] > s[i]) return solve(s);

            for (int j = i+1; j < s.size(); j++){
                s[j] = '9';
            }
            return stoll(s);
        }
    }
    return stoll(s);
}

int main(void){
   remove("out.txt");
   int T;
   cin >> T;
   for (int i = 1; i <= T; i++){
       string s;
       cin >> s;
       write(i, solve(s));
   }
   return 0;
}
