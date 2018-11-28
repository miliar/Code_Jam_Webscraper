#include <iostream>
#include <stdio.h>
#include "gcj2017.cpp"
using namespace std;

int main()
{
    freopen("dd.txt","r",stdin);
    freopen("out.txt","w+",stdout);
    Solve sol = Solve();
    sol.input();
    sol.solve();
    sol.output();
    return 0;
}
