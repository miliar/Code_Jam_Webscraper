#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);

    int t;
    cin >> t;
    for(int it=1;it<=t;it++) {
        string s,ans="",temp="";
        char c;
        cin >> s;
        int i,j,n,pos=-1;
        n = s.length();
        if(n == 1) {
            ans = s;
        }
        else {
            for(i=0;i<n-1;i++) ans = ans + "9";
            for(i=n-2;i>=0;i--) {
                temp.clear();
                if(s[i] > s[i + 1]) {
                    pos = 1;
                    if(i > 0 || (i == 0 && s[i] != '1')) {
                        c = s[i] - 1;
                        temp = temp + c;
                        for(j=i+1;j<n;j++) temp = temp + "9";
                        for(j=i-1;j>=0;j--) {
                            if(s[j] > temp[0]) temp = temp[0] + temp;
                            else temp = s[j] + temp;
                        }
                        if(temp[0] == '0') continue;
                        if(temp.length() > ans.length()) ans = temp;
                        else {
                            if(temp > ans) ans = temp;
                        }
                    }
                }
                else {
                        if(pos == -1) {
                            temp = temp + s[i];
                            for(j=i+1;j<n;j++) temp = temp + s[j];
                            for(j=i-1;j>=0;j--) {
                                if(s[j] > temp[0]) temp = temp[0] + temp;
                                else temp = s[j] + temp;
                            }
                            if(temp[0] == '0') continue;
                            if(temp.length() > ans.length()) ans = temp;
                            else {
                                if(temp > ans) ans = temp;
                            }
                        }
                        else {
                            if((i > 0 || (i == 0 && s[i] != '1')) && s[i] != '0') {
                                c = s[i] - 1;
                                temp = temp + c;
                                for(j=i+1;j<n;j++) temp = temp + "9";
                                for(j=i-1;j>=0;j--) {
                                    if(s[j] > temp[0]) temp = temp[0] + temp;
                                    else temp = s[j] + temp;
                                }
                             //   cout << temp << "\n";
                                if(temp[0] == '0') continue;
                                if(temp.length() > ans.length()) ans = temp;
                                else {
                                    if(temp > ans) ans = temp;
                                }
                            }
                        }
                }
            }
        }
        cout << "Case #" << it << ": " << ans << "\n";
    }
    return 0;


}
