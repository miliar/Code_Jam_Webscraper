#include <iostream>
#include <string>
using namespace std;
string n;
int t, ult, caso;
bool cer;
int main()
{
    cin >> t;
    while (t--){
        caso++;
        cin >> n;
        ult = n.length();
        for (int i=n.length()-1; i>0;i--){
            if (n[i] < n[i-1]){
                ult = i;
                n[i-1]--;
            }
        }
        for (int i=ult;i< n.length();i++){
            n[i] = '9';
        }
        cer = false;
        cout << "Case #" << caso <<": ";
        for (int i=0;i<n.length();i++){
            if (!cer && n[i] != '0'){
                cer = true;
            }
            if (!(n[i] == '0' && !cer)){
                cout << n[i];
            }
        }
        cout << "\n";
    }
    return 0;
}
