#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    for (int i=1; i<=t; ++i) {
        string n;
        cin >> n;
        for (int j=0; j<n.size()-1; j++) {
            if (n[j+1]<n[j]) {
                --(n[j]);
                for (int k=j+1; k<n.size(); k++) {
                    n[k] = '9';
                }
                j=-1;
                continue;
            }
            if (j == n.size()-2) {
                break;
            }
        }
        if (n[0] == '0') {
            n[0] = ' ';
        }
        cout << "Case #" << i << ":" << ((n[0]==' ')?(""):(" ")) << n << endl;
    }
    
    return 0;
}
