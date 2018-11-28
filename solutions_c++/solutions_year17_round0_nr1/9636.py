#include <iostream>
#include <cstring>

using namespace std;

int count(string str, int k){
    int count = 0;
    for(int i = 0; i<str.size()-k+1; i++){
        if (str[i] == '-'){
            count++;
            for (int j=0; j < k; j++) {
                if(str[i+j] == '+') str[i+j] = '-';
                else str[i+j] = '+';
            }
            //cout << str << endl;
        }
    }
    for(int i = 0; i < str.size(); i++){
        if (str[i] == '-')
            return -1;
    }
    return count;
}

int main(){
    int n = 0;
    int k = 0;
    cin >>n;
    string str = "";
    for (int i = 1; i <=n; i++){
        cin >> str;
        cin >> k;
        if(count(str, k) == -1)
            cout << "Case #" << i << ": " <<  "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i << ": " <<  count(str, k) << endl;
    }

    return 0;
}
