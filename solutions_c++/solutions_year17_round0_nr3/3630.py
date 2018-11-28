#include <iostream>
#include <fstream>
#include <queue>


using namespace std;

pair<long, long> get_bathroom(long stall, int people){
    priority_queue<long> stall_list;
    stall_list.push(stall);
    people--;

    while (people){
        long choose_stall = stall_list.top();
        stall_list.pop();

        long amax = choose_stall /2;
        long amin = choose_stall - amax - 1;

        stall_list.push(amax);
        stall_list.push(amin);

        people--;
    }

    long choose_stall = stall_list.top();
    long rmax = choose_stall / 2;
    long rmin = choose_stall - rmax - 1;
    return pair<long, long>(rmax, rmin);
}


int main(){

    ifstream infile("C-small-2-attempt0.in");
    ofstream outfile("f3.out");

    int n;

    infile >> n;

    for (int acase = 0; acase < n; ++acase){
        long stall;
        int people;
        infile >> stall >> people;
        outfile << "Case #" << acase+1 << ": ";
        pair<long, long> result = get_bathroom(stall, people);
        outfile << result.first << " " << result.second << endl;
    }

    infile.close();
    outfile.close();
}