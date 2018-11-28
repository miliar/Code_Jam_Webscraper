#include <bits/stdc++.h>
using namespace std;
int main(){
    ifstream infile;
    ofstream outfile;
    long long t;
    infile.open("B-small-attempt0.in");
    outfile.open("B-output.out");
    infile>>t;
    for(long long tk=1;tk<=t;tk++){
        long n;
        infile >> n;
        long r,g,y,b,o,v;
        infile>>r>>o>>y>>g>>b>>v;
        bool answerf = true;
        if( 2*g > r || 2*o > b || 2*v > y)
            answerf = false;
        r -= 2*g;
        b -= 2*o;
        y -= 2*v;
        vector<pair<long,char> > arr;
        arr.push_back(make_pair(r+g,'R'));
        arr.push_back(make_pair(y+v,'Y'));
        arr.push_back(make_pair(b+o,'B'));
        sort(arr.begin(),arr.end());
        if(arr[0].first + arr[1].first < arr[2].first){
            answerf = false;
        }
        if(answerf) {
            string s = "";
            char fi, sec, th;
            fi = arr[0].second;
            sec = arr[1].second;
            th = arr[2].second;
            long excess = arr[0].first - (arr[2].first - arr[1].first);
            long secval = arr[1].first;
            while(n) {
                if(th == 'R') {
                    if(r){
                        s += 'R';
                        r--;
                        n--;
                    } else if(g) {
                        s += "RGR";
                        g--;
                        n -= 3;
                    }
                } else if (th == 'B') {
                    if(b){
                        s += 'B';
                        b--;
                        n--;
                    } else if(o) {
                        s += "BOB";
                        o--;
                        n -= 3;
                    }
                } else {
                    if(y){
                        s += 'Y';
                        y--;
                        n--;
                    } else if(g) {
                        s += "YVY";
                        v--;
                        n -= 3;
                    }
                }
                if(secval){
                    secval--;
                    if(sec == 'R') {
                        if(r){
                            s += 'R';
                            r--;
                            n--;
                        } else if(g) {
                            s += "RGR";
                            g--;
                            n -= 3;
                        }
                    } else if (sec == 'B') {
                        if(b){
                            s += 'B';
                            b--;
                            n--;
                        } else if(o) {
                            s += "BOB";
                            o--;
                            n -= 3;
                        }
                    } else {
                        if(y){
                            s += 'Y';
                            y--;
                            n--;
                        } else if(g) {
                            s += "YVY";
                            v--;
                            n -= 3;
                        }
                    }
                } else {
                    if(fi == 'R') {
                        if(r){
                            s += 'R';
                            r--;
                            n--;
                        } else if(g) {
                            s += "RGR";
                            g--;
                            n -= 3;
                        }
                    } else if (fi == 'B') {
                        if(b){
                            s += 'B';
                            b--;
                            n--;
                        } else if(o) {
                            s += "BOB";
                            o--;
                            n -= 3;
                        }
                    } else {
                        if(y){
                            s += 'Y';
                            y--;
                            n--;
                        } else if(g) {
                            s += "YVY";
                            v--;
                            n -= 3;
                        }
                    }
                }
                if(excess) {
                    excess--;
                    if(fi == 'R') {
                        if(r){
                            s += 'R';
                            r--;
                            n--;
                        } else if(g) {
                            s += "RGR";
                            g--;
                            n -= 3;
                        }
                    } else if (fi == 'B') {
                        if(b){
                            s += 'B';
                            b--;
                            n--;
                        } else if(o) {
                            s += "BOB";
                            o--;
                            n -= 3;
                        }
                    } else {
                        if(y){
                            s += 'Y';
                            y--;
                            n--;
                        } else if(g) {
                            s += "YVY";
                            v--;
                            n -= 3;
                        }
                    }

                }
            }
            outfile<<"Case #"<<tk<<": "<<s;
            outfile<<endl;
        } else {
            outfile<<"Case #"<<tk<<": IMPOSSIBLE"<<endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
