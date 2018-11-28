#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define PI 3.1413916333897931384616433831
#define MOD 1000000007
#define MOD1 1000000009
#define bas 19
#define bas1 19
using namespace std;
int main()
{
     freopen("in","r",stdin);
    freopen("outp","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t , k ;
    cin>>t;
    string s ;
    for(int u = 1 ; u <= t ; u++){
        cin>>s >>k;
        int cou = 0 ;
        for(int i = 0 ; i <= s.size() - k ; i++){
            if(s[i]=='-'){
                for(int j = i ; j <i + k ; j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
                cou++;
            }
        }
        bool is = true;
        for(int i = 0 ; i < s.size() ; i++){
            if(s[i]=='-'){
                is = false ;
                break;
            }
        }
        if(is)cout<<"Case #"<<u<<": "<<cou<<endl;
        else cout<<"Case #"<<u<<": "<<"IMPOSSIBLE"<<endl;
    }
}
