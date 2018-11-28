#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define PI 3.1413916333897931384616433831
#define MOD 1000000007
#define MOD1 1000000009
#define bas 19
#define bas1 19
using namespace std;
int isless(string s , string target){
    for(int i = 0 ; i < s.size() ; i++){
        if(s[i]< target[i])return 1;
        else if(s[i] >target[i]) return -1 ;

    }
    return 0 ;
}
int main()
{
    freopen("in","r",stdin);
    freopen("outp","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t ;
    cin>>t;
    string s ;
    for(int u = 1 ; u <= t ; u++){
        cin>>s;
        string res = "";
        string test = "";
        int be = 0 ;
        for(int i = 0 ; i < s.size() - 1 ; i++)res+='9';
        for(int i = 0 ; i <= s.size() - 1 ; i++)test+='1';
        while(be < s.size()){
            int which = isless(test,s);
            if(which >= 0){
                res = test;
                if(test[be]=='9')break;
                for(int i = be ; i < test.size() ; i++){
                    test[i]++;
                }
            }else {
                if(test[be]=='1')break;
                for(int i = be ; i < test.size() ; i++){
                    test[i]--;
                }
                be++;
            }

        }

        cout<<"Case #"<<u<<": "<<res<<endl;

    }
}
