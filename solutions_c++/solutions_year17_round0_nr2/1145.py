#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++) {
        string n;
        cin>>n;
        cout << "Case #"<<tt<<": ";

        string r;
        int l=n.length();
        int i=0;
        for(i=1;i<l;i++) {
            if(n[i]<n[i-1]) break;
        }

        if(i==l) { cout << n << "\n"; continue; }

        int j=i-1;

        for(j=i-1;j>=1;j--) {
            if(n[j]>n[j-1]) break;
        }

        if(j==0 && n[j]=='1') {
            r.resize(l-1,'9');
        }
        else {
            r=n;
            r[j]=n[j]-1;
            for(int k=j+1;k<l;k++) r[k]='9';
        }
        cout << r << "\n";
    }
    return 0;
}
