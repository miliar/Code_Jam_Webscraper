#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <tuple>
typedef long long ll;
using namespace std;
int t,n,k,a,b,ac,aj;
double pi = atan(1)*4;

void solve(int Case){
    vector<tuple<int,int,bool> > vals;
    cin >> ac >> aj;
    for(int i=0; i<ac; i++){
        cin >> a >> b;
        vals.push_back(make_tuple(a,b,0));
    }
    for(int i=0; i<aj; i++){
        cin >> a >> b;
        vals.push_back(make_tuple(a,b,1));
    }
    sort(vals.begin(), vals.end());
    vals.push_back(make_tuple(get<0>(vals[0])+1440, get<1>(vals[0])+1440, get<2>(vals[0]) ) );
    vector< vector<int> > gaps (3);
    vector<int> times (2,0);
    int swaps = 0;
    int prevend = get<1>(vals[0]);
    int prevtype = get<2>(vals[0]);
    for(int i=1; i<ac+aj+1; i++){
        int newstart = get<0>(vals[i]);
        int newend = get<1>(vals[i]);
        int newtype = get<2>(vals[i]);
        times[newtype] += newend - newstart;
        if(prevtype!=newtype){
            ++swaps;
            gaps[2].push_back(newstart - prevend);
        }else{
            gaps[newtype].push_back(newstart - prevend);
            times[newtype] += newstart - prevend;
        }
        prevend = newend;
        prevtype = newtype;
    }
    for(int i=0; i<3; i++) sort(gaps[i].rbegin(), gaps[i].rend());
    if(times[0]<=720 && times[1] <= 720){
        cout << "Case #" << Case << ": " << swaps << "\n";
        return;
    }
    int sind = 0;
    while(times[0] > 720){
        times[0] -= gaps[0][sind];
        sind++;
        swaps+=2;
    }
    sind = 0;
    while(times[1] > 720){
        times[1] -= gaps[1][sind];
        sind++;
        swaps+=2;
    }
    cout << "Case #" << Case << ": " << swaps << "\n";
}



int main()
{
    ios::sync_with_stdio(false);
    cout.precision(17);
    cin >> t;
    for(int i=0; i<t; i++){
        solve(i+1);
    }
    return 0;
}