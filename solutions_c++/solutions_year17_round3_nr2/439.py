#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <stack>
#include <queue>
#include <array>
#include <algorithm>
#include <cmath>
#include <complex>
#include <map>
#include <cassert>
#include <functional>
#include <stdarg.h>
#include <iomanip>

#define FOR(i, a, b) for(int i=(a);i<=(b);i++)
#define FORD(i, a, b) for(int i=(a);i>=(b);i--)
#define REP(i, b) for(int i=0;i<(b);i++)
#define ll long long
#define nl printf("\n")

// M_PI SI TREBA ODLOZIT

using namespace std;

typedef long double ld;

int count_dlzka(int l, int r, bool rovnako){
    if (l == r && rovnako){
        return 24 * 60 - l + r;
    }
    else if (l == r && !rovnako){
        return 0;
    }
    else if (l >= r){
        return 24 * 60 - l + r;
    }
    else {
        return r - l;
    }
}

int main(){
    //string m;
    int t;
    ll n, k;
    cin>>t;
    for (int tt = 0; tt < t; tt++){
        cout<<"Case #"<<(tt+1)<<": ";
        ll ac, aj;
        cin>>ac>>aj;
        ll ci, di;
        vector<pair<ll, pair<ll, int> > > intervals;
        REP(i, ac){
            cin>>ci>>di;
            intervals.push_back(make_pair(ci,make_pair(di, 0)));
        }

        REP(i, aj){
            cin>>ci>>di;
            intervals.push_back(make_pair(ci,make_pair(di, 1)));
        }

        sort(intervals.begin(), intervals.end());

        int vymen = 0;

        int cL = 0;
        int jL = 0;
        int last = intervals[intervals.size()-1].second.second;
        int lastI = intervals[intervals.size()-1].first;
        REP(i, aj+ac){
            int dlzka = count_dlzka(lastI, intervals[i].first, i==0);
            if(last == 0){
                cL += dlzka;
            }
            else {
                jL += dlzka;
            }
            lastI = intervals[i].first;
            if (intervals[i].second.second != last){
                last = intervals[i].second.second;
                vymen++;
            }
        }

        last = intervals[intervals.size()-1].second.second;
        lastI = intervals[intervals.size()-1].second.first;


       // cout<<cL<<endl;
        //cout<<jL<<endl;

        REP(i, aj+ac){
            int dlzka = count_dlzka(lastI, intervals[i].first, i==0);
            if (intervals[i].second.second != last){
                last = intervals[i].second.second;
                if(jL < cL){
                    if(last == 1) {
                        int rozdiel = min(dlzka, (cL-jL)/2);
                        jL+=rozdiel;
                        cL-=rozdiel;
                    }
                }
                else if(cL < jL){
                    if(last == 0) {
                       // cout<<"dlzka "<<dlzka<<" "<<lastI<<" "<<intervals[i].first<<endl;
                        int rozdiel = min(dlzka, (jL-cL)/2);
                        cL+=rozdiel;
                        jL-=rozdiel;
                    }
                }
            }
            lastI = intervals[i].second.first;
        }

        //cout<<cL<<endl;
        //cout<<jL<<endl;


        last = intervals[intervals.size()-1].second.second;
        lastI = intervals[intervals.size()-1].second.first;
        priority_queue<pair<int,int> > rovnake_int;
        REP(i, aj+ac) {
            int dlzka = count_dlzka(lastI, intervals[i].first, i==0);
            if (intervals[i].second.second == last){
                rovnake_int.push(make_pair(dlzka, last));
            }
            else {
                last = intervals[i].second.second;
            }
            lastI = intervals[i].second.first;
        }



        while(cL != jL){
            pair<int,int> dvojica = rovnake_int.top();
           // cout<<"dvojica "<<dvojica.first<<" "<<dvojica.second<<endl;
            rovnake_int.pop();
            if(jL<cL && dvojica.second == 0){
                int rozdiel = min(dvojica.first, (cL-jL)/2);
                jL+=rozdiel;
                cL-=rozdiel;
                vymen+=2;
            }
            else if(cL<jL && dvojica.second == 1){
                int rozdiel = min(dvojica.first, (jL-cL)/2);
                jL-=rozdiel;
                cL+=rozdiel;
                vymen+=2;
            }
        }

       // cout<<cL<<endl;
        //cout<<jL<<endl;
        cout<<vymen<<endl;

       // cout<<std::fixed    <<std::setprecision(12)<<best_sucet * M_PI<<endl;
    }
}