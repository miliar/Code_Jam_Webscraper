#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int,int>pii;
char lst='a';

string str = "";
bool comp(pair<int,char> p1, pair<int,char> p2){
    if(p1.first == p2.first){
        if(str.length()){
            if(p1.second == str[0]) return true;
            else return false;
        }else{
            if(p1.second == lst) return false;
            else return true;
        }
    }
    if(p1.second == lst) return false;
    else if(p1.first > p2.first) return true;
    return false;
}
int main(){

    freopen("inin.in","r",stdin);
    freopen("outout.out","w",stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        int n;
        int r,o,y,g,b,v;
        int z ;
        cin >> z >> r >> o >> y >> g >> b >> v;
        pair<int,char> pr[3];
        pr[0].first = r;
        pr[0].second = 'R';

        pr[1].first = y;
        pr[1].second = 'Y';

        pr[2].first = b;
        pr[2].second = 'B';

        str = "";
        lst = 'a';

        bool isAns = true;
        for(int f = 0; f < z; f++){
            sort(pr,pr+3,comp);
            bool fnd = false;
            for(int e = 0; e <= 2; e++){
                if(pr[e].first <= 0){
                    fnd = false;
                    break;
                }
                if(lst != pr[e].second){
                    fnd = true;
                    pr[e].first--;
                    str+=pr[e].second;
                    lst = pr[e].second;
                    break;
                }
            }
            if(!fnd) {isAns = false;}
        }

        for(int i = 0; i < str.length(); i++){
            if(str[i] == str[(i+1)%str.length()]){
                isAns=false;
                break;
            }
        }
        if(isAns && str.length() == z){
            cout << "Case #" << i <<": " << str << endl;
        }else{

            cout << "Case #" << i <<": " << "IMPOSSIBLE" << endl;
        }
    }


    return 0;
}
