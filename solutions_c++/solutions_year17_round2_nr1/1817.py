#include "cruise.cpp"

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int t;
    cin >> t;

    for(int i=1; i<=t; i++){
        cout << "Case #" << i << ": ";
        cruise::solve(i);
        cout << endl;
    }


    return 0;
}
