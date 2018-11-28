#include <iostream>
#include <string>
using namespace std;

int main(){
    int ts;
    cin>>ts;
    for (int t = 1; t <= ts; t++) {
        string s;
        cin>>s;
        for (int i = 0; i < s.size() - 1; i++) {
            if (s.at(i) > s.at(i + 1)) {
                s.at(i) -= 1;

                while (i < s.size() - 1) {
                    s.at(i + 1) = '9';
                    i++;
                }
                if(s.at(0) == '0'){
                    s.erase(0,1);
                }
                i = -1;
            }
        }
        cout<<"Case #"<<t<<": "<<s<<endl;
    }
}
