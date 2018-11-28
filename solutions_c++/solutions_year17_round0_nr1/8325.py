#include  <vector>
#include <iostream>
#include <string>


int main(){
    int a;
    std :: cin >> a;
    int cc = 1;
    while(a--){
        std :: string str;

        int siz;
        int cntr = 0;
        std :: cin >> str >> siz;
        bool ret = true;
        int i = 0;
        while(i < str.size() && i + siz <= str.size()){
            if(str[i] == '+'){
                ++i;
                continue;
            }
            cntr++;
            bool yes = true;
            int k = 0;
            while(k < siz){
                if( str[i + k] == '+' ) str[i + k] = '-';
                else str[i + k] = '+';
                if(str[i + k] == '-') yes = 0;
                k++;
            }
            i += yes?k : 0;
        }
        while(i < str.size()) if(str[i++] == '-') ret = false;
        std :: cout << "Case #" << cc++ << ": ";
        if(ret) std :: cout << cntr ;
        else std :: cout << "IMPOSSIBLE";
        std :: cout << std :: endl;
    }
    return 0;
}
