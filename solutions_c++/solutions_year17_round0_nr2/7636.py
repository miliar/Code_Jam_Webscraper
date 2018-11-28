#include <bits/stdc++.h>
using namespace std;



string s;
void findNonDecreasing(int index){
    if(index==0) return;
    if(s[index]>=s[index-1]) {
        findNonDecreasing(index-1);
        return;
    }else{
        for (int i = index; i < s.length(); ++i) {
            s[i]='9';
        }
        s[index-1]-=1;
        findNonDecreasing(index-1);
    }
}

int main() {
    freopen("inputB","r",stdin);
    freopen("outputB","w",stdout);
    int tests;
    cin>>tests;
    for (int T = 1; T <= tests; ++T) {
        cin>>s;
        findNonDecreasing(s.length()-1);

        cout<<"Case #"<<T<<": ";
        if(s[0]!='0') cout<<s[0];
        for (int i = 1; i < s.length(); ++i) {
            cout<<s[i];
        }

        cout<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
