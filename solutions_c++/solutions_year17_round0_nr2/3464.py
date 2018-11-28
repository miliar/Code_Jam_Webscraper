#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for(int i = a; i <= b ;i++)

bool check(string s1){
    for(int i = 0; i<s1.size()-1; i++){
        if(s1[i] > s1[i+1]) return false;
    }
    return true;
}
string make_tidy_num(string s1){
    string tep;
    bool b =false;
    int t = 0,c = 1;
    for(int i = 1; i<s1.size(); i++){
            if(s1[i-1] >= s1[i] and !b){
                b = true;
                t = 1;
            }
     if(b and c) {
        if(((s1[i-1] - '1') + 48) ==  '0'){
             continue;
        }
        c = 0;
     }
     (b)?(t and ((s1[i-1] - '1') + 48) > '0')? tep +=  (s1[i-1] - '1') + 48  : tep += '9'  : tep += s1[i-1];
     t = 0;
    }
    tep += '9';
    return tep;
}
int main()
{
    //freopen("b_in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    ios_base::sync_with_stdio(false);cin.tie(NULL);
    int n,k = 0;
    cin >> n;
    while(n--){

       string p;
       cin >> p;
    cout << "Case #" << ++k << ": ";
       if(p.size() == 1)
          cout << p << endl;
       else{
          if(check(p))
             cout << p << endl;
          else
             cout << make_tidy_num(p) << endl;
       }

    }
    return 0;
}

