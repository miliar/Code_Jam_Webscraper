#include <iostream>
#include <cstdio>
using namespace std;

bool verify(string str){
    for(int i=0; i < str.size(); i++)
        if(str[i] == '-')
            return false;
    return true;
}
int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int t;
    cin >> t;
    for(int f=1; f<=t; f++){
        string pancakes;
        int k, flips = 0;
        cin >> pancakes >> k;
        for(int i=0; i + k <= pancakes.size(); i++){
            if(pancakes[i] == '-'){
                ++flips;
                for(int j=i; j<i+k; j++)
                    pancakes[j] = (pancakes[j] == '-' ? '+' : '-');
            }
        }

        if(verify(pancakes))
            cout << "Case #" << f << ": " << flips << endl;
        else
            cout << "Case #" << f << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
