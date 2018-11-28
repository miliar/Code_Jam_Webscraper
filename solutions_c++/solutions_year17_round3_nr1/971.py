#include <vector>
#include <iostream>
#include <map>
#include <tuple>
#include <algorithm>
#include <cmath>
using namespace std;


int main(){
    long long int ncases;
    cin >> ncases;
    for(long long int i = 0; i < ncases; i++){

        long long int n, k;
        cin >> n;

        cin >> k;
        pair<long long int, long long int> max;
        max.first = 0;
        max.second = 0;

        vector<pair<long long int,long long int>> allp;
        for(long long int j = 0; j < n; j ++){

            pair<long long int,long long int> cur;
            cin >> cur.first;
            cin >> cur.second;

            if(max.first <= cur.first){
                if(max.first == cur.first){
                    max.second = std::max(max.second, cur.second);
                }

                else{
                    max = cur;
                }
            }
            allp.push_back(cur);
            sort(allp.begin(), allp.end(), [](auto &a, auto& b) -> bool{return a.first * a.second > b.second * b.first; });

        }

        long long int counts = 0;
        for(auto c : allp){
            if(c.first == max.first and c.second == max.second){
                counts ++;
            }
        }

        double sum1 = 0.0, sum2 = 0.0;
        double maxd = 0;
        for(long long int j = 0; j < k; j++){
            double r = allp[j].first;
            sum1 += 2 * r * M_PI * allp[j].second; 
            maxd = std::max(maxd, r);
        }
        sum1 += M_PI * maxd * maxd;


        maxd = 0;
        for(long long int j = 0; j < k - 1; j++){
            double r = allp[j].first;
            sum2 += 2 * r * M_PI * allp[j].second; 
            maxd = std::max(maxd, r);
            if(allp[j].first == max.first and allp[j].second == max.second){
                counts--;
            }
        }
        if(counts){
            double r = max.first;
            sum2 += 2 * r * M_PI * max.second; 
            maxd = std::max(maxd, r);
            sum2 += M_PI * maxd * maxd;
        }

        cout << fixed;
        cout.precision(10);
        cout << "Case #" << i + 1<< ": ";
        cout << std::max(sum1 , sum2);

        cout << endl;

    }
}
