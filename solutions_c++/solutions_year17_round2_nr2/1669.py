#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cmath>
#include<string>
#include<algorithm>
#include<cstdlib>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pr;
const double pi=acos(-1);
#define rep(i,a,n) for(int i=a;i<=n;i++)
#define per(i,n,a) for(int i=n;i>=a;i--)
#define Rep(i,u) for(int i=head[u];i;i=Next[i])
#define clr(a) memset(a,0,sizeof a)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())



bool sortbysec(const pair<char,int>&a,const pair<char,int>&b){
    return a.second > b.second;
}

void removezero(vector<pair<char,int> > & colors){
    vector<int> pos;
    for(int i = 0;i<colors.size();i++)
        if(colors[i].second == 0)
            pos.pb(i);
    for(int i = 0;i<sz(pos);i++)
        colors.erase(colors.begin()+pos[i]);
}

string getDist(vector<pair<char,int> > colors){  
    string s = "";
    s += colors[0].first;
    colors[0].second--;
    sort(colors.begin(),colors.end(),sortbysec);
    while(!colors.empty()){
        int ind = 0;
        for(int i = 0;i<colors.size();i++){
            if(colors[i].first != s[s.size()-1]){
                s+=colors[i].first;
                colors[i].second--;
                break;
            }
        }
        removezero(colors);
        sort(colors.begin(),colors.end(),sortbysec);
    }
    if(s[0] == s[s.size()-1]){
        swap(s[s.size()-1],s[s.size()-2]);
    }
    return s;
}

int main(){
    int t;
    cin>>t;
    int i = 1;
    int r,o,y,g,b,v;
    int n;
    vector< pair<char,int> > colors(6);
    while(t--){
        //logic
        int h;
        colors.clear();
        cin>>n>>r>>o>>y>>g>>b>>v;
        colors.push_back(mp('R',r));
        colors.push_back(mp('O',o));
        colors.push_back(mp('Y',y));
        colors.push_back(mp('G',g));
        colors.push_back(mp('B',b));
        colors.push_back(mp('V',v));

        sort(colors.begin(),colors.end(),sortbysec);
        //reverse(all(colors));
        //cout<<endl;

        h= n/2;
        if(r > h || o > h || y > h || g > h || b > h || v > h){
            cout<<"Case #"<<i++<<": "<<"IMPOSSIBLE"<<endl;
        }else{
             
            cout<<"Case #"<<i++<<": "<<getDist(colors)<<endl;
        }
    }
}
