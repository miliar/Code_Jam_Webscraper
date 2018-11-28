#include <iostream>

using namespace std;

int main() {
    int t,i,cn=1;
    cin >> t;
    while(t--) {
        string a;
        bool flag=false;
        cin >> a;
        i=0;
        while(a[i]!='\0'&&a[i+1]!='\0') {
            if(a[i]>a[i+1]) {
                flag=true;
                break;
            }
            i++;
        }
        if(flag) {
            while(i) {
                if(a[i]==a[i-1])
                    i--;
                else
                    break;
            }
            a[i]--;
            i++;
            while(a[i]!='\0') {
                a[i]='9';
                i++;
            }
        }
        //a[i]='\0';
        a.erase(0, a.find_first_not_of('0'));
        cout <<"Case #"<< cn << ": " <<  a << endl;
        cn++;
    }
    return 0;
}
