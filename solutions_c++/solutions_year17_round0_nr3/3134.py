#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int testy;
long long n,k;

int main() {

    cin>>testy;

    for(int t=1; t<=testy; ++t) {
        cin>>n>>k;
        long long m = n+k;
        long long pot = 1;
        long long suma = 0;
        long long ilemn = n;
        long long liczbamn = 1;
        long long ilewie = n;
        long long liczbawie = 0;
        long long b1, b2, b3, b4;
        long long lm1, ilelm1, lw1, ilelw1, lm2, ilelm2, lw2, ilelw2;
        while (suma<k) {
            suma+=pot;
            pot*=2;
            b1 = ilemn; b2=liczbamn; b3=ilewie; b4=liczbawie;
            lm1 = (ilemn-1)/2;
            ilelm1 = liczbamn;
            lw1 = ilemn/2;
            ilelw1 = liczbamn;
            lm2 = (ilewie-1)/2;
            ilelm2 = liczbawie;
            lw2 = ilewie/2;
            ilelw2 = liczbawie;
            //cout<<":"<<lm1<<" "<<ilelm1<<" "<<lw1<<" "<<ilelw1<<endl;
            //cout<<":"<<lm2<<" "<<ilelm2<<" "<<lw2<<" "<<ilelw2<<endl;
            vector < pair <long long, long long> > licznosci;
            licznosci.clear();
            licznosci.push_back(make_pair(lm1,ilelm1));
            licznosci.push_back(make_pair(lw1,ilelw1));
            licznosci.push_back(make_pair(lm2,ilelm2));
            licznosci.push_back(make_pair(lw2,ilelw2));
            sort(licznosci.begin(), licznosci.end());
            vector < pair <long long, long long> > dalej;
            dalej.clear();
            dalej.push_back(make_pair(licznosci[0].first, licznosci[0].second));
            for (int i=1; i<licznosci.size(); ++i) {
                if (licznosci[i].first == licznosci[i-1].first) {
                    dalej[dalej.size()-1].second += licznosci[i].second;
                }
                else dalej.push_back(make_pair(licznosci[i].first, licznosci[i].second));
            }
            //if(dalej.size()>2) cout<<"NO NIE NO:::::::::::::::::::::::::::::::::::::::::::::"<<endl;
            ilemn = dalej[0].first;
            liczbamn = dalej[0].second;
            if (dalej.size()>1) {
                ilewie = dalej[1].first;
                liczbawie = dalej[1].second;
            }
            else {
                ilewie = dalej[0].first;
                liczbawie = 0;
            }
            //cout<<"!"<<ilemn<<" "<<liczbamn<<" "<<ilewie<<" "<<liczbawie<<endl;
        }

        pot/=(long long)2;

            //cout<<"!!!"<<pot<<":"<<b1<<" "<<b2<<" "<<b3<<" "<<b4<<endl;
            long long minodl, maxodl;
        if (b4>=(k-(pot-1))) {
            minodl = (b3-1)/2;
            maxodl = b3/2;

        }
        else {
            minodl = (b1-1)/2;
            maxodl = b1/2;
        }
        cout<<"Case #"<<t<<": "<<maxodl<<" "<<minodl<<"\n";
    }

    return 0;
}
