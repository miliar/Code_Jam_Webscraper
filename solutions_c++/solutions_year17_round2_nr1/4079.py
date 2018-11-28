#include <bits/stdc++.h>
#define horse pair <double, double>
using namespace std;

const int nmax = 1005;
const double inf = 100000000000.0;

int tests;
int d, n;
double x, y;
double s[nmax];
double k[nmax];
vector <horse> v;

double time_until_meeting(horse &h1, horse &h2) {
    return double(h1.first - h2.first) / (h2.second - h1.second);
}

double time_until_finish(horse &h) {
    double rem = d - h.first;
    if(rem <= 0)
        return 0.0;
    return rem / h.second;
}

double meeting_point(horse &h1, horse &h2) {
    return h1.first + h2.second * time_until_meeting(h1, h2);
}


void fast_forward(horse &h, double time) {
    h.first = h.first + h.second * time;
}

void show_horse(horse x) {
    cerr<<fixed<<setprecision(9)<<"horse(pos="<<x.first<<", speed="<<x.second<<")\n";
}


int main() {
    cin>>tests;
    for(int test=1; test<=tests; test++) {
        v.clear();
        cin>>d>>n;


        cout<<"Case #"<<test<<": ";


        /* v.push_back(make_pair(0.0, inf)); */
        for(int i=1; i<=n; i++) {
            cin>>x>>y;
            v.push_back(make_pair(x, y));
        }
        /* v.push_back(make_pair(d, 0.0)); */

        double current_time = 0.0;
        while(true) {
            cerr<<"================= TIME "<<current_time<<" ======================\n";
            sort(v.begin(), v.end());

            for(auto x:v)
                show_horse(x);

            double min_time = inf;
            int current = -1;

            for(int i=0; i+1<int(v.size()); i++) {
                double t = time_until_meeting(v[i], v[i+1]);

                cerr<<"time_until_meeting("<<i<<", "<<i+1<<") = "<<time_until_meeting(v[i], v[i+1])<<"\n";

                if(0 <= t && t < min_time && meeting_point(v[i], v[i+1]) < d) {
                    min_time = t;
                    current = i;
                }
            }

            if(current == -1) {
                cerr<<"current = -1; nobody catches up with nobody\n";
                break;
            } else {
                cerr<<current<<" catches up with "<<current+1<<"\n";

                for(int i=0; i<int(v.size()); i++)
                    v[i].first = v[i].first + v[i].second * min_time;

                swap(v[current], v[v.size()-1]);
                v.pop_back();
            }

            current_time += min_time;
        }

        cerr<<v.size()<<" horses remaining\n";


        double max_finish_time = 0.0;
        for(auto x:v) {
            max_finish_time = max(max_finish_time, time_until_finish(x));
            cerr<<"horse (pos="<<x.first<<", speed="<<x.second<<") ";
            cerr<<"will finish in "<<time_until_finish(x)<<"\n";
        }

        current_time += max_finish_time;
        cerr<<"current_time: "<<current_time<<"\n";
        cerr<<"cruising speed: "<<d/current_time<<"\n";
        cerr<<"\n";

        cout<<fixed<<setprecision(6)<<d/current_time<<"\n";

    }

    return 0;

}
