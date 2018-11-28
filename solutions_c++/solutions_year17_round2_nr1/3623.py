#include<bits/stdc++.h>
using namespace std;

/*************************template stuff*********************************/
/*vv prdouble all args in macro call along with their names vv*/
#define cerrPrintAll(...) cerr<<"VARS: "; __printAll(#__VA_ARGS__, __VA_ARGS__)
/*http://stackoverflow.com/a/22965289/1102730*/ template <typename Arg1> void __printAll(const char* name, Arg1&& arg1) { std::cerr<<name<<"="<<arg1<<"\n"; } template <typename Arg1, typename... Args> void __printAll(const char* names, Arg1&& arg1, Args&&... args) { const char* comma = strchr(names + 1, ','); std::cerr.write(names, comma - names) << "=" << arg1; __printAll(comma, args...); }
/******************************end template stuff**************************************/

int main() {
    std::ios::sync_with_stdio(false);

    vector<long> horses;
    vector<double> hspeed;
    vector<double> timeOfArrival;

	double TC, D, N, hPos, maxSpeed;

    cin >> TC;
    for(int i=1; i <= TC; ++i) {
        cin >> D >> N;
        horses.resize(N); hspeed.resize(N); timeOfArrival.resize(N+1); timeOfArrival[N] = 0;
        for ( double j = 0 ; j < N ; ++j) {
            cin >> horses[j]>> hspeed[j];
        }


        //backwards in list to find the times of arrival
        for( double j = N-1; j >=0; j--) {

            long distance= D - horses[j];
            double timeToGet = distance / static_cast<double>(hspeed[j]);
            timeOfArrival[j] = timeToGet;
            if(timeOfArrival[j]< timeOfArrival[j+1]) timeOfArrival[j]= timeOfArrival[j+1];
            //cerrPrintAll("case", i, D, j,  distance, horses[j], hspeed[j], timeToGet, timeOfArrival[j]);
        }

        cout << "Case #" << i << ": " << setprecision(6) << fixed << D/timeOfArrival[0] << "\n";
    }
    return 0;    
}
