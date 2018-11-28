#include <bits/stdc++.h>

using namespace std;

char s[25];
int v[25];
int main(){
    ifstream fin("home.in");
    ofstream fout("home.out");
    int T,test;
    fin>>T;
    for(test = 1;test <= T;test++){
        fin>>s + 1;
        int n,i;
        n = strlen(s + 1);
        for(i = 1;i <= n;i++){
            v[i] = s[i] - '0';
        }
        int mx = -1;
        for(i = 1;i <= n;i++){
            if(v[i] >= mx){
                mx = max(mx, v[i]);
            }else{
                int j = i - 1;
                for(i = i - 2;i >= 1 && v[i] == v[j];i--){
                    v[i]--;
                }
                v[j]--;
                for(j = i + 2;j <= n;j++){
                    v[j] = 9;
                }
                break;
            }
        }
        for(i = 1;v[i] == 0;i++);
        fout<<"Case #"<<test<<": ";
        for(;i <= n;i++){
            fout<<v[i];
        }
        fout<<'\n';
    }
    return 0;
}
