#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

double maxOf(double a, double b) {
    return (a>b)?a:b;
}

double minOf(double a, double b) {
    return (a<b)?a:b;
}

double absOf(double a) {
    return (a>0)?a:-a;
}

int main() {
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");

    int testCase;
    fin >> testCase;

    double total_distance,number_of_horses;

    for(int t=0;t<testCase;t++) {
        fin >> total_distance;
        fin >> number_of_horses;

        vector<pair<double,double > > l;

        for(int n=0;n<number_of_horses;n++) {
            double k,s;
            fin >> k;
            fin >> s;

            l.push_back(make_pair(total_distance-k,s));
        }

        sort(l.rbegin(),l.rend());

        double prev_distance = -1;
        double prev_max_speed = -1;
        double prev_time_taken = -1;

        double last_clash_point = -1;

        while(!l.empty()) {
            double distance_remaining = l.back().first;
            double max_speed = l.back().second;
            l.pop_back();

            double timeTaken = distance_remaining/max_speed;

            if(timeTaken > prev_time_taken) {
                prev_time_taken = timeTaken;
                prev_distance = distance_remaining;
                prev_max_speed = max_speed;

                last_clash_point = -1;
            }else {
                if(last_clash_point == -1) {
                    double relative_speed = absOf(prev_max_speed - max_speed);
                    double relative_distance = absOf(prev_distance - distance_remaining);
                    double time_taken = relative_distance / relative_speed;
                    last_clash_point = distance_remaining - (time_taken * max_speed);

                    time_taken = time_taken + last_clash_point/minOf(max_speed,prev_max_speed);
                    prev_time_taken = time_taken;
                    prev_max_speed = minOf(max_speed,prev_max_speed);;
                    prev_distance = last_clash_point;
                }
            }
        }

        //cout.precision(17);

        double effective_speed = total_distance/prev_time_taken;
        fout << "Case #" << t+1 << ": ";
        fout.precision(6);
        fout << fixed << effective_speed << endl;

    }
}