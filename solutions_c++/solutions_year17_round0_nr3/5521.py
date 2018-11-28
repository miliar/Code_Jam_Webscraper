#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

//A dumb solution first

char stalls[1000009];
int t, nCase=1;
long long n,k, ls, rs;
int main()
{

    scanf("%d", &t);
    while(t--) {
        scanf("%lld %lld", &n, &k);
        n = n+2;
        memset(stalls, '0', sizeof(char) * n);
        stalls[0] = '1';
        stalls[n-1] = '1';

        long long y = 0, z = 0;
        vector<pair<int, pair<long long, long long> > > choices;
        while(k--) {
            ls = rs = 0;
            int posMin = 0, posMax = 0;
            long long ls_max, rs_max;
            long long ls_min, rs_min;
            ls_max = rs_max = -1;
            ls_min = rs_min = -1;
            int nMin = 1;
            for (int i = 0; i < n; i++) {
                if (stalls[i] == '1')
                    continue;

                bool ldone = false, rdone = false;
                long long counter = 1;
                ls = rs = 0;
                while(!ldone || !rdone) {
                    if (!ldone && stalls[i-counter] == '0') {
                        ls++;
                    } else {
                        ldone = true;
                    }

                    if (!rdone && stalls[i+counter] == '0') {
                        rs++;
                    } else {
                        rdone = true;
                    }

                    counter++;
                }

                //printf("%lld %lld %lld %lld %lld %lld\n", ls, rs, ls_min, rs_min, ls_max, rs_max);

                if (std::min(ls,rs) > std::min(ls_min, rs_min)) {
                    choices.clear();
                    z = std::min(ls,rs);
                    ls_min = ls;
                    rs_min = rs;
                    posMin = i;
                    nMin = 0;
                    choices.push_back(make_pair(i,make_pair(ls,rs)));
                } else if (std::min(ls,rs) == std::min(ls_min,rs_min)) {
                    choices.push_back(make_pair(i,make_pair(ls,rs)));
                }
            }

            pair<int, pair<long long, long long> > choice;
            choice = choices[0];
            if (choices.size() > 1) {
                vector<pair<int, pair<long long, long long> > >::iterator it = choices.begin();
                long long smax = std::max(it->second.first, it->second.second);
                it++;
                for (it; it != choices.end(); it++) {
                    if (std::max(it->second.first, it->second.second) > smax) {
                        smax = std::max(it->second.first, it->second.second);
                        choice = *it;
                    }
                }
            }

            int position = choice.first;
            y = std::max(choice.second.first, choice.second.second);
            z = std::min(choice.second.first, choice.second.second);
            //printf("%d\n", position);
            stalls[position]= '1';
            //for (int i = 0; i < n; i++)
                //printf("%c ", stalls[i]);
            //printf("\n\n");
        }

        printf("Case #%d: %lld %lld\n", nCase++, y, z);
    }

    return 0;
}
