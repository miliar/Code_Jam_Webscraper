#include <bits/stdc++.h>

using namespace std;

long long T, N, ans[110];
string s;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> T;
    for(int i = 1; i <= T ; i++){
        cin >> s;
        int loop = 1;

        long long tem=1;
        for(int j = s.length()-1; j >= 0 ; j--){
                int a = (int)(s[j]-'0');
                ans[i]+=(int)a *tem;
                tem*=10;
        }

        while (loop){

        long long tem=1;
        for(int j = s.length()-1; j >= 0 ; j--){
                s[j]=(char)((ans[i]/tem)%10+'0');
                tem*=10;
        }

        int pre = 0,now = -1,checked = 0;
        for(int j = 0; j < s.length(); j++){
            now++;
            int tem = (int)(s[j]-'0');
            if(tem < pre){
                checked = 1;

                break;
            }
            pre = tem;
            if(checked == 0 && j==s.length()-1)loop=0;
        }

        if(checked){
            ans[i]=0;
            long long tem = 1;
            for(int j = s.length()-1; j >= 0 ; j--){
                int a = (int)(s[j]-'0');

                if(j >= now)ans[i]+=9*tem;
                else if(j == now-1)ans[i]+=(a- 1)*tem;
                else ans[i]+=(int)a *tem;
                tem*=10;
            }
        }

        }

    }
    for(int i = 1; i <= T; i++){
        cout<<"Case #"<<i<<": "<<ans[i]<<endl;

    }
    return 0;
}
