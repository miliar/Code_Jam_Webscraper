#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <list>

using namespace std;
typedef  long long ll;

string zero(string s){
    int y=0;
    string sol="" ;
    for (int i = 0 ; i<s.length(); i++) {
        if (s[i]!='0') y++;
        if(y) sol+=s[i];
    }
    return sol;
}


int main()
{
    freopen("B-largesamir.in", "r", stdin);
    freopen("outputBL.txt", "w", stdout);

    int c;
    cin>>c;
    for (int ii = 0 ; ii<c; ii++) {
        cout<<"Case #"<<ii+1<<": ";
        string s,sol="";
        cin>>s;
        s=zero(s);
        int hh=0;
        for (int i = 1 ;i<s.length(); i++) {
            if(s[i]<s[i-1]) {
                if(s[i]=='0' && s[i-1]=='1') {
                    for (int j = 1; j<s.length(); j++) sol+='9';
                    hh++;
                    break;
                }
                
                int tt=0;
                for (int j=0;j<=i-1;j++) {
                    if(s[j]==s[i-1] && tt==0) {s[j]--;tt++;}
                    else if(s[j]==s[i-1] && tt!=0) {s[j]='9';}

                }
            
                for (int j = i; j<s.length(); j++) {
                    s[j]='9';
                }
                i--;
            }
        }
        if(hh){
            cout<<sol<<endl;
        }
        else cout<<zero(s)<<endl;
    }
 
    return 0;
}
