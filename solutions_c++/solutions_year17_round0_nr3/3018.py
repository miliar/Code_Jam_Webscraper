#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <cmath>
#include <vector>
#include <stack>
#include <bitset>

//#define cin in
//#define cout out

using namespace std;

const int INF = (int)1e9;
typedef int64_t ll;


int main()
{
//    ifstream in;
//    in.open("/home/vlad/QtProjects/ICM/ICMtrain/C-large.in");
//    ofstream out;
//    out.open("/home/vlad/QtProjects/ICM/ICMtrain/output.txt");
    int n_t;
    cin >> n_t;
    vector<ll> ans(n_t);
    for(int test = 0; test < n_t; ++test){
        ll N, K;
        cin >> N >> K;
        map<ll, ll> room;
        room[N] = 1;
        ll cK = 0;
        ll last = N;
        while(cK < K){
            map<ll, ll>::iterator it = room.end();
            --it;
            room.erase(it->first);
            last = it->first;;
            cK += it->second;
            ll n = it->second, a = it->first / 2, b = it->first - a - 1;
            if(a != 0){
                if(room.find(a) != room.end()){
                    room[a] = room[a] + n;
                }
                else room[a] = n;
            }
            if(b != 0){
                if(room.find(b) != room.end()){
                    room[b] = room[b] + n;
                }
                else room[b] = n;
            }
        }
        ans[test] = last;
    }
    for(int i = 0; i < n_t; ++i){
        cout << "Case #" << i + 1 << ": ";
        cout << (ans[i] / 2) << ' ' << (ans[i] - ans[i] / 2 - 1);
        cout << endl;
    }

}




