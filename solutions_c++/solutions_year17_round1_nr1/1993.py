#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define ll long long
int main(){
    freopen("A-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tc=1, t;
    cin>>t;
    while(t--){
        int r,c;
        cin>>r>>c;
        string s[30];
        bool flag[30]={0};
        for(int i=0; i<r; i++){
            cin>>s[i];
            for(int j=0; j<c; j++) flag[i]|=(s[i][j]!='?');
        }
        for(int i=0; i<r; i++){
            if(!flag[i]) continue;
            for(int j=0; j<c; j++){
                if(s[i][j]=='?') continue;
                int k=1;
                while(k<c&&s[i][j+k]=='?'){
                    s[i][j+k]=s[i][j];
                    k++;
                }
                k=1;
                while(j-k>=0&&s[i][j-k]=='?'){
                    s[i][j-k]=s[i][j];
                    k++;
                }
            }
            int j=1;
            while(i+j<r&&!flag[i+j]){
                flag[i+j]=1;
                for(int k=0; k<c; k++) s[i+j][k]=s[i][k];
                j++;
            }
            j=1;
            while(i-j>=0&&!flag[i-j]){
                flag[i-j]=1;
                for(int k=0; k<c; k++) s[i-j][k]=s[i][k];
                j++;
            }
        }
        cout<<"Case #"<<tc++<<": "<<endl;
        for(int i=0; i<r; i++) cout<<s[i]<<endl;
    }
}
