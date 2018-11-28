#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream f("tidy.in");
    ofstream g("tidy.out");
    int i, j, cf, t, c = 1;
    string n;
    f >> t;
    while(t--){
        n.clear();
        f >> n;
        g << "Case #" << c << ": ";
        c++;
        for(i=1; i<n.size() && n[i-1] <= n[i]; i++);
        if(i == n.size()){
            g << n << "\n";
            continue;
        }
        else{
            while(n[i-1] > n[i] ) n[--i] --;
            for(++i; i<n.size(); i++)
                n[i] = '9';
            if(n[0] == '0'){
                for(i=1; i<n.size(); i++)
                    g << n[i];
                g << "\n";
                continue;
            }
            g << n << "\n";
        }
    }
}
