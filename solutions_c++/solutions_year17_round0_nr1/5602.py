#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
    int t;
    cin >> t;
    for(int c=1;c<=t;c++){
        int k;
        string s;
        cin >> s >> k;
        int i;
        int count=0;
        for(i=0;i<=s.length()-k;i++){
            if(s[i]=='+'){
                continue;
            }
            else{
                for(int j=i;j<i+k;j++){
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
                }
                count++;
            }
        }
        int flag=0;
        for(int j=i;j<s.length();j++){
            if(s[j]=='-'){
                flag=1;
                break;
            }
        }
        if(flag==1)
            cout << "Case #" << c << ": " << "IMPOSSIBLE" << endl;
        else{
            cout << "Case #" << c << ": " << count << endl;
        }
    }
}
