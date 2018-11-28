#include <vector>
#include <iostream>
#include <map>
#include <tuple>
using namespace std;



//map<tuple<int, int, int, int, int, int>, bool> seen;

bool triang(int a, int b, int c){


    if(a > b + c){
        return false;
    }
    if( b > c + a){
        return false;
    }
    if(c > a + b){
        return false;
    }
    return true;
}


bool solve(int r, int g, int b){
    if(triang(r,g,b) == false){
        return false;
    }


    char mc, sc, tc;
    int mi, si, ti;
    if(r >= g  and r >= b){
        mc = 'R';
        mi = r;
        if(g>=b){
            sc = 'Y';
            si = g;
            tc = 'B';
            ti = b;
        }
        else {
            sc = 'B';
            si = b;
            tc = 'Y';
            ti = g;
        }

    }
    if(g >= b  and g >= r){
        mc = 'Y';
        mi = g;
        if(b>=r){
            sc = 'B';
            si = b;
            tc = 'R';
            ti = r;
        }
        else {
            sc = 'R';
            si = r;
            tc = 'B';
            ti = b;
        }
    }
    if(b >= g  and b >= r){
        mc = 'B';
        mi = b;
        if(g>=r){
            sc = 'Y';
            si = g;
            tc = 'R';
            ti = r;
        }
        else {
            sc = 'R';
            si = r;
            tc = 'Y';
            ti = g;
        }
    }
    for(int i = 0; i < mi; i++){
        cout << mc;
        if(si > ti){
            si --;
            cout << sc;
        } else {
            ti --;
            cout << tc;
        }
    }

    if(si != ti){
        cout << sc;
    }
    for(int i = 0; i < ti; i++){
        cout << tc << sc;
    }
    return true;
}


bool solve(int r, int o,int y,int g,int b,int v){

    return solve(r,y,b);
}


int main(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int n;

        cin >> n;
        int r,o,y,g,b,v;
        cin >> r >> o >> y >> g >> b >> v;
        cout << "Case #" << i + 1<< ": ";

        if (false == solve(r,o,y,g,b,v)){
            cout << "IMPOSSIBLE";
        }

        cout << endl;

    }
}
