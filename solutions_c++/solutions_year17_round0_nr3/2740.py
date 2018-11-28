// Probleme B v1

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>
#include <ctime>
#include <algorithm>
#include <string>
#include <set>
#include <cmath>
#include <map>

using namespace std;


int main()
{
    int number;

    cin >> number;


    for(int i = 0; i < number; i++)
    {
        map<long long, long long> s;
        long long n, k;
        cin >> n >> k;

        s[n] = 1;

        long long NbPassage = 0;

        while(NbPassage + s.rbegin()->second < k)
        {
            long long nbActu = s.rbegin()->second;
            NbPassage += nbActu;
            long long maxi = s.rbegin()->first;

            s.erase(maxi);

            maxi--;

            long long premier = maxi / 2;
            long long second = maxi / 2 + maxi % 2;


            if(s.count(premier))
                s[premier]+=nbActu;
            else
                s[premier] = nbActu;

            if(s.count(second))
                s[second]+=nbActu;
            else
                s[second] = nbActu;
        }


        long long mini;
        long long maxi;


        long long nb = s.rbegin()->first - 1;
        mini = (nb / 2);
        maxi = (nb / 2) + (nb % 2);

        cout << "Case #" << i+1 << ": " << maxi << " " << mini << endl;
    }
}
