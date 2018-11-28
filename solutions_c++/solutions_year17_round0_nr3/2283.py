#include <bits/stdc++.h>
using namespace std;


    map <long long, long long> myMap;
    long long n, k, t;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> t;
    for (int u = 1; u<=t; u++)
    {
        cin >> n >> k;
        myMap.clear();
        myMap[n]=1;

        map <long long, long long>::iterator it = myMap.end();
        it--;
        long long key = (*(it)).first;
        long long data=(*(it)).second;
        while (data <k)
        {
                myMap.erase(it);
                if (key % 2 == 1) myMap[key/2]+=2*data;
                else {
                    myMap[key/2]+=data;
                    myMap[key/2-1]+=data;
                }
                k =k - data;

                it = myMap.end();
                it--;
                key = (*(it)).first;
                data=(*(it)).second;

        }
        cout << "Case #" << u << ": ";
        if (key % 2 == 1) cout << key /2 << " " << key/2 << endl;
        else cout << key/2 << " " << key/2 -1 << endl;
    }
}
