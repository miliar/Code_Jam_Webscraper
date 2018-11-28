#include <bits/stdc++.h>

using namespace std;

ifstream f("date.in");
ofstream g("date.out");


int n, i;

int found(int m){

    if(m==0)
        return 1;

    if(m%10 >= m/10%10)
        return found(m/10);
    else
        return 0;

}

int main()
{

    f>>n;

    for(i=1; i<=n; i++){

        int x;

        f>>x;

        while(!found(x))
            x--;

        g<<"Case #"<<i<<": "<<x<<'\n';


    }


    return 0;
}
