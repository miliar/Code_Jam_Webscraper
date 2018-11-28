#include<iostream>
#include<set>
#include<queue>
#include<cstdio>
#include<algorithm>
using namespace std;
struct Dragon{
    int nowH;
    int nowA;
    int eleA;
    int eleH;
    Dragon(int a,int b,int c,int d):nowH(a),nowA(b),eleH(c),eleA(d){
    }
    bool operator <(const Dragon &tmp)const{
        if(nowH != tmp.nowH)return nowH < tmp.nowH;
        if(nowA != tmp.nowA)return nowA < tmp.nowA;
        if(eleH != tmp.eleH)return eleH < tmp.eleH;
        return eleA < tmp.eleA;
    }
};
struct XD{
    Dragon d;
    int t;
    XD(Dragon _d,int _t):d(_d),t(_t){
    }
};
int main (){
    int T;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("CSout.txt","w",stdout);

    cin >> T;
    for(int ca=1;ca<=T;ca++){
        int nowH,nowA,eleH,eleA,B,D;
        cin >> nowH >> nowA >> eleH >> eleA >> B >> D;
        queue<XD> q;
        Dragon fd = Dragon(nowH,nowA,eleH,eleA);
        q.push(XD(fd,0));
        set<Dragon> s;
        s.insert(fd);
        int ans = -1;
        while(!q.empty()){
            int nowT = q.front().t;
            Dragon nowD = q.front().d;

            q.pop();
            if(nowD.eleH - nowD.nowA <= 0){
                ans = nowT+1;
                break;
            }
             Dragon newD = Dragon(0,0,0,0);
            //Attack
            if(nowD.nowH - nowD.eleA > 0){
                newD = Dragon(nowD.nowH - nowD.eleA,nowD.nowA,nowD.eleH - nowD.nowA,nowD.eleA);
                set<Dragon>::iterator it;
                it = s.find(newD);
                if( it == s.end() ){
                    q.push(XD(newD,nowT+1));
                    s.insert(newD);
                }
            }
            //Buff
            if(nowD.nowH - nowD.eleA > 0){
                newD = Dragon(nowD.nowH - nowD.eleA,nowD.nowA + B,nowD.eleH,nowD.eleA);
                set<Dragon>::iterator it;
                it = s.find(newD);
                if( it == s.end() ){
                    q.push(XD(newD,nowT+1));
                    s.insert(newD);
                }
            }
            //Debuff
            if(nowD.nowH - max(nowD.eleA-D,0) > 0){
                newD = Dragon(nowD.nowH - max(nowD.eleA-D,0),nowD.nowA,nowD.eleH,max(nowD.eleA-D,0) );
                set<Dragon>::iterator it;
                it = s.find(newD);
                if( it == s.end() ){
                    q.push(XD(newD,nowT+1));
                    s.insert(newD);
                }
            }
            //Cure
            if(nowH - nowD.eleA > 0){
                newD = Dragon(nowH - nowD.eleA,nowD.nowA,nowD.eleH,nowD.eleA);
                set<Dragon>::iterator it;
                it = s.find(newD);
                if( it == s.end() ){
                    q.push(XD(newD,nowT+1));
                    s.insert(newD);
                }
            }

        }

        cout << "Case #" << ca <<": ";
        if(ans == -1)cout <<"IMPOSSIBLE\n";
        else cout << ans <<"\n";
    }


    return 0;
}
