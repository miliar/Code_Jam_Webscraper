#include<bits/stdc++.h>
using namespace std;

int main(){

    freopen("B-large.in","r",stdin);
    freopen("output3.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        string s;
        cin >> s;


        for(int j=0;j<s.length()-1;j++){
            if(s[j]>s[j+1]){
                s[j]--;
                string s1=s.substr(0,j+1);
                int l=s.length()-j-1;
                string s2(l,'9');
                s = s1+s2;

                j=-1;
            }
        }
        cout<<"Case #"<<i<<": ";
        if(s[0]=='0'){
            cout << s.substr(1) << "\n";
        }
        else {
            cout << s << endl;
        }



    }
    return 0;
}
