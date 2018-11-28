#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int t;

bool ok(int i ){
    string k  ="";
    while(i){k+=(i%10) + '0'; i/=10;}
    reverse(k.begin(),k.end());
    for(int i = 1; i < k.length(); i++)
        if(k[i]<k[i-1])return false;
    return true;
}

string check(string st){
    string ans ="";

    int nr = 0;

    for(int i = 0; i < st.length(); i++){
        nr = nr*10 + (st[i]-'0');
    }
    int ss=0;
    for(int i = 0; i <= nr; i++){
        if(ok(i)){
            ss=i;
        }
    }
    while(ss){
        ans+= (ss%10) + '0';
        ss/=10;
    }
    reverse(ans.begin(),ans.end());

    return ans;
}
int main(){
    freopen("blarge.in", "r" , stdin);
    freopen("outputblarge.txt", "w" , stdout);
    cin >> t;

    for(int i = 0; i < t; i++){
        string st;
        cin >> st;

        int firstPoz=0, bigNr = 0;
        int gg = 0;
        for(int e =0; e < st.length(); e++){
            if(e > 0 && st[e] < st[e-1]) break;
            if(st[e]-'0' > bigNr){
                bigNr = st[e] - '0';
                firstPoz = e;
            }
            gg++;
        }
        string dd= st;
        string ans;
        if(st.length() == 1 || gg==st.length()){
            ans = st;
        }else if(bigNr == 1){
            int sz = st.length();
            st="";
            for(int  e = 0; e < sz-1; e++){
                st+='9';
            }
            ans = st;
        }else{
            st[firstPoz] = (bigNr-1) + '0';
            for(int e = firstPoz+1; e < st.length(); e++){
                st[e]='9';
            }
            ans = st;
        }
        //string chk = check(dd);
       // if(chk != ans){
        //    cout << dd << " <----> " << chk << " " << ans << endl;
        //}
        cout << "Case #" << i+1 << ": " << ans<< endl;

    }

    return 0;
}
