#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>

using namespace std;

int main()
{
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);


    long long nbT;
    cin >> nbT;


    long long new1, new2;
    for (long long t = 1; t <= nbT; t++)
    {
        long long taille, nbGens;
        cin >> taille >> nbGens;
        map<long long,long long> gaps;
        gaps[taille] = 1;

        long curNbDone = 0;
        while (curNbDone < nbGens)
        {
            auto itCurTaille = gaps.end();
            itCurTaille--;
            const long long curTaille = itCurTaille->first;
            long long nbCur = itCurTaille->second;
            gaps.erase(itCurTaille);

            //std::cerr << curTaille << "aaaaaa" << taille << std::endl;

            if (curTaille%2)
            {
                new1 = curTaille/(long long)2;
                new2 = curTaille/(long long)2;
            }
            else
            {
                new1 = max((long long)0,curTaille/2-1);
                new2 = curTaille/2;
            }

            auto it1 = gaps.find(new1);
            if (it1 == gaps.end())
                gaps[new1] = nbCur;
            else
                it1->second += nbCur;

            auto it2 = gaps.find(new2);
            if (it2 == gaps.end())
                gaps[new2] = nbCur;
            else
                it2->second += nbCur;
            curNbDone += nbCur;
        }


        std::cout << "Case #" << t << ": " << max(new1, new2) << ' ' << min(new1, new2) << '\n';
        //std::cout << vus.size() << " VS " << log2(taille) << std::endl;
        //break;
    }

    return 0;
}
