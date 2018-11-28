#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <ctime>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <list>
using namespace std;


#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define rerm(i,l,u,m) for(int (i)=(int)(l);(i)<=(int)(u);(i)+=(m))
typedef long long int lli;
typedef long long ll;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
#define pb(x) push_back(x)
#define modu 1000000007


int main(){
    int t;
    ofstream fout ("B-small-attempt3.out");
    ifstream fin ("B-small-attempt3.in");
    fin>>t;
    // cin>>t;
    rep(_,t){
        float N, R, O, Y, G, B, V;
        string s;

        // cin>>N>> R>> O>> Y>> G>> B>> V;
        fin>>N>> R>> O>> Y>> G>> B>> V;
        int imp = 0;
        if(R>(Y+B)){
            imp =1 ;
        } else if(Y>(R+B)){
            imp =1 ;
        } else if(B>(Y+R)){
            imp =1 ;
        }
        float r,y,b;
        r = R/(B+Y);
        y = Y/(B+R);
        b = B/(Y+R);
        char prev ='_';
        char fir ;
        fout<<"Case #"<<_+1<<": ";
        // cout<<"Case #"<<_+1<<": ";
        int i =1;
        if(Y == (R+B)){
            if(r > b){
                prev = 'R';
                R--;
                r = R/(B+Y);
                y = Y/(B+R);
                b = B/(Y+R);
            }else {
                prev = 'B';
                B--;
                r = R/(B+Y);
                y = Y/(B+R);
                b = B/(Y+R);
            }
            // cout<<prev;
            fout<<prev;
        } else if(R == (Y+B)){
            if(b < y){
                prev = 'Y';
                Y--;
                r = R/(B+Y);
                y = Y/(B+R);
                b = B/(Y+R);
            }else {
                prev = 'B';
                B--;
                r = R/(B+Y);
                y = Y/(B+R);
                b = B/(Y+R);
            }
            // cout<<prev;
            fout<<prev;
        } else if(B == (Y+R)){
            if(y < r){
                prev = 'R';
                R--;
                r = R/(B+Y);
                y = Y/(B+R);
                b = B/(Y+R);
            }else {
                prev = 'Y';
                Y--;
                r = R/(B+Y);
                y = Y/(B+R);
                b = B/(Y+R);
            }
            fout<<prev;
            // cout<<prev;
        } else {
            i = 0 ;
        }
        fir = prev;

        // fout<<fir<<endl;

        for( ; imp == 0 && i <N; i++){
            if(prev == '_'){

                if(y < r && r > b){
                    prev = 'R';
                    R--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }else if(y>b){
                    prev = 'Y';
                    Y--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }else {
                    prev = 'B';
                    B--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }
                fir = prev;
            } else if( i == N-2){
                if(R==1 && Y==1){
                    if(fir == 'Y' || (fir!='Y' && prev =='R')){
                        prev = 'Y';
                        Y--;
                        r = R/(B+Y);
                        y = Y/(B+R);
                        b = B/(Y+R);
                    } else {
                        prev = 'R';
                        R--;
                        r = R/(B+Y);
                        y = Y/(B+R);
                        b = B/(Y+R);
                    }
                } else if(R==1 && B==1){
                    if(fir == 'B' || (fir!='B' && prev =='R')){
                        prev = 'B';
                        B--;
                        r = R/(B+Y);
                        y = Y/(B+R);
                        b = B/(Y+R);
                    } else {
                        prev = 'R';
                        R--;
                        r = R/(B+Y);
                        y = Y/(B+R);
                        b = B/(Y+R);
                    }
                }else {
                    if(fir == 'Y' || (fir!='Y' && prev =='B')){
                        prev = 'Y';
                        Y--;
                        r = R/(B+Y);
                        y = Y/(B+R);
                        b = B/(Y+R);
                    }else {
                        prev = 'B';
                        B--;
                        r = R/(B+Y);
                        y = Y/(B+R);
                        b = B/(Y+R);
                    }
                }
            } else if(prev == 'R'){
                if(b < y){
                    prev = 'Y';
                    Y--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }else {
                    prev = 'B';
                    B--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }
            }else if(prev == 'Y'){

                if(b < r ){
                    prev = 'R';
                    R--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }else {
                    prev = 'B';
                    B--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }
            } else {
                if(y < r){
                    prev = 'R';
                    R--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }else {
                    prev = 'Y';
                    Y--;
                    r = R/(B+Y);
                    y = Y/(B+R);
                    b = B/(Y+R);
                }
            }
            // cout<<prev;
            fout<<prev;

        }

        if(imp==1){
            fout<<"IMPOSSIBLE";
            // cout<<"IMPOSSIBLE";
        }
        fout<<endl;
        // fout<<fir<<endl;
        // cout<<endl;
        

    }

    return 0;
}
