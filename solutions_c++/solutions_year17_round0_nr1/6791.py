#include <iostream>
#include <string>

using namespace std;


int main() {
    int T, K, c, f, i, x;
    string S;   

    c=0;

    cin >> T;

    while(T) {
        T--;
        c++;
        f=0;
       
        cin >> S >> K; 

//cout << "[T=" << T << "][c=" << c << "][S=" << S << "][K=" << K << "]" << endl;
    
        for(i=0; i<S.length(); i++) {
            if(S[i]=='+') continue;
            if(i+K>S.length()) break;
            for(x=0; x<K; x++) {
                if(S[i+x]=='+') S[i+x]='-';
                else S[i+x]='+';
            }
            f++;
        }

//cout << "[T=" << T << "][c=" << c << "][S=" << S << "][K=" << K << "][i=" << i << "][x=" << x << "][f=" << f << "]" << endl << endl;

        cout << "Case #" << c << ": ";

        if(i==S.length()) cout << f;
        else cout << "IMPOSSIBLE";

        cout << endl; 

       
    }

    return 0;
}

