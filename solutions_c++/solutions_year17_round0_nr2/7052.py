#include<iostream>
//#include<limits> //numeric_limits for stuff like numeric_limits<int>::max()
//#include<iomanip> //iostream helper stuff like ignore, fixed, setprecision(int), setfill, setw (fieldwidth) get_money, get_time, setbase, setiosflags
//#include<algorithm>
#include<vector>
//#include<cmath>
//#include<climits> //INT_MAX PI etc
//#include<utility> //swap, make_pair, move, etc
//#include<regex>
#include<cstring>
using namespace std;

/*************************template stuff*********************************/
typedef unsigned short us;
typedef long long ll;
typedef unsigned long long ull;

/*vv print all args in macro call along with their names vv*/
#define cerrPrintAll(...) cerr<<"VARS: "; __printAll(#__VA_ARGS__, __VA_ARGS__)
/*http://stackoverflow.com/a/22965289/1102730*/ template <typename Arg1> void __printAll(const char* name, Arg1&& arg1) { std::cerr<<name<<"="<<arg1<<"\n"; } template <typename Arg1, typename... Args> void __printAll(const char* names, Arg1&& arg1, Args&&... args) { const char* comma = strchr(names + 1, ','); std::cerr.write(names, comma - names) << "=" << arg1; __printAll(comma, args...); }
/******************************end template stuff**************************************/

bool tidy(const string& snumber) { //return the loc to the 1st non-sorted 
    if(snumber.size()==1) return snumber.size();
    char last= snumber[0];
    for(auto i = 1; i < snumber.size(); ++i) {
        if (snumber[i] < last) return false;
        last = snumber[i]; 
    }
    return true;
}

int tidyLoc(const string& snumber) { //return the loc to the 1st non-sorted 
    if(snumber.size()==1) return snumber.size();
    char last= snumber[0];
    for(auto i = 1; i < snumber.size(); ++i) {
        if (snumber[i] < last) return i;
        last = snumber[i]; 
    }
    return snumber.size();
}

void removeNondecreasing(string& snumber) {
    char first = snumber[0];
    for (int i= 1; i < snumber.size(); ++i) {
        if(snumber[i]<=first) snumber[i]='0'; 
    }
    //cerrPrintAll(snumber);
    snumber = to_string(stoull(snumber)-1);
}

int main() {
    std::ios::sync_with_stdio(false);
	int n;
    string snumber;
    unsigned long long number;
    cin >> n;
    for(int i=1; i <= n; ++i) {
        cin >> snumber;
        if(tidy(snumber)) {
            //cerr << tidy(snumber) << "\n";
            cout << "Case #" << i << ": " << snumber << "\n";
            continue;
        }
        
        while(!tidy(snumber)) {
            removeNondecreasing(snumber);
        }

        cout << "Case #" << i << ": " << snumber << "\n";
    }
    return 0;    
}
