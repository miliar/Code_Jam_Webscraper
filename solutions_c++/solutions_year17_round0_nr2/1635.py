#include <iostream>
#include <string>
using namespace std;

int main(){
    int nCases;
    cin >> nCases;

    string n;
    int lenN;

    for(int i = 0; i < nCases; i ++){
        cin >> n;
        lenN = n.size();
        for(int j = 1; j < lenN; j ++){
            if(n[j] < n[j - 1]){
                n[j - 1] --;
                int startFrom = j - 1;
                for(; startFrom > 0; startFrom --){
                    if(n[startFrom] >= n[startFrom - 1])
                        break;
                    n[startFrom - 1] --;
                }
                for(int k = startFrom + 1; k < lenN; k ++){
                    n[k] = '9';
                }
            }
        }

        cout << "Case #" << i + 1 << ": ";
        bool flagStarted = false;
        for(int j = 0; j < lenN; j ++){
            if(!flagStarted){
                if(n[j] == '0')
                    continue;
                flagStarted = true;
            }
            cout << n[j];
        }
        cout << endl;
    }
    return 0;
}

