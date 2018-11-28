#include <bits/stdc++.h>

using namespace std;

string s;

string solve(int p, char last , bool done){
    string ret ;
    if(p==s.size())return "";
    if(!done && s[p]<last) return "0";
    if(done) return "9"+solve(p+1,last,done);
    if(s[p]>=last) {
        string a = s[p]+solve(p+1,s[p],done);
        if(a.size()>1 && a[1]=='0') {
            if(s[p]==last) return "0";
            else a = (char)(s[p]-1)+ solve(p+1,s[p]-1,1);
            return a;
        }
        return a;

    }
}

int main()
{
    ifstream cin("B-large (2).in");
    ofstream cout("out.txt");
    int t ;
    cin >> t ;
    for(int tc=1 ;  tc<=t; tc++){

        cin >> s ;
        string ans = solve(0,'0',0);
        if(ans[0]=='0')
        {reverse(ans.begin(),ans.end());
        ans.pop_back();
        reverse(ans.begin(),ans.end());}

        cout << "Case #" << tc << ": "<<ans<<endl;

    }
}
