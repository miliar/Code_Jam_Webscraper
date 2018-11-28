#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int main(){
    int q;
    cin >> q;
    for(int t = 0; t < q; t++){
        string s;
        cin >> s;
        string a;
        a = s;
        while(1){
            int flag = 0;
            int i;
            for(i = s.length() - 1; i > 0; i--){
                if(a[i] < a[i-1]){
                    a[i-1]--;
                    flag = 1;
                    break;
                }
            }
            if(flag == 0){
                break;
            }
            while(a[i] != '\0'){
                a[i] = '9';
                i++;
            }
        }
        cout << "Case #" << t+1 <<": ";
        for(int i = 0; i < a.length(); i++){
            if(a[i] != '0'){
                cout << a[i];
            }
        }
        cout << '\n';
    }

    return 0;
}
