#include <cstdio>
#include <iostream>
#include <string>

int main(){
    int t, k, cont, flag;
    std::string s;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        cont = flag = 0;
        s.clear();
        std::cin >> s;
        scanf("%d", &k);
        for(int j = 0; j < s.size(); j++){
            for(int b = 0; b < s.size(); b++){
                if(s[b] == '-' && k + b <= s.size()){
                    cont++;
                    for(int a = b; a < k + b; a++){
                        if(s[a] == '-'){
                            s[a] = '+';
                        }
                        else
                            s[a] = '-';
                    }
                }
            }
        }
        for(int j = 0; j < s.size(); j++)
            if(s[j] == '-')
                flag = 1;
        if(flag)
            printf(" Case #%d: IMPOSSIBLE\n", i);
        else
            printf(" Case #%d: %d\n", i, cont);
        
    }
    return 0;
}
