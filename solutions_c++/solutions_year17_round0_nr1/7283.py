#include <bits/stdc++.h>
#define cin in
#define cout out

using namespace std;

int t,k,a[1005],cnt;
string s;

int main() {
    ifstream in("file.in");
    ofstream out("file.out");
    cin >> t;
    for(int h=1;h<=t;h++){
        bool pos=1; cnt=0;
        cin >> s >> k;
        for(int i=0;i<s.length();i++){
            a[i]=0;
        }
        for(int i=0;i<s.length();i++){
            if(i) a[i]+=a[i-1];
            if(a[i]%2){
                if(s[i]=='+') s[i]='-';
                else s[i]='+';
            }
            if(s[i]=='-'){
                if(i>s.length()-k){
                    pos=0;
                }
                else{
                    a[i]++;
                    a[i+k]--;
                    cnt++;
                }
            }
        }
        if(!pos) cout << "Case #" << h << ": IMPOSSIBLE\n";
        else cout << "Case #" << h << ": " << cnt << '\n';
    }
}
