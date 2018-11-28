#include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    string s;
    int T, q=0;
    int k,len,cnt, i;
    bool flag;
    cin >> T;
    while(T--){
        q++;
        cin>>s >> k;
        len = s.length();
        cnt = 0;
        flag = true;
        for(i=0; i<=len-k;i++){
            if(s[i]=='-'){
                cnt++;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        for(;i<len;i++){
            if(s[i]=='-'){
                flag=false;
                break;
            }
        }
        if(flag==true)
            cout << "Case #"<<q<<": "<< cnt << endl;
        else
            cout << "Case #"<<q<<": "<< "IMPOSSIBLE" << endl;

    }
}
