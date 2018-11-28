
/*
JUST FOR SMALL
*/
#include<iostream>
#include<sstream>
#include<fstream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<functional>
#include<climits>
#include<utility>
#include <iomanip>
#include<map>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;

#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define REP(i,x) FOR(i,0,x)
#define CLR(a) memset((a), 0 ,sizeof(a))


const int MOD = 1e+9+7;
const double PI  = acos(-1.0);

string getOneStr(int R, int Y, int B){
    string ret="";
    vector< pair<int, string> > lst;
    lst.push_back(pair<int, string>(R,"R"));
    lst.push_back(pair<int, string>(Y,"Y"));
    lst.push_back(pair<int, string>(B,"B"));
    sort(lst.begin(), lst.end());
    int total=R+Y+B;
    int onemax=lst[2].first;
    if(onemax > total-onemax) return "";
    REP(i,onemax){
        ret=ret+lst[2].second;
        if(i<lst[0].first) ret=ret+lst[0].second;
        if(onemax-i-1<lst[1].first) ret=ret+lst[1].second;
    }
    return ret;
}

int main(){
    int T;
    cin>>T;
    REP(t,T){
        cout<<"Case #"<<(t+1)<<": ";
        int n;
        int R,O,Y,G,B,V;
        cin>>n>>R>>O>>Y>>G>>B>>V;
        if((R<G) || (Y<V) || (B<O)){
            cout<<"IMPOSSIBLE"<<"\n";
            continue;
        }
        string header="";
        int loopf=0;
        if(G!=0 && R==G){
            REP(i,R){
                header=header+"GR";
            }
            loopf+=1;
            R=0,G=0;
        }
        if(V!=0 && Y==V){
            REP(i,Y){
                header=header+"VY";
            }
            loopf+=1;
            V=0,Y=0;
        } 
        if(O!=0 && B==O){
            REP(i,B){
                header=header+"OB";
            }
            loopf+=1;
            O=0,B=0;
        }
        if(loopf>1 ||( loopf==1 && R+B+Y+G+V+O!=0)){
            cout<<"IMPOSSIBLE"<<"\n";
            continue;
        }

        string onestr=getOneStr(R-G, Y-V, B-O);
        if(onestr == "" && R-G+Y-V+B-O!=0){
            cout<<"IMPOSSIBLE"<<"\n";
            continue;
        }else{
            cout<<header;
            REP(i, onestr.size()){
                switch(onestr[i]){
                    case 'R':
                    cout<<"R";
                    if(G!=0){
                        REP(j,G) cout<<"GR"; 
                    }
                    G=0;
                    break;
                    case 'Y':
                    cout<<"Y";
                    if(V!=0){
                        REP(j,V) cout<<"VY";
                         
                    }
                    V=0;
                    break;
                    case 'B':
                    cout<<"B";
                    if(O!=0){
                        REP(j,O) cout<<"OB";
                    }
                    O=0;
                    break;
                }
            }
            cout<<"\n";
        }
    }
}
