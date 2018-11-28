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
    ofstream fout ("B-large.out");
    ifstream fin ("B-large.in");
    fin>>t;
    // cin>>t;
    rep(_,t){
        int k;
        string s;

        fin>>s;
        // cin>>s;
        
        for(int i = 0 ; i < s.length()-1;i++){
            if(s[i] > s[i+1]){
                s[i]--;
                for(int j = i+1;j<s.length();j++){
                    s[j] = '9';
                }
                i = -1;
            }
        }

        fout<<"Case #"<<_+1<<": ";
        // cout<<"Case #"<<_+1<<": ";
        int i = 0;
        if(s[0] =='0'){
            i++;
        }
        for(;i< s.length();i++){
            fout<<s[i];
            // cout<<s[i];
        }
        fout<<endl;
        // cout<<endl;

    }

    return 0;
}
