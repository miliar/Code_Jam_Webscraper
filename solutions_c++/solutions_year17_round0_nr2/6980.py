#include <iostream>
using namespace std;
int main() {
    int t;
    string n;
    cin>>t;
    for(int i=1;i<=t;i++) {
        cin>>n;
        for (int j=n.size()-1;j>=0;j--) {
            int k = j;
            if (n[k] < n[k-1]) {
                for (int m = k+1; m < n.size(); m++) {
                    n[m] = '9';
                }
                n[k] = '9';
                int l = k-1;

                //carry
                while (n[l] == '0') {
                    n[l] = '9';
                    l--;
                }

                n[l] = n[l] - '1' + '0';
            }
        }
        bool leadZero = 1;

        string tmp = "";
        for (int j = 0; j<n.size();j++) {
            if (!j && n[j] == '0') continue;
            else if (n[j] == '0' && leadZero) continue;
            else {
                tmp += n[j];
                leadZero = 0;
            }
        }
        cout<<"Case #"<<i<<": "<<tmp<<endl;
    }
}