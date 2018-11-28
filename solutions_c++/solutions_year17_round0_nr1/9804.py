#include <bits/stdc++.h>
#define FAST_INPUT ios_base::sync_with_stdio(0);cin.tie(0)
#define ll long long
using namespace std;


string inputString;
int K;
int ans;

struct Pair{
    string str;
    int depth;
    Pair(string s,int d){
        str = s;
        depth = d;
    }
};




set<string>s;


int exist(string str){

    if (s.find(str) == s.end()) return 0;
    return 1;

}



int allPlus(string str){
    int len = str.length();
    for(int c = 0;c<len;c++){
        if(str[c] == '-') return 0;
    }
    return 1;
}



void bfs(string str,int depth){
    queue<Pair> q;
    q.push(Pair(str,depth));
    s.insert(str);

    while(!q.empty()){
        Pair p = q.front();q.pop();
        string cstr = p.str;
        int d = p.depth;
        if(allPlus(cstr) == 1){
            ans = d;
            break;
        }
        for(int i = 0;i<=cstr.length()-K;i++){

            int ii = i;
            string temp = cstr;
            for(int j = 0;j<K;j++){
                if(temp[ii] == '-')temp[ii] = '+';
                else temp[ii] = '-';
                ii++;
            }

            if(exist(temp) == 0){
                q.push(Pair(temp,d+1));
                s.insert(temp);
            }

        }

    }




}














int main(){
    //freopen("E:/a.in","r",stdin);
    //freopen("E:/aout.txt","w",stdout);
    FAST_INPUT;

    int T;
    cin >> T;
    int v;
    int t = 1;
    while(T-->0){
        s.clear();

        cin >> inputString >> K;
        ans = -1;
        bfs(inputString,0);


        cout << "Case #"<< (t++) << ": ";
        if(ans != -1)cout <<  ans << endl;
        else cout <<  "IMPOSSIBLE" << endl;


    }







    return 0;



}
