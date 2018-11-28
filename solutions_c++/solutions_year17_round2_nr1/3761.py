#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;
ifstream cin("small_input.txt");
ofstream cout("small_output.txt");
#define INF 1e9+13
int t, d, n;

struct Horse {
    int dist;
    int speed;
};

struct HorseComp{
    bool operator()(const Horse& a, const Horse& b){
        return ((a.dist < b.dist) || (a.dist == b.dist && a.speed << b.speed));
    }
};

double time(Horse a){
    return 1.00*(d - a.dist)/a.speed;
}

double theyMeet(Horse a, Horse b){
    if (a.speed <= b.speed) return INF;
    return (b.dist - a.dist) / (a.speed - b.speed);
}

double solve (int d, const vector<Horse>& h){
    int index = h.size()-1;
    double t = 1.00 * (d - h[index].dist) / h[index].speed;
    for (int i=index - 1; i>=0; --i){
        if (theyMeet(h[i], h[index]) <= time(h[index])){
            continue;
        }
        t = time(h[i]);
        index = i;
    }
    return 1.00 * d / t;
}

int main(){
    cin >> t;
    for (int tt = 1; tt <= t; ++tt){
        cin >> d >> n;
        int maxTime = 0;
        vector <Horse> h(n);
        for (int i=0;i<n;++i){
            cin >> h[i].dist >> h[i].speed;
        }
        sort(h.begin(), h.end(), HorseComp());
        cout << "Case #" << fixed << setprecision(10) << tt << ": " << solve(d, h) <<"\n";
    }
    return 0;
}
