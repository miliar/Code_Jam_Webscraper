#include <bits/stdc++.h>
using namespace std;
int t,k;
string s;
void flip(char& cc)
{
    if(cc=='+')cc='-';
    else if(cc=='-')cc='+';
}
int dostuff(string &r)
{
    int cnt = 0;
    int lm = r.size();
    for(int i=0;i<lm;i++)
    {
        if(i+k<=lm){
            if(r[i]=='+')continue;
            for(int j=i;j<i+k;j++){
                flip(r[j]);
            }
            cnt++;
        }
    }
    return cnt;
}
bool check(string &r)
{
    bool yes = true;
    for(int i=0;i<r.size();i++){
        if(r[i]=='-'){
            yes = false;
            break;
        }
    }
    return yes;
}
int main()
{
    freopen("aain.txt","r",stdin);
    freopen("aaout.txt","w",stdout);
    cin.tie(0),cout.tie(0),ios_base::sync_with_stdio(false);
    cin >> t;
    for(int i=0;i<t;i++)
    {
        cin >> s >> k;
        int rm = dostuff(s);
        if(check(s)){
            cout << "Case #" << i+1 << ":" << " " << rm << '\n';
        }
        else{
            cout << "Case #" << i+1 << ":" << " " << "IMPOSSIBLE" << '\n';
        }
    }
    return 0;
}
