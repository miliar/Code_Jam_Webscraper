#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<string>
using namespace std;

typedef long long in;

int main(){
    in test;
    cin >> test;
    for(in t=0;t<test;t++){
        cout << "Case #" << t+1 << ": ";
        string s;
        in k;
        cin >> s >> k;
        int ct=0;
        bool imp=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='-'){
                ct++;
                for(int j=0;j<k;j++){
                    if(i+j>=s.size()){
                        cout << "IMPOSSIBLE" << endl;
                        imp=1;
                        break;
                    }
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else
                        s[i+j]='-';
                }
            }
            if(imp)
                break;
        }
        if(!imp)
            cout << ct << endl;
    }
    return 0;
}
