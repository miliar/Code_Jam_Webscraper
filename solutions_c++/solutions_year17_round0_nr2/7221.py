#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    scanf("%d", &n);
    string s;

    for(int x=1;x<=n;x++){
        cin >> s;

        printf("Case #%d: ", x);

        if(s.size() == 1){
            printf("%s\n", s.c_str());
            continue;
        }

        int tam = s.size();
        int eq = 0;

        for(int i = 0; i < (tam-1); i++){
            if(s[i] > s[i+1]){
                if(s[eq] != '1' and s[eq] != '0'){
                    s[eq] = (s[eq] + '0' - 1) - '0';
                    for(int ii = eq + 1; ii <= i; ii++){
                        s[ii] = '9';
                    }
                }
                else{
                    for(int ii = eq; ii <= i; ii++){
                        if(s[ii] == '1' and s[i+1] == '0' and ii){
                            s[ii] = '9';
                        }
                        else if(s[ii] != '0'){
                            s[ii] = (s[ii] + '0' - 1) - '0';
                        }
                        else{
                            s[ii] = '9';
                        }
                    }
                } 
                //s[eq] = (s[eq] + '0' - 1) - '0';

                for(int ii = i+1; ii < tam; ii++)
                    s[ii] = '9';

                break;
            }
            if(s[i] != s[i+1]) eq = i + 1;
        }

        cout << stoll(s) << endl;
        //cout << s << endl;
    }

    return 0;
}
