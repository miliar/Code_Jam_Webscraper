#pragma comment(linker, ”/STACK:38777216“
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <time.h>
#include <map>
#include <set>

using namespace std;

const int N = 1005;
const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;

int t,k,n;
string answ = "IMPOSSIBLE";
int a[10];
pair <int, pair<char,int> > p[5];
map <char,char> lev;
int mp[5];
map < pair<char,char>,bool > mark;

void update(int i){
    if(mp[i] == 0){
        mp[i] = 1;
        for(int j=1;j<=a[p[i].second.second];j++){
            char x = p[i].second.first;
            answ += x;
            answ += lev[x];
        }
    }
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    lev['B'] = 'O';
    lev['R'] = 'G';
    lev['Y'] = 'V';

    cin>>t;
    mark[make_pair('B','O')] = mark[make_pair('O','B')] = 1;
    mark[make_pair('R','G')] = mark[make_pair('G','R')] = 1;
    mark[make_pair('Y','V')] = mark[make_pair('V','Y')] = 1;

    mark[make_pair('R','Y')] = mark[make_pair('Y','R')] = 1;
    mark[make_pair('R','V')] = mark[make_pair('V','R')] = 1;
    mark[make_pair('V','B')] = mark[make_pair('B','V')] = 1;
    while(t--){
        k++;
        cin>>n;
        for(int i=1;i<=6;i++)cin>>a[i];
        answ = "IMPOSSIBLE";
        mp[1] = mp[2] = mp[3] = 0;
        if(a[1] >= a[4] && a[3] >= a[6] && a[5] >= a[2]){
            if(a[1] - a[4] == 0 && a[1] > 0){
                if(a[2] == 0 && a[3] == 0 && a[5] == 0 && a[6] == 0){
                    answ = "";
                    for(int i=1;i<=a[1];i++){
                        answ += 'R';
                        answ += 'G';
                    }
                    printf("Case #%d: ",k);
                    cout<<answ<<endl;
                }
                else{
                    printf("Case #%d: ",k);
                    cout<<answ<<endl;
                }
                continue;
            }
            if(a[3] - a[6] == 0 && a[3] > 0){
                if(a[2] == 0 && a[4] == 0 && a[5] == 0 && a[1] == 0){
                    answ = "";
                    for(int i=1;i<=a[3];i++){
                        answ += 'Y';
                        answ += 'V';
                    }
                    printf("Case #%d: ",k);
                    cout<<answ<<endl;
                }
                else{
                    printf("Case #%d: ",k);
                    cout<<answ<<endl;
                }
                continue;
            }
            if(a[5] - a[2] == 0 && a[5] > 0){
                if(a[1] == 0 && a[3] == 0 && a[4] == 0 && a[6] == 0){
                    answ = "";
                    for(int i=1;i<=a[5];i++){
                        answ += 'B';
                        answ += 'O';
                    }
                    printf("Case #%d: ",k);
                    cout<<answ<<endl;
                }
                else{
                    printf("Case #%d: ",k);
                    cout<<answ<<endl;
                }
                continue;
            }
            p[1] = make_pair(a[1] - a[4] , make_pair('R' , 4));
            p[2] = make_pair(a[3] - a[6] , make_pair('Y' , 6));
            p[3] = make_pair(a[5] - a[2] , make_pair('B' , 2));
            sort(p+1,p+4);
            reverse(p+1,p+4);
            if(p[1].first <= p[2].first + p[3].first){
                answ = "";
                int t1 = (-p[1].first + p[2].first + p[3].first) / 2;
                int t2 = (-p[1].first + p[2].first + p[3].first) / 2 + (-p[1].first + p[2].first + p[3].first) % 2;
                for(int i=1;i<=p[1].first;i++){
                    update(1);
                    answ += p[1].second.first;
                    if(p[2].first != t2){
                        update(2);
                        answ += p[2].second.first;
                        p[2].first--;
                        continue;
                    }
                    update(3);
                    answ += p[3].second.first;
                    p[3].first--;
                }
                int z = 0;
                while(true){
                    if(t1 == 0 && t2 == 0)break;
                    if(z % 2 == 0){
                        t2--;
                        update(2);
                        answ += p[2].second.first;
                    }
                    else{
                        t1--;
                        update(3);
                        answ += p[3].second.first;
                    }
                    z++;
                }
            }
        }
        printf("Case #%d: ",k);
        cout<<answ<<endl;
    }
    return 0;
}
