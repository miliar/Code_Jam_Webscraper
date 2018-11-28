#include <bits/stdc++.h>
#define ld long double
using namespace std;

const ld pi=3.14159265359;

struct Cake {
    ld h, r;
    ld x, y;
    Cake () { };
    void be() {
        cin>>r>>h;
    }
    void szamol()  {
        x=r*r*pi;
        y=h*r*pi*2;
    }
    const bool operator< (Cake masik) const {
        return y>masik.y;
    }
};

bool kisebb(Cake a, Cake b) {
    return a.x<b.x;
}

int main()
{
	freopen("be.txt","r",stdin);
	freopen("ki.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=0;tc<t;tc++) {
        int n, k;
        cin>>n>>k;
        vector<Cake> tab(n);
        for(int i=0;i<n;i++) {
            tab[i].be();
            tab[i].szamol();
        }
        sort(tab.begin(),tab.end(),kisebb);
        priority_queue<Cake> kovi;
        ld benney=0;
        ld aktx=0;
        ld maxi=0;
        for(int i=0;i<k;i++) {
            benney+=tab[i].y;
            kovi.push(tab[i]);
        }
        aktx=tab[k-1].x;
        for(int i=k;i<n;i++) {
            if(aktx+benney>maxi) {
                maxi=aktx+benney;
            }
            benney-=kovi.top().y;
            kovi.pop();
            benney+=tab[i].y;
            aktx=tab[i].x;
            kovi.push(tab[i]);
        }
        if(aktx+benney>maxi) {
            maxi=aktx+benney;
        }
        cout<<"Case #"<<tc+1<<": "<<fixed<<setprecision(10)<<maxi<<endl;
	}
    return 0;
}
