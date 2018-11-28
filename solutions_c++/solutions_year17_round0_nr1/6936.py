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
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    fin>>t;
    // cin>>t;
    rep(_,t){
        int k;
        string s;

        fin>>s>>k;
        // cin>>s>>k;
        int num = 0;
        char frFlip, curr ;
        for(int i = 0 ; i < s.length() -(k -1); i++){
            frFlip = s[i];
            if(s[i] == '-'){
                num++;
                for( int j = i ; j < (i + k) && j < s.length(); j ++ ){
                    // cout<<j<<" " <<s[j]<<",";
                    if(s[j] == '-'){
                        s[j] = '+';
                    }else {
                        s[j] = '-';
                    }
                }
                // cout<<" " << s<<endl;
            }
        }
        for(int i = 0 ; i < s.length(); i++){
            if(s[i] == '-'){
                num = -1;
            }
        }

        fout<<"Case #"<<_+1<<": ";
        // cout<<"Case #"<<_+1<<": ";
        if(num == -1){
            fout<<"IMPOSSIBLE"<<endl;
            // cout<<"IMPOSSIBLE"<<endl;
        }else {
            fout<<num<<endl;
            // cout<<num<<endl;
        }

    }

    return 0;
}
